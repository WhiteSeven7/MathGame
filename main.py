import pygame
import sys
import random
from info import Info
from player import Player
from bullet import Bullet
from enemy import Enemy
from menu import PauseMenu, DeathMenu
from timer import RepellMagic, SluggishMagic
from data import *
from color import *


def collide(bullet, enemy):
    return bullet.x - bullet.radius < enemy.rect.right and enemy.rect.left < bullet.x + bullet.radius and bullet.y - bullet.radius < enemy.rect.bottom and enemy.rect.top < bullet.y + bullet.radius


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode(displaySize)
        pygame.display.set_caption("最大公因数")
        self.clock = pygame.time.Clock()
        self.events = None
        self.info = Info()
        self.player = Player(random.randint(0, 4))
        self.bullets: set[Bullet] = set()
        self.Enemy = Enemy
        self.enemys: set[Enemy] = set()
        self.wire = 122
        self.status = 'playing'
        self.pauseMenu = PauseMenu()
        self.deathMenu = DeathMenu()
        self.repellMagic = RepellMagic()
        self.sluggishMagic = SluggishMagic()
        pygame.display.flip()

    def control(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                if pygame.font.get_init():
                    pygame.font.quit()
                pygame.quit()
                sys.exit()

    def playerControl1(self, event):
        if event.key == pygame.K_UP and self.player.line != 0:
            self.player.moveUp()
        elif event.key == pygame.K_DOWN and self.player.line != 4:
            self.player.moveDown()

        if event.unicode in '0123456789' and len(self.player.number.n) < 2:
            self.player.number.write(event.unicode)
        elif event.key == pygame.K_BACKSPACE and len(self.player.number.n) > 0:
            self.player.number.backSpace()
        if event.key == pygame.K_SPACE and self.player.number.n and len(self.bullets) < 6:
            self.bullets.add(
                Bullet(int(self.player.number.n), self.player.line))
            self.player.number.clear()

    def playerControl2(self, event):
        if event.key == pygame.K_a and self.info.repell > 0:
            self.repellMagic.accumulate()
            self.info.repell -= 1
        elif event.key == pygame.K_b and self.info.sluggish > 0:
            self.info.sluggish -= 1
            self.sluggishMagic.accumulate()
        elif event.key == pygame.K_c and self.info.bomb > 0 and len(self.bullets) < 6:
            self.info.bomb -= 1
            self.bullets.add(Bullet('?', self.player.line, 50, bombColor))

    def plyarControl(self):
        for event in self.events:
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_ESCAPE:
                self.status = 'pause'
            self.playerControl1(event)
            self.playerControl2(event)

    def addEnemy(self):
        lines = {0, 1, 2, 3, 4}
        for enemy in self.enemys:
            if enemy.rect.right + 20 > displayWidth and enemy.line in lines:
                lines.remove(enemy.line)
        if not lines:
            return
        if not random.randint(0, 150 * len(self.enemys)):
            self.enemys.add(Enemy(random.choice(tuple(lines)), random.randint(
                1, 100), random.randint(1, 100), self))

    def setEnemySpeed(self):
        E = self.Enemy
        if self.repellMagic.time > 0:
            E.speed = -E.FAST
            return
        for enemy in self.enemys:
            if enemy.rect.right < displayWidth:
                E.speed = E.LOW
                break
        else:
            E.speed = Enemy.FAST
        if self.sluggishMagic.time > 0:
            E.speed = E.speed // 4

    def compare(self, bullet, enemy, killSet):
        if bullet.number.n == '?':
            killSet.add(enemy)
            bullet.set(enemy.answer)
            return
        if bullet.number.n == enemy.answer:
            killSet.add(enemy)
            self.info.grade += 1
            self.info.addByColor(enemy.color)
        else:
            enemy.errorFast.accumulate()
        killSet.add(bullet)

    def collide(self, killSet):
        for bullet in self.bullets:
            for enemy in self.enemys:
                if collide(bullet, enemy):
                    self.compare(bullet, enemy, killSet)
                    break

    def missing(self, killSet):
        for bullet in self.bullets:
            if bullet.x - bullet.radius > displayWidth or bullet.x + bullet.radius < 0:
                killSet.add(bullet)

    def touchWire(self, killSet):
        for enemy in self.enemys:
            if enemy.rect.left < self.wire:
                killSet.add(enemy)
                self.info.lives -= 1
                self.repellMagic.accumulate()
                if self.info.lives < 1:
                    self.status = 'death'
                    self.deathMenu.setGrade(self.info.grade)

    def kill(self):
        killSet = set()
        self.collide(killSet)
        self.missing(killSet)
        self.touchWire(killSet)

        self.enemys -= killSet
        self.bullets -= killSet

    def magicTick(self):
        if self.repellMagic.time > 0:
            self.repellMagic.tick()
        if self.sluggishMagic.time > 0:
            self.sluggishMagic.tick()

    def update(self):
        self.addEnemy()
        self.setEnemySpeed()
        for bullet in self.bullets:
            bullet.move()
        for enemy in self.enemys:
            enemy.move()
        self.magicTick()
        self.kill()

    def pauseControl(self):
        for event in self.events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.status = 'playing'
                return

    def restart(self):
        self.player = Player(random.randint(0, 4))
        self.enemys.clear()
        self.bullets.clear()
        self.info = Info()
        self.status = 'playing'

    def deathControl(self):
        for event in self.events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.restart()
                return

    def run(self):
        while True:
            self.events = pygame.event.get()
            self.control()
            if self.status == 'playing':
                self.plyarControl()
                self.update()
            elif self.status == 'pause':
                self.pauseControl()
            else:
                self.deathControl()

            self.display.fill('black')
            if self.status != 'death':
                self.draw()
                if self.status == 'pause':
                    self.pauseMenu.draw(self.display)
            else:
                self.deathMenu.draw(self.display)
            pygame.display.flip()
            self.clock.tick(FPS)

    def draw(self):
        for i in range(1, 5):
            pygame.draw.line(self.display, gray, (0, 120 * i + 60),
                             (displayWidth, 120 * i + 60), 4)
        pygame.draw.line(self.display, red, (self.wire, 60 + 0),
                         (self.wire, displayHeight), 4)
        for bullet in self.bullets:
            bullet.draw(self.display)
        for enemy in self.enemys:
            enemy.draw(self.display)
        self.player.draw(self.display)
        self.info.draw(self.display)


if __name__ == '__main__':
    game = Game()
    game.run()
