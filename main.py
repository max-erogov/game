import pygame as pg
import numpy as np


class Game:
    def __init__(self):
        # params
        self.block_size = 96  # in pixels
        self.screen_width = 1536
        self.screen_height = 864
        self.map_width = 50
        self.map_height = 20
        self.visible_map_width = 7
        self.visible_map_height = 4
        self.game_map = np.zeros((self.map_width, self.map_height))  # initialize
        self.game_map[:, self.map_height//2:] = 1  # blocks up to half
        self.bg_color = (0, 192, 255)
        self.block_color = (127, 127, 32)

        # pygame
        pg.init()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.mainloop_active = True
        self.game_active = False

        # game
        self.player_x = 25
        self.player_y = 9
        self.camera_x = 25
        self.camera_y = 9

    def main(self):
        while self.mainloop_active:
            self.check_events()
            self.draw_blocks()
            pg.display.flip()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.mainloop_active = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    self.mainloop_active = False
                elif event.key == pg.K_a:
                    self.left()
                elif event.key == pg.K_d:
                    self.right()

    def draw_blocks(self):
        for x in range(self.camera_x - self.visible_map_width, self.camera_x + self.visible_map_width + 1):
            for y in range(self.camera_y - self.visible_map_height, self.camera_y + self.visible_map_height + 1):
                if self.game_map[x, y] == 0:
                    pg.draw.rect(self.screen, self.bg_color,
                                 (self.block_size//2 + (x - (self.camera_x - self.visible_map_width)) * self.block_size,
                                  (y-(self.camera_y - self.visible_map_height)) * self.block_size,
                                  self.block_size, self.block_size))
                if self.game_map[x, y] == 1:
                    pg.draw.rect(self.screen, pg.Color("black"),
                                 (self.block_size // 2 + (x-(self.camera_x - self.visible_map_width))*self.block_size,
                                  (y-(self.camera_y - self.visible_map_height))*self.block_size,
                                  self.block_size, self.block_size))
                    pg.draw.rect(self.screen, self.block_color,
                                 (self.block_size//2 + 1 + (x-(self.camera_x - self.visible_map_width))*self.block_size,
                                  (y-(self.camera_y - self.visible_map_height))*self.block_size,
                                  self.block_size-2, self.block_size-2))
                if x == self.player_x and y == self.player_y:
                    pg.draw.rect(self.screen, pg.Color("red"),
                                 (self.block_size//2 + (x - (self.camera_x - self.visible_map_width)) * self.block_size,
                                  (y - (self.camera_y - self.visible_map_height)) * self.block_size,
                                  self.block_size, self.block_size))

    def left(self):
        if self.player_x > 0:
            self.player_x -= 1
        if 6 < self.player_x < 42:
            self.camera_x -= 1
        print(self.player_x, self.camera_x)

    def right(self):
        if self.player_x < 49:
            self.player_x += 1
        if 7 < self.player_x < 43:
            self.camera_x += 1
        print(self.player_x, self.camera_x)


if __name__ == '__main__':
    game = Game()
    game.main()
