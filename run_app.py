import os
import pygame

from background import Background
from knight import Knight

class App(object):
    sizeFaktorX = 1.5
    sizeFaktorY = 1.5
    windowWidth = 800
    windowHeight = 768
    W, H = int(windowWidth / sizeFaktorX), int(windowHeight / sizeFaktorY)

    def __init__(self):
        self._running = True
        self.screen = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption('Lovag')
        self.bg = Background(self.W, self.H, self.sizeFaktorX, self.sizeFaktorY)
        self.kn = Knight(self.W, self.H, self.sizeFaktorX, self.sizeFaktorY)
        self.clock = None

    def on_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self._running = True

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit(0)

    def on_loop(self):
        self.kn.checkJump()

    def on_render(self):
        self.screen.fill((0, 0, 0))
        self.bg.render(self.screen)
        self.kn.render(self.screen)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            self.on_event()

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                self.kn.turn_left()
                if self.kn.knight_is_not_middle() or not self.bg.can_move_right():
                    self.kn.move_left()
                else:
                    self.bg.move_right()
                    self.kn.change_image()

            elif pressed[pygame.K_RIGHT]:
                self.kn.turn_right()
                if self.kn.knight_is_not_middle() or not self.bg.can_move_left():
                    self.kn.move_right()
                else:
                    self.bg.move_left()
                    self.kn.change_image()
            if pressed[pygame.K_UP]:
                self.kn.jump()

            self.on_loop()
            self.on_render()
            self.clock.tick(600)
        self.on_cleanup()

if __name__ == "__main__":
    app = App()
    app.on_execute()