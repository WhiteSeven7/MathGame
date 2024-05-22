class Timer:
    def __init__(self, cool):
        self.time = 0
        self.COOL = cool
    
    def tick(self):
        self.time -= 1
    
    def reset(self):
        self.time = self.COOL
    
    def accumulate(self):
        self.time += self.COOL

class RepellMagic(Timer):
    def __init__(self):
        super().__init__(120)

class SluggishMagic(Timer):
    def __init__(self):
        super().__init__(450)

class ErrorFast(Timer):
    def __init__(self):
        super().__init__(30)
