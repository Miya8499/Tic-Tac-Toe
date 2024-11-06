import time

import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
Status = True

pygame.display.set_caption("Tic_tac_Toe")

# buttons

# left side
button_surface1 = pygame.Surface((178, 176))
box1 = pygame.Surface((178, 176), pygame.SRCALPHA, 32)
box1 = box1.convert_alpha()
button_rect1 = pygame.Rect(30, 393, 178, 176)
team1 = 0

button_surface2 = pygame.Surface((178, 176))
box2 = pygame.Surface((178, 176), pygame.SRCALPHA, 32)
box2 = box2.convert_alpha()
button_rect2 = pygame.Rect(30, 213, 178, 176)
team2 = 0

button_surface3 = pygame.Surface((178, 176))
box3 = pygame.Surface((178, 176), pygame.SRCALPHA, 32)
box3 = box3.convert_alpha()
button_rect3 = pygame.Rect(30, 32, 178, 176)
team3 = 0

# middle
button_surface4 = pygame.Surface((176, 176))
box4 = pygame.Surface((176, 176), pygame.SRCALPHA, 32)
box4 = box4.convert_alpha()
button_rect4 = pygame.Rect(213, 393, 176, 176)
team4 = 0

button_surface5 = pygame.Surface((176, 176))
box5 = pygame.Surface((176, 176), pygame.SRCALPHA, 32)
box5 = box5.convert_alpha()
button_rect5 = pygame.Rect(213, 213, 176, 176)
team5 = 0

button_surface6 = pygame.Surface((176, 176))
box6 = pygame.Surface((176, 176), pygame.SRCALPHA, 32)
box6 = box6.convert_alpha()
button_rect6 = pygame.Rect(213, 32, 176, 176)
team6 = 0

# right side
button_surface7 = pygame.Surface((178, 176))
box7 = pygame.Surface((178, 176), pygame.SRCALPHA, 32)
box7 = box7.convert_alpha()
button_rect7 = pygame.Rect(394, 393, 178, 176)
team7 = 0

button_surface8 = pygame.Surface((178, 176))
box8 = pygame.Surface((178, 176), pygame.SRCALPHA, 32)
box8 = box8.convert_alpha()
button_rect8 = pygame.Rect(394, 213, 178, 176)
team8 = 0

button_surface9 = pygame.Surface((178, 176))
box9 = pygame.Surface((178, 176), pygame.SRCALPHA, 32)
box9 = box9.convert_alpha()
button_rect9 = pygame.Rect(394, 32, 178, 176)
team9 = 0

counter = 0

# winning text
fontX = pygame.font.Font(None, 100)
textX = fontX.render("X won!", True, "yellow")
text_rectX = pygame.Rect(186, 276, 600, 600)

fontO = pygame.font.Font(None, 100)
textO = fontO.render("O won!", True, "yellow")
text_rectO = pygame.Rect(186, 276, 600, 600)

while running:

    if Status == False :
        time.sleep(5)
        running = False

    if button_rect1.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface1, (127, 255, 212), (0, 0, 178, 176))
    else:
        pygame.draw.rect(button_surface1, (0, 0, 0), (0, 0, 178, 176))
        pygame.draw.rect(button_surface1, (255, 255, 255), (0, 0, 178, 176))
        pygame.draw.rect(button_surface1, (0, 0, 0), (0, 0, 178, 176), 2)
        pygame.draw.rect(button_surface1, (0, 100, 0), (0, 0, 178, 176), 2)

    for event in pygame.event.get():
        # pressing X closes the program
        if event.type == pygame.QUIT:
            running = False
        # check pressing buttons
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            counter += 1 # switches between X and O every click
            if button_rect1.collidepoint(event.pos):
                if counter % 2 == 0:
                    pygame.draw.circle(box1, "red", (86, 89), 40, 3)
                    team1 = 2
                elif counter % 2 != 0:
                    pygame.draw.line(box1, "blue", [46, 49], [126, 129], 4)
                    pygame.draw.line(box1, "blue", [46, 129], [126, 49], 4)
                    team1 = 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect2.collidepoint(event.pos):
                if counter % 2 == 0:
                    pygame.draw.circle(box2, "red", (86, 89), 40, 3)
                    team2 = 2
                elif counter % 2 != 0:
                    pygame.draw.line(box2, "blue", [46, 49], [126, 129], 4)
                    pygame.draw.line(box2, "blue", [46, 129], [126, 49], 4)
                    team2 = 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect3.collidepoint(event.pos):
                if counter % 2 == 0:
                    pygame.draw.circle(box3, "red", (86, 89), 40, 3)
                    team3 = 2
                elif counter % 2 != 0:
                    pygame.draw.line(box3, "blue", [46, 49], [126, 129], 4)
                    pygame.draw.line(box3, "blue", [46, 129], [126, 49], 4)
                    team3 = 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect4.collidepoint(event.pos):
                if counter % 2 == 0:
                    pygame.draw.circle(box4, "red", (86, 89), 40, 3)
                    team4 = 2
                elif counter % 2 != 0:
                    pygame.draw.line(box4, "blue", [46, 49], [126, 129], 4)
                    pygame.draw.line(box4, "blue", [46, 129], [126, 49], 4)
                    team4 = 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect5.collidepoint(event.pos):
                if counter % 2 == 0:
                    pygame.draw.circle(box5, "red", (86, 89), 40, 3)
                    team5 = 2
                elif counter % 2 != 0:
                    pygame.draw.line(box5, "blue", [46, 49], [126, 129], 4)
                    pygame.draw.line(box5, "blue", [46, 129], [126, 49], 4)
                    team5 = 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect6.collidepoint(event.pos):
                if counter % 2 == 0:
                    pygame.draw.circle(box6, "red", (86, 89), 40, 3)
                    team6 = 2
                elif counter % 2 != 0:
                    pygame.draw.line(box6, "blue", [46, 49], [126, 129], 4)
                    pygame.draw.line(box6, "blue", [46, 129], [126, 49], 4)
                    team6 = 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect7.collidepoint(event.pos):
                if counter % 2 == 0:
                    pygame.draw.circle(box7, "red", (86, 89), 40, 3)
                    team7 = 2
                elif counter % 2 != 0:
                    pygame.draw.line(box7, "blue", [46, 49], [126, 129], 4)
                    pygame.draw.line(box7, "blue", [46, 129], [126, 49], 4)
                    team7 = 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect8.collidepoint(event.pos):
                if counter % 2 == 0:
                    pygame.draw.circle(box8, "red", (86, 89), 40, 3)
                    team8 = 2
                elif counter % 2 != 0:
                    pygame.draw.line(box8, "blue", [46, 49], [126, 129], 4)
                    pygame.draw.line(box8, "blue", [46, 129], [126, 49], 4)
                    team8 = 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect9.collidepoint(event.pos):
                if counter % 2 == 0:
                    pygame.draw.circle(box9, "red", (86, 89), 40, 3)
                    team9 = 2
                elif counter % 2 != 0:
                    pygame.draw.line(box9, "blue", [46, 49], [126, 129], 4)
                    pygame.draw.line(box9, "blue", [46, 129], [126, 49], 4)
                    team9 = 1

    screen.fill((155, 255, 155))

# grid
    # horizontal lines
    pygame.draw.line(screen, "white", start_pos=[30, 210], end_pos=[570, 210], width=4)
    pygame.draw.line(screen, "white", start_pos=[30, 390], end_pos=[570, 390], width=4)
    # vertical lines
    pygame.draw.line(screen, "white", start_pos=[210, 30], end_pos=[210, 570], width=4)
    pygame.draw.line(screen, "white", start_pos=[390, 30], end_pos=[390, 570], width=4)

# button hover effect


    if button_rect2.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface2, (127, 255, 212), (0, 0, 178, 176))
    else:
        pygame.draw.rect(button_surface2, (0, 0, 0), (0, 0, 178, 176))
        pygame.draw.rect(button_surface2, (255, 255, 255), (0, 0, 178, 176))
        pygame.draw.rect(button_surface2, (0, 0, 0), (0, 0, 178, 176), 2)
        pygame.draw.rect(button_surface2, (0, 100, 0), (0, 0, 178, 176), 2)

    if button_rect3.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface3, (127, 255, 212), (0, 0, 178, 176))
    else:
        pygame.draw.rect(button_surface3, (0, 0, 0), (0, 0, 178, 176))
        pygame.draw.rect(button_surface3, (255, 255, 255), (0, 0, 178, 176))
        pygame.draw.rect(button_surface3, (0, 0, 0), (0, 0, 178, 176), 2)
        pygame.draw.rect(button_surface3, (0, 100, 0), (0, 0, 178, 176), 2)

    if button_rect4.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface4, (127, 255, 212), (0, 0, 176, 176))
    else:
        pygame.draw.rect(button_surface4, (0, 0, 0), (0, 0, 176, 176))
        pygame.draw.rect(button_surface4, (255, 255, 255), (0, 0, 176, 176))
        pygame.draw.rect(button_surface4, (0, 0, 0), (0, 0, 176, 176), 2)
        pygame.draw.rect(button_surface4, (0, 100, 0), (0, 0, 176, 176), 2)

    if button_rect5.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface5, (127, 255, 212), (0, 0, 176, 176))
    else:
        pygame.draw.rect(button_surface5, (0, 0, 0), (0, 0, 176, 176))
        pygame.draw.rect(button_surface5, (255, 255, 255), (0, 0, 176, 176))
        pygame.draw.rect(button_surface5, (0, 0, 0), (0, 0, 176, 176), 2)
        pygame.draw.rect(button_surface5, (0, 100, 0), (0, 0, 176, 176), 2)

    if button_rect6.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface6, (127, 255, 212), (0, 0, 176, 176))
    else:
        pygame.draw.rect(button_surface6, (0, 0, 0), (0, 0, 176, 176))
        pygame.draw.rect(button_surface6, (255, 255, 255), (0, 0, 176, 176))
        pygame.draw.rect(button_surface6, (0, 0, 0), (0, 0, 176, 176), 2)
        pygame.draw.rect(button_surface6, (0, 100, 0), (0, 0, 176, 176), 2)

    if button_rect7.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface7, (127, 255, 212), (0, 0, 178, 176))
    else:
        pygame.draw.rect(button_surface7, (0, 0, 0), (0, 0, 178, 176))
        pygame.draw.rect(button_surface7, (255, 255, 255), (0, 0, 178, 176))
        pygame.draw.rect(button_surface7, (0, 0, 0), (0, 0, 178, 176), 2)
        pygame.draw.rect(button_surface7, (0, 100, 0), (0, 0, 178, 176), 2)

    if button_rect8.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface8, (127, 255, 212), (0, 0, 178, 176))
    else:
        pygame.draw.rect(button_surface8, (0, 0, 0), (0, 0, 178, 176))
        pygame.draw.rect(button_surface8, (255, 255, 255), (0, 0, 178, 176))
        pygame.draw.rect(button_surface8, (0, 0, 0), (0, 0, 178, 176), 2)
        pygame.draw.rect(button_surface8, (0, 100, 0), (0, 0, 178, 176), 2)

    if button_rect9.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface9, (127, 255, 212), (0, 0, 178, 176))
    else:
        pygame.draw.rect(button_surface9, (0, 0, 0), (0, 0, 178, 176))
        pygame.draw.rect(button_surface9, (255, 255, 255), (0, 0, 178, 176))
        pygame.draw.rect(button_surface9, (0, 0, 0), (0, 0, 178, 176), 2)
        pygame.draw.rect(button_surface9, (0, 100, 0), (0, 0, 178, 176), 2)

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
    if all([team1 == 1, team2 == 1, team3 == 1]) or all([team2 == 1, team5 == 1, team8 == 1]) or all([team3 == 1, team6 == 1, team9 == 1]) or all(
            [team7 == 1, team8 == 1, team9 == 1]) or all([team1 == 1, team4 == 1, team7 == 1]) or all(
            [team1 == 1, team5 == 1, team9 == 1]) or all([team3 == 1, team5 == 1, team7 == 1]):
        screen.blit(textX, text_rectX)
        Status = False


    elif all([team1 == 2, team2 == 2, team3 == 2]) or all([team2 == 2, team5 == 2, team8 == 2]) or all([team3 == 2, team6 == 2, team9 == 2]) or all(
            [team7 == 2, team8 == 2, team9 == 2]) or all([team1 == 2, team4 == 2, team7 == 2]) or all(
            [team1 == 2, team5 == 2, team9 == 2]) or all([team3 == 2, team5 == 2, team7 == 2]):
        screen.blit(textO, text_rectO)
        Status = False

    pygame.display.flip()

    clock.tick(60)

    pygame.display.update()

pygame.quit()

