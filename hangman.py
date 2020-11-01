import math
import pygame
import random

# SET DISPLAY
pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 800, 500

# Button Variable
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 12) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + (RADIUS * 2 + GAP) * (i % 13)
    y = starty + (i // 13) * (RADIUS * 2 + GAP)
    letters.append([x, y, chr(A + i), True])

# Font
INTRO_TITLE_FONT = pygame.font.SysFont("comicsans", 40)
LETTER_FONT = pygame.font.SysFont("comicsans", 40)
WORD_FONT = pygame.font.SysFont("comicsans", 60)

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
FAINT_WHITE = (200,200,200)

# CONSTANTS
IMAGES = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    IMAGES.append(image)
WORDS = ["FUNCTION", "METHOD", "CLASS", "PRIVATE", "PUBLIC", "PROTECTED", "ATTRIBUTE", "ISA", "HASA", "VARIABLE", "CONSTANT", "TYPE"]


# game variables
word = random.choice(WORDS)
hangman_status = 0
guessed = []


    


def redraw_window(win, isStart, isEnd, hangman_status):
    if isStart and not isEnd:
        win.fill((255,255,255))
        # Draw title




        # Draw word
        display_word = ""
        for character in word:
            if character in guessed:
                display_word += character + " "
            else:
                display_word += "_ "
        text = WORD_FONT.render(display_word, 1, BLACK)
        win.blit(text, (400, 200))

        # Draw Button
        for letter in letters:
            x, y, character, visible = letter
            if visible:
                pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
                text = LETTER_FONT.render(character, 1, BLACK)
                win.blit(text, (x-text.get_width()/2, y - text.get_height()/2))

        # Drawing Hangman
        win.blit(IMAGES[hangman_status], (150, 100))
    elif not isStart: 
        win.fill((200,200,200))
        introText = INTRO_TITLE_FONT.render("Start", 1, (0,0,0))
        win.blit(introText, (WIDTH/2 - introText.get_width()/2, HEIGHT/2 - introText.get_height()/2))
    else:
        pygame.time.delay(1000)
        win.fill((200,200,200))
        introText = INTRO_TITLE_FONT.render("Thank you for playing!", 1, (0,0,0))
        win.blit(introText, (WIDTH/2 - introText.get_width()/2, HEIGHT/2 - introText.get_height()/2))
        pygame.display.update()
        pygame.time.delay(2000)

    pygame.display.update()




def main():
    global hangman_status
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hangman")
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    isStart = False
    isEnd = False
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if not isStart and event.type == pygame.MOUSEBUTTONDOWN:
                isStart = True

            if isStart and event.type == pygame.MOUSEBUTTONDOWN:
                isStart = True
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, character, visible = letter
                    if visible:
                        dist = math.sqrt((m_x-x)**2 + (m_y-y)**2)
                        if dist < RADIUS:
                            letter[3] = False
                            guessed.append(character)
                            if character not in word:
                                hangman_status += 1
        redraw_window(win, isStart, isEnd, hangman_status)

        won = True
        for character in word:
            if character not in guessed:
                won = False
                break

        if won:
            isEnd = True
            run = False

        if hangman_status > 6:
            isEnd = True
            run = False

        redraw_window(win, isStart, isEnd, hangman_status)





main()
pygame.quit()
