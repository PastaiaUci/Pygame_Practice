from pygame import *
pygame.init()

screen_width = 500
screen_height = 500

# creting and naming the root
root = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mykull")

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (220, 20, 60)
black = (0, 0, 0)

true = True


def draw_lines(x_coord1, y_coord1):

    # x line
    pygame.draw.line(root, red, coord(0, y_coord1), coord(500, y_coord1), 2)
    # y line
    pygame.draw.line(root, green, coord(x_coord1, 0), coord(x_coord1, 500), 2)

    pygame.display.update()


def display_coord(x_coord, y_coord):

   # getting coord written on screen
    font = pygame.font.Font('freesansbold.ttf', 20)

    X = font.render("X:{}  ".format(coord_x(x_coord)), True, white)
    X_rect = X.get_rect()

    Y = font.render("Y:{}  ".format(coord_y(y_coord)), True, white)
    Y_rect = Y.get_rect()

    Z = font.render("Z:346", True, white)
    Z_rect = Z.get_rect()

    X_rect.center = (35, 15)
    Y_rect.center = (35, 40)
    Z_rect.center = (31, 65)

    root.blit(X, X_rect)
    root.blit(Y, Y_rect)
    root.blit(Z, Z_rect)

    pygame.display.update()


def draw_circle(x_coord2, y_coord2):

    pygame.draw.circle(root, blue, coord(x_coord2, y_coord2), 7, 0)
    pygame.display.update()


def coord(x, y):
    "Convert world coordinates to pixel coordinates."
    return screen_height - x, -screen_width + y


def coord_x(x):
    "Convert world coordinates to pixel coordinates."
    return 600+screen_height - x


def coord_y(y):
    "Convert world coordinates to pixel coordinates."
    return 600-screen_width + y


while true:

    x_coord = pygame.mouse.get_pos()[0]
    y_coord = pygame.mouse.get_pos()[1]

    display_coord(x_coord, y_coord)
    draw_lines(x_coord, y_coord)
    draw_circle(x_coord, y_coord)

    root.fill(red)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            true = False


pygame.quit()
