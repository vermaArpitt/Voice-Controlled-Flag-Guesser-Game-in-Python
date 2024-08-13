import pygame as p
import threading
from main import display_text, listen_for_voice_input
import game_menu
import game_window

p.init()
fps = 30
clock = p.time.Clock()

def game_over(screen, score):
    screen.fill("orchid4")
    display_text(screen, "Game Over!", 215, 55, 60, "black")
    display_text(screen, "Game Over!", 210, 50, 60, "white")

    #Displaying Final Score
    display_text(screen, "Your Score: " + str(score) + "/195", 180, 205, 55, "black")
    display_text(screen, "Your Score: " + str(score) + "/195", 175, 200, 55, "white")

    exit_game = False
    answer = None
    valid_commands = {'return', 'retry', 'exit'}
    result = []

    voice_thread = threading.Thread(target = listen_for_voice_input, args = (result,))
    voice_thread.start()

    while not exit_game:
        for event in p.event.get():
            if event.type == p.QUIT:
                exit_game = True

        if not voice_thread.is_alive() and len(result) != 0:  # Check if the thread has finished and result is not yet processed
            # answer = listen_for_voice_input()
            answer = result.pop(0)
            print(answer)
            if answer in valid_commands:
                if answer.lower() == 'return':
                    game_menu.game_menu(screen)
                    break

                elif answer.lower() == 'retry':
                    game_window.game_loop(screen)

                elif answer.lower() == 'exit':
                    exit_game = True
                    break
            
            game_over(screen, score)

        p.display.update()
        clock.tick(fps)
        
    p.quit()