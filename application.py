#application.py

from scenes import Scene, Main, Scene1, Scene2
import pygame, pygame.locals, sys


class Director:

    
    def __init__(self):

        self.current_scene = self
        self.screen = pygame.display.set_mode((1000, 600))

    def loop(self, master):

        active_scene = self.current_scene
        while True:
            print(active_scene)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()

            self.current_scene.processed_input(event, self)
            self.current_scene.render_scene(self)
            self.current_scene.update_scene()

            pygame.display.flip()
                        

    def quit(self):

        pygame.quit()
        sys.exit()

    def switch_scene(self, new_scene):

        self.current_scene = new_scene
        print(self.current_scene)


if __name__ == "__main__":
    pygame.init()
    app = Director()
    start_scene = Main(app)
    app.switch_scene(start_scene)
    app.loop(app)
