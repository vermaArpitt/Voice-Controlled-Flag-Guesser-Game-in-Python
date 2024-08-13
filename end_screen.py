import pygame as p
import threading
from main import display_text, listen_for_voice_input

p.init()
fps = 30
clock = p.time.Clock()

def end_screen(screen, score):
    screen.fill("darkslateblue")
    display_text(screen, "Congrats!", 55, 155, 60, "black")
    display_text(screen, "Congrats!", 50, 150, 60, "white")

    #Displaying Final Score
    display_text(screen, "Score: " + str(score), 305, 205, 55, "black")
    display_text(screen, "Score: " + str(score), 300, 200, 55, "white")
    exit_game = False

    while not exit_game:
        for event in p.event.get():
            if event.type == p.QUIT:
                exit_game = True

        p.display.update()
        clock.tick(fps)
        
    p.quit()