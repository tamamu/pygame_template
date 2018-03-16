#scene2_scene.py

from .scene import Scene
import pygame, pygame.locals, sys


class Scene2(Scene):


    def __init__(self, master):
        Scene.__init__(self, master)

    def processed_input(self, event, master):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                master.switch_scene(Main(master))


    def render_scene(self, master):

        master.screen.fill((0, 0, 255))

    def update_scene(self):

        pass


