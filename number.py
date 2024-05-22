class Number:
    def __init__(self, n, font):
        self.n = n
        self.image = font.render(str(n), True, 'white')
        self.offsetX = -self.image.get_width() // 2
        self.offsetY = -self.image.get_height() // 2


class VariateNumber:
    def __init__(self, font):
        self.n = ''
        self.font = font
        self.image = font.render(self.n, True, 'white')
        self.offsetX = -self.image.get_width() // 2
        self.offsetY = -self.image.get_height() // 2

    def _changeImage(self):
        self.image = self.font.render(self.n, True, 'white')
        self.offsetX = -self.image.get_width() // 2
        self.offsetY = -self.image.get_height() // 2

    def clear(self):
        self.n = ''
        self._changeImage()

    def write(self, num):
        self.n += num
        self._changeImage()

    def backSpace(self):
        self.n = self.n[:-1]
        self._changeImage()
