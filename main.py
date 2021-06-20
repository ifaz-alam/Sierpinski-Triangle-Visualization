"""
A sierpinski triangle visualization using recursion
"""
import pygame
import pygame.gfxdraw

BACKGROUND = (40, 40, 40)
TRIANGLE_COLOUR = (141, 192, 255)

# A constant denoting the side length threshold for the triangle
THRESHOLD = 2

# turn this off if you would simply like to see the final result
visualization = True

# The animation drawing delay in milliseconds
DELAY = 3


def midpoint(v1: tuple[int, int], v2: tuple[int, int]) -> tuple[int, int]:
    """"Return the midpoint of v1 and v2"""
    return (v1[0] + v2[0]) // 2, (v1[1] + v2[1]) // 2


def triangle(screen: pygame.Surface, v1: tuple[int, int], v2: tuple[int, int], v3: tuple[int, int]) -> None:
    """
    :param screen: The screen on which the triangle is to be displayed
    :param v1: An (x, y) tuple representing the lower-left vertex of the triangle
    :param v2: An (x, y) tuple representing the upper vertex of the triangle
    :param v3: An (x, y) tuple representing the lower-right vertex of the triangle

    Draw a sierpinski triangle on the provided screen formed from the provided vertices v1, v2, and v3.
    """
    side_length = v3[0] - v1[0]

    # The sierpinski triangle is recursively divided into smaller triangles infinitely
    # For the sake of this visualization we will stop dividing the triangle once it reaches a small enough threshold
    # This threshold is represented using the variable 'THRESHOLD' which can be found at the top of the program

    if side_length < THRESHOLD:
        # Display the triangle on the screen
        pygame.gfxdraw.aapolygon(screen, [v1, v2, v3], TRIANGLE_COLOUR)
    else:
        # Subdivide the triangle further, and fill the center of the triangle division with "negative space"
        pygame.gfxdraw.aapolygon(screen, [v1, v2, v3], TRIANGLE_COLOUR)

        midpoint1 = midpoint(v1, v2)  # midpoint of /
        midpoint2 = midpoint(v1, v3)  # midpoint of -
        midpoint3 = midpoint(v2, v3)  # midpoint of \

        if visualization:
            pygame.display.flip()
            pygame.time.wait(DELAY)

        # Draw the centre sub-triangle
        pygame.gfxdraw.aapolygon(screen, [midpoint1, midpoint2, midpoint3], (41, 192, 255))

        if visualization:
            pygame.display.flip()
            pygame.time.wait(DELAY)

        # Draw the 3 sub-triangles recursively
        triangle(screen, v1, midpoint1, midpoint2)
        triangle(screen, midpoint1, v2, midpoint3)
        triangle(screen, midpoint2, midpoint3, v3)


if __name__ == '__main__':
    # Initialize the pygame window
    pygame.init()
    pygame.display.set_caption('Sierpinski Triangle Visualization')
    window = pygame.display.set_mode((800, 800))
    window.fill(BACKGROUND)

    # Draw the Sierpinski Triangle
    triangle(window, (100, 620), (400, 100), (700, 620))

    # Display the image on screen
    pygame.display.flip()

    # Wait until the window is closed
    while True:
        if any(event.type == pygame.QUIT for event in pygame.event.get()):
            break
    pygame.display.quit()
    pygame.quit()
