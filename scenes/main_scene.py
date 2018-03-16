#main_scene.py

from .scene import Scene
from .scene1_scene import Scene1
import pygame, pygame.locals, sys


class Main(Scene):


    def __init__(self, master):
        Scene.__init__(self, master)

    def processed_input(self, event, master):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                master.switch_scene(Scene1(master))

    def render_scene(self, master):

        master.screen.fill((255, 0, 0))

    def update_scene(self):

        pass


