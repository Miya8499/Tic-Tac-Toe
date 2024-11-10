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

counter = 0

# winning text
fontX = pygame.font.Font(None, 100)
textX = fontX.render("X won!", True, "yellow")
text_rectX = pygame.Rect(186, 276, 600, 600)

fontO = pygame.font.Font(None, 100)
textO = fontO.render("O won!", True, "yellow")
text_rectO = pygame.Rect(186, 276, 600, 600)

grid_value = [[], [], [],
              [], [], [],
              [], [], []]
                #3 6 9
                #2 5 8
                #1 4 7
# draw x
def x(box, grid):
    pygame.draw.line(box, "blue", [46, 49], [126, 129], 4)
    pygame.draw.line(box, "blue", [46, 129], [126, 49], 4)
    grid_value[grid] = 1
# draw o
def o(box, grid):
    pygame.draw.circle(box, "red", (86, 89), 40, 3)
    grid_value[grid] = 2

while running:
    if not Status:
        time.sleep(2)
        running = False

    for event in pygame.event.get():
        # pressing X closes the program
        if event.type == pygame.QUIT:
            running = False
        # check pressing buttons
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            counter += 1 # switches between X and O every click
            if button_rect1.collidepoint(event.pos):
                if counter % 2 == 0:
                    o(box1, 6)
                elif counter % 2 != 0:
                    x(box1, 6)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect2.collidepoint(event.pos):
                if counter % 2 == 0:
                    o(box2, 3)
                elif counter % 2 != 0:
                    x(box2, 3)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect3.collidepoint(event.pos):
                if counter % 2 == 0:
                    o(box3, 0)
                elif counter % 2 != 0:
                    x(box3, 0)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect4.collidepoint(event.pos):
                if counter % 2 == 0:
                    o(box4, 7)
                elif counter % 2 != 0:
                    x(box4, 7)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect5.collidepoint(event.pos):
                if counter % 2 == 0:
                    o(box5, 4)
                elif counter % 2 != 0:
                    x(box5, 4)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect6.collidepoint(event.pos):
                if counter % 2 == 0:
                    o(box6, 1)
                elif counter % 2 != 0:
                    x(box6, 1)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect7.collidepoint(event.pos):
                if counter % 2 == 0:
                    o(box7, 8)
                elif counter % 2 != 0:
                    x(box7, 8)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect8.collidepoint(event.pos):
                if counter % 2 == 0:
                    o(box8, 5)
                elif counter % 2 != 0:
                    x(box8, 5)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect9.collidepoint(event.pos):
                if counter % 2 == 0:
                    o(box9, 2)
                elif counter % 2 != 0:
                    x(box9, 2)

    screen.fill((155, 255, 155))

# grid
    # horizontal lines
    pygame.draw.line(screen, "white", start_pos=[30, 210], end_pos=[570, 210], width=4)
    pygame.draw.line(screen, "white", start_pos=[30, 390], end_pos=[570, 390], width=4)
    # vertical lines
    pygame.draw.line(screen, "white", start_pos=[210, 30], end_pos=[210, 570], width=4)
    pygame.draw.line(screen, "white", start_pos=[390, 30], end_pos=[390, 570], width=4)

# button hover effect
    def hover(button_rect, button_surface):
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface, (127, 255, 212), (0, 0, 178, 176))
        else:
            pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 178, 176))
            pygame.draw.rect(button_surface, (255, 255, 255), (0, 0, 178, 176))
            pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 178, 176), 2)
            pygame.draw.rect(button_surface, (0, 100, 0), (0, 0, 178, 176), 2)

    hover(button_rect1, button_surface1)
    hover(button_rect2, button_surface2)
    hover(button_rect3, button_surface3)
    hover(button_rect4, button_surface4)
    hover(button_rect5, button_surface5)
    hover(button_rect6, button_surface6)
    hover(button_rect7, button_surface7)
    hover(button_rect8, button_surface8)
    hover(button_rect9, button_surface9)

    screen.blit(button_surface1, (button_rect1.x, button_rect1.y))
    screen.blit(button_surface2, (button_rect2.x, button_rect2.y))
    screen.blit(button_surface3, (button_rect3.x, button_rect3.y))
    screen.blit(button_surface4, (button_rect4.x, button_rect4.y))
    screen.blit(button_surface5, (button_rect5.x, button_rect5.y))
    screen.blit(button_surface6, (button_rect6.x, button_rect6.y))
    screen.blit(button_surface7, (button_rect7.x, button_rect7.y))
    screen.blit(button_surface8, (button_rect8.x, button_rect8.y))
    screen.blit(button_surface9, (button_rect9.x, button_rect9.y))

    screen.blit(box1, (button_rect1.x, button_rect1.y))
    screen.blit(box2, (button_rect2.x, button_rect2.y))
    screen.blit(box3, (button_rect3.x, button_rect3.y))
    screen.blit(box4, (button_rect4.x, button_rect4.y))
    screen.blit(box5, (button_rect5.x, button_rect5.y))
    screen.blit(box6, (button_rect6.x, button_rect6.y))
    screen.blit(box7, (button_rect7.x, button_rect7.y))
    screen.blit(box8, (button_rect8.x, button_rect8.y))
    screen.blit(box9, (button_rect9.x, button_rect9.y))

#winning conditions
    if all([grid_value[6] == 1, grid_value[3] == 1, grid_value[0] == 1]) or all([grid_value[6] == 1, grid_value[4] == 1, grid_value[2] == 1]) or all(
            [grid_value[0] == 1, grid_value[1] == 1, grid_value[2] == 1]) or all([grid_value[8] == 1, grid_value[5] == 1, grid_value[2] == 1]) or all(
            [grid_value[6] == 1, grid_value[7] == 1, grid_value[8] == 1]) or all([grid_value[0] == 1, grid_value[4] == 1, grid_value[8] == 1]) or all(
            [grid_value[3] == 1, grid_value[4] == 1, grid_value[5] == 1]) or all([grid_value[1] == 1, grid_value[7] == 1, grid_value[4] == 1]):
        screen.blit(textX, text_rectX)
        Status = False

    elif all([grid_value[6] == 2, grid_value[6] == 2, grid_value[0] == 2]) or all([grid_value[6] == 2, grid_value[4] == 2, grid_value[2] == 2]) or all(
            [grid_value[0] == 2, grid_value[1] == 2, grid_value[2] == 2]) or all([grid_value[8] == 2, grid_value[5] == 2, grid_value[2] == 2]) or all(
            [grid_value[6] == 2, grid_value[7] == 2, grid_value[8] == 2]) or all([grid_value[0] == 2, grid_value[4] == 2, grid_value[8] == 2]) or all(
            [grid_value[3] == 2, grid_value[4] == 2, grid_value[5] == 2]) or all([grid_value[1] == 2, grid_value[7] == 2, grid_value[4] == 2]):
        screen.blit(textO, text_rectO)
        Status = False

    pygame.display.flip()

    clock.tick(60)

    pygame.display.update()

pygame.quit()

