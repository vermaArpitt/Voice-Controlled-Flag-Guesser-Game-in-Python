import pygame as p
import threading
import sys
from main import display_text, listen_for_voice_input

p.init()
fps = 30
clock = p.time.Clock()

def game_level(screen, score, flag, value):
    screen.fill("green")

    #Displaying the score
    display_text(screen, "Score: " + str(score), 11, 11, 55, "black")
    display_text(screen, "Score: " + str(score), 10, 10, 55, "yellow")

    #Displaying the flag
    screen.blit(flag, (250, 200))
    
    exit_game = False
    answer = None
    result = []

    voice_thread = threading.Thread(target = listen_for_voice_input, args=(result,))
    voice_thread.start()

    while not exit_game:
        for event in p.event.get():
            if event.type == p.QUIT:
                exit_game = True 
                voice_thread.join()
                p.quit()
                sys.exit()

        
        if not voice_thread.is_alive() and len(result) != 0:  # Check if the thread has finished and result is not yet processed
            # answer = listen_for_voice_input()
            answer = result.pop(0)
            print(answer)
            if answer == value:
                return score + 1

            elif answer.lower() == 'exit':
                return -2

            else:
                return score - 1

        p.display.update()
        clock.tick(fps)
