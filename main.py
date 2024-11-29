import time

import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
Status = True

pygame.display.set_caption("Tic_tac_Toe")

# buttons
def button(x, y, width, height, alpha = 32):
    button_surface = pygame.Surface((width, height))
    box = pygame.Surface((width, height), pygame.SRCALPHA, alpha)
    box = box.convert_alpha()
    button_rect = pygame.Rect(x, y, width, height)

    return button_surface, box, button_rect
# left side
button_surface1, box1, button_rect1 = button(30, 393, 178, 176)
button_surface2, box2, button_rect2 = button(30, 213, 178, 176)
button_surface3, box3, button_rect3 = button(30, 32, 178, 176)

# middle
button_surface4, box4, button_rect4 = button(213, 393, 176, 176)
button_surface5, box5, button_rect5 = button(213, 213, 176, 176)
button_surface6, box6, button_rect6 = button(213, 32, 176, 176)

# right side
button_surface7, box7, button_rect7 = button(394, 393, 178, 176)
button_surface8, box8, button_rect8 = button(394, 213, 178, 176)
button_surface9, box9, button_rect9 = button(394, 32, 178, 176)

# winning text
fontX = pygame.font.Font(None, 100)
textX = fontX.render("X won!", True, "yellow")
text_rectX = pygame.Rect(186, 276, 600, 600)

fontO = pygame.font.Font(None, 100)
textO = fontO.render("O won!", True, "yellow")
text_rectO = pygame.Rect(186, 276, 600, 600)

grid_value = [[], [], [],                #3 6 9
              [], [], [],                #2 5 8
              [], [], []]                #1 4 7

# draw x
def x(box, grid):
    box.fill((0, 0, 0, 0))
    pygame.draw.line(box, "blue", [46, 49], [126, 129], 4)
    pygame.draw.line(box, "blue", [46, 129], [126, 49], 4)
    grid_value[grid] = 1
# draw o
def o(box, grid):
    box.fill((0, 0, 0, 0))
    pygame.draw.circle(box, "red", (86, 89), 40, 3)
    grid_value[grid] = 2

# button hover effect
def hover(button_rect, button_surface):
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface, (127, 255, 212), (0, 0, 178, 176))
    else:
        pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 178, 176))
        pygame.draw.rect(button_surface, (255, 255, 255), (0, 0, 178, 176))
        pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 178, 176), 2)
        pygame.draw.rect(button_surface, (0, 100, 0), (0, 0, 178, 176), 2)

counter = 0

while running:
    if not Status:
        time.sleep(2)
        running = False

    # Store the button_rects, boxes, and positions in lists
    button_rects = [button_rect1, button_rect2, button_rect3, button_rect4, button_rect5, button_rect6, button_rect7,
                    button_rect8, button_rect9]
    boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]
    positions = [6, 3, 0, 7, 4, 1, 8, 5, 2]

    for event in pygame.event.get():
        # pressing X closes the program
        if event.type == pygame.QUIT:
            running = False

        # check pressing buttons
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in range(9):
                if button_rects[i].collidepoint(event.pos):
                    counter += 1  # Switches between X and O every click
                    if counter % 2 == 0:
                        o(boxes[i], positions[i])
                    else:
                        x(boxes[i], positions[i])

    screen.fill((155, 255, 155))

# grid
    # horizontal lines
    pygame.draw.line(screen, "white", start_pos=[30, 210], end_pos=[570, 210], width=4)
    pygame.draw.line(screen, "white", start_pos=[30, 390], end_pos=[570, 390], width=4)
    # vertical lines
    pygame.draw.line(screen, "white", start_pos=[210, 30], end_pos=[210, 570], width=4)
    pygame.draw.line(screen, "white", start_pos=[390, 30], end_pos=[390, 570], width=4)

    button_rects = [button_rect1, button_rect2, button_rect3, button_rect4, button_rect5, button_rect6, button_rect7,
                    button_rect8, button_rect9]
    button_surfaces = [button_surface1, button_surface2, button_surface3, button_surface4, button_surface5,
                       button_surface6, button_surface7, button_surface8, button_surface9]

    for button_rect, button_surface in zip(button_rects, button_surfaces):
        hover(button_rect, button_surface)

    button_rects = [button_rect1, button_rect2, button_rect3, button_rect4, button_rect5, button_rect6, button_rect7,
                    button_rect8, button_rect9]
    button_surfaces = [button_surface1, button_surface2, button_surface3, button_surface4, button_surface5,
                       button_surface6, button_surface7, button_surface8, button_surface9]

    for button_rect, button_surface in zip(button_rects, button_surfaces):
        screen.blit(button_surface, (button_rect.x, button_rect.y))

    boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]
    button_rects = [button_rect1, button_rect2, button_rect3, button_rect4, button_rect5, button_rect6, button_rect7,
                    button_rect8, button_rect9]

    for box, button_rect in zip(boxes, button_rects):
        screen.blit(box, (button_rect.x, button_rect.y))

#winning conditions
    win_conditions = [
        [6, 3, 0], [6, 4, 2], [0, 1, 2], [8, 5, 2], [6, 7, 8], [0, 4, 8], [3, 4, 5], [1, 7, 4]
    ]

    if any(all(grid_value[i] == 1 for i in condition) for condition in win_conditions):
        screen.blit(textX, text_rectX)
        Status = False

    elif any(all(grid_value[i] == 2 for i in condition) for condition in win_conditions):
        screen.blit(textO, text_rectO)
        Status = False

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
pygame.quit()