import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Cube3D():
    def __init__(self, verticies, edges) -> None:
        self.verticies = verticies
        self.edges = edges

    def drawCube(self):
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(verticies[vertex])
        glEnd()


def main(cube):
    pygame.init()
    clock = pygame.time.Clock()

    display = (400, 300)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        clock.tick(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube.drawCube()

        pygame.display.flip()

if __name__ == "__main__":
    verticies = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
                (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))
    edges = ((0,1), (0,3), (0,4), (2,1),(2,3), (2,7), (6,3), (6,4),(6,7), (5,1), (5,4), (5,7))

    cube = Cube3D(verticies, edges)
    main(cube)

