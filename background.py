import pygame

class Background(object):
    def __init__(self, W, H, sizeFaktorX, sizeFaktorY):
        self.W = W
        self.H = H
        self.sizeFaktorX = sizeFaktorX
        self.sizeFaktorY = sizeFaktorY
        self.bg_x = 0
        self.image = None
        self.load_background('pictures/bg.png')

    def load_background(self, filename):
        img = pygame.image.load(filename).convert()
        meret = img.get_size()
        self.image = pygame.transform.scale(img, (int(meret[0] / self.sizeFaktorX), int(meret[1] / self.sizeFaktorY)))

    def move_right(self):
        if self.bg_x < 0:
            self.bg_x += 1

    def move_left(self):
        if self.bg_x > 0 - self.image.get_rect().width + self.W:
            self.bg_x -= 1

    def can_move_left(self):
        if self.bg_x > 0 - self.image.get_rect().width + self.W:
            return True
        else:
            return False

    def can_move_right(self):
        if self.bg_x < 0:
            return True
        else:
            return False

    def render(self, screen):
        screen.blit(self.image, (self.bg_x, 0))



