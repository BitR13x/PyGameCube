import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Cube3D():
    def __init__(self, vertices, edges) -> None:
        self.vertices = vertices
        self.edges = edges


    # Define the function to draw the 4D cube
    def drawCube(self):
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex4fv(self.vertices[vertex])
        glEnd()



class Player():
    def __init__(self, mouse_rotation_speed) -> None:
        self.mouse_rotation_speed = mouse_rotation_speed
        self.up_down_angle = 0.0


    def move(self):
        keys = pygame.key.get_pressed()
        # 3D movement
        if keys[K_a]:
            glTranslatef(0.1, 0, 0)
        if keys[K_d]:
            glTranslatef(-0.1, 0, 0)
        if keys[K_SPACE]:
            glTranslatef(0, -0.1, 0)
        if keys[K_c]:
            glTranslatef(0, 0.1, 0)
        if keys[K_w]:
            glTranslatef(0, 0, 0.1)
        if keys[K_s]:
            glTranslatef(0, 0, -0.1)


def main():
    vertices = [
        (-1, 1, 1, 1),  # vertex 0
        (1, 1, 1, 1),   # vertex 1
        (1, -1, 1, 1),  # vertex 2
        (-1, -1, 1, 1), # vertex 3
        (-1, 1, -1, 1), # vertex 4
        (1, 1, -1, 1),  # vertex 5
        (1, -1, -1, 1), # vertex 6
        (-1, -1, -1, 1),# vertex 7
        (-1, 1, 1, -1), # vertex 8
        (1, 1, 1, -1),  # vertex 9
        (1, -1, 1, -1), # vertex 10
        (-1, -1, 1, -1),# vertex 11
        (-1, 1, -1, -1),# vertex 12
        (1, 1, -1, -1), # vertex 13
        (1, -1, -1, -1),# vertex 14
        (-1, -1, -1, -1)# vertex 15
    ]

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0), # edges on the front face
        (4, 5), (5, 6), (6, 7), (7, 4), # edges on the back face
        (0, 4), (1, 5), (2, 6), (3, 7), # edges connecting front and back faces
        (0, 8), (1, 9), (2, 10), (3, 11), # edges connecting left and right faces
        (4, 12), (5, 13), (6, 14), (7, 15),  # edges connecting top and bottom faces
        (8, 9), (9, 10), (10, 11), (11, 8), # edges on the front face
        (12, 13), (13, 14), (14, 15), (15, 12), # edges on the back face
        (8, 12), (9, 13), (10, 14), (11, 15), # edges connecting front and back faces
    ]

    mouse_rotation_speed = 0.1
    # Create class for cube and player
    cube = Cube3D(vertices, edges)
    player = Player(mouse_rotation_speed)

    # Initialize Pygame and set up the OpenGL display
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    # Set up a perspective projection with a 120 degree field of view
    gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)

    # Move camera
    gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Clear screen
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # Player Movement
        player.move()

        # Draw cube
        cube.drawCube()


        # Update display
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()