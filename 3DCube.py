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


    def camera_vertical(self, mouse_delta_y):
        self.up_down_angle += mouse_delta_y*self.mouse_rotation_speed
        glRotatef(self.up_down_angle, 1.0, 0.0, 0.0)


    def camera_horizontal(self, mouse_delta_x):
        glRotatef(mouse_delta_x*self.mouse_rotation_speed, 0.0, 1.0, 0.0)



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
    
    glMatrixMode(GL_PROJECTION)
    # Set up a perspective projection with a 120 degree field of view
    gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    # Move camera
    gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glLoadIdentity()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        mouse_delta_x, mouse_delta_y = pygame.mouse.get_rel()
        # init model view matrix
        glLoadIdentity()

        # Rotate camera up or down
        player.camera_vertical(mouse_delta_y)

        # init the view matrix
        glPushMatrix()
        glLoadIdentity()
        
        # Player Movement
        player.move()

        # Rotate camera left or right
        player.camera_horizontal(mouse_delta_x)

        # multiply the current matrix by the get the new view matrix and store the final vie matrix 
        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        # apply view matrix
        glPopMatrix()
        glMultMatrixf(viewMatrix)

        # Clear the color and depth buffers
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glPushMatrix()

        # Hide cursor
        pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
        # Lock cursor in middle of screen
        screen_width, screen_height = pygame.display.get_surface().get_size()
        pygame.mouse.set_pos((screen_width // 2, screen_height // 2))

        # Draw cube
        cube.drawCube()

        glPopMatrix()
        # Update display
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()