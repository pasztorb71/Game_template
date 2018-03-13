import glob

import pygame


class Knight(object):
    def __init__(self, W, H, sizeFaktorX, sizeFaktorY):
        self.W = W
        self.H = H
        self.sizeFaktorX = sizeFaktorX
        self.sizeFaktorY = sizeFaktorY
        self.kx = self.kx_orig = int(350/sizeFaktorX)
        self.ky = self.ky_orig = int(505/sizeFaktorY)
        self.images_left = []
        self.images_right = []
        self._load_images('pictures/')
        self.images = self.images_right
        self.imagesize = self.images[0].get_rect().width
        self.imcnt = 0
        self.jumpcnt = 0
        self.isjump = 0
        self.cnt = 0
        self.v_orig = self.v = 8
        self.m = 2 / sizeFaktorX

    def _load_images(self, path):
        """
        Loads all images in directory. The directory must only contain images.
        Args:
            path: The relative or absolute pathchange_image to the directory to load images from.
        Returns:
            List of images."""
        for file_name in sorted(glob.glob(path+'Walk*.png')):
            image = pygame.image.load(file_name).convert_alpha()
            meret = image.get_size()
            image = pygame.transform.scale(image, (int(meret[0]/5/self.sizeFaktorX), int(meret[1]/5/self.sizeFaktorY)))
            self.images_right.append(image)
            self.images_left.append(pygame.transform.flip(image, True, False))

    def turn_left(self):    self.images = self.images_left

    def turn_right(self):   self.images = self.images_right

    def render(self, screen):   screen.blit(self.images[self.imcnt], (self.kx, self.ky))

    def change_image(self):
        self.cnt += 1
        if self.cnt == 10:
            self.cnt = 0
            self.imcnt += 1
        if self.imcnt == len(self.images):
            self.imcnt = 0

    def move_right(self):
        if self.kx < self.W-self.imagesize:
            self.kx += 1
            self.change_image()

    def move_left(self):
        if self.kx > 0:
            self.kx -= 1
            self.change_image()

    def knight_is_not_middle(self):  return self.kx != self.kx_orig

    def jump(self):
        if self.isjump == 0:    self.isjump = 1

    def checkJump(self):
        if self.isjump == 1:
            if self.jumpcnt == 7:
                self.jumpcnt = 0
                if self.v > 0:
                    F = (0.2 * self.m * (self.v * self.v))
                else:
                    F = -(0.2 * self.m * (self.v * self.v))
                self.ky = self.ky - F
                self.v -= 1
                if self.ky >= self.ky_orig:
                    self.ky = self.ky_orig
                    self.isjump = 0
                    self.v = self.v_orig
            self.jumpcnt += 1

