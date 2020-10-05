import pygame, sys
import time

pygame.init()
screen = pygame.display.set_mode((500,300))

sentence = "What to do in this crazy world"
sentence_length = len(sentence)
sentence_words = len(sentence.split())

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0 )

font_1 = pygame.font.Font('sans.ttf', 32)
font_2 = pygame.font.Font('sans.ttf', 15)
screen.fill(white)

sentence_text = font_2.render(sentence, True, red, white)
sentencetextRect = sentence_text.get_rect()
sentencetextRect.center = (250, 75)
screen.blit(sentence_text, sentencetextRect)
pygame.display.update()

def typing(sentence):
    letter_count = 0
    text_position = 0
    wrong_count = 0
    while letter_count < sentence_length:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if letter_count == 0 and wrong_count == 0:
                    start_time = time.time()
                if event.unicode == sentence[letter_count]:
                    letter_count += 1
                    text_position -= 15
                    text = font_1.render(event.unicode,True,blue,white)
                    textRect = text.get_rect()
                    textRect.center = (0 - text_position, 150)
                    screen.blit(text, textRect)
                    pygame.display.update()

                else:
                    wrong_count += 1

    if letter_count == sentence_length:
        end_time = time.time()
        typing_time = round(end_time - start_time,2)
        wpm = round((sentence_words / (typing_time / 60)),0)
        summary = f'Typing time is {typing_time} seconds, with {wpm} Words Per Minute'
        summary_text = font_2.render(summary, True, red, white)
        summarytextRect = summary_text.get_rect()
        summarytextRect.center = (200, 200)
        screen.blit(summary_text, summarytextRect)
        pygame.display.update()

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                typing(sentence)

game_loop()
