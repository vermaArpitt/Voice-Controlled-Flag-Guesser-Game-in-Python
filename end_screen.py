import pygame as p
import threading
from main import display_text, listen_for_voice_input
import game_menu

p.init()
fps = 30
clock = p.time.Clock()

def end_screen(screen, score):
    screen.fill("darkslateblue")
    display_text(screen, "CONGRATS!", 215, 35, 60, "black")
    display_text(screen, "CONGRATS!", 210, 30, 60, "white")

    display_text(screen, "Result", 275, 135, 50, "black")
    display_text(screen, "Result", 270, 130, 50, "white")

    #Displaying Final Score
    display_text(screen, "Score: " + str(score) + "/195", 225, 225, 55, "black")
    display_text(screen, "Score: " + str(score) + "/195", 220, 220, 55, "white")

    exit_game = False
    answer = None
    valid_commands = {'return', 'exit'}
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
                if answer.lower() == "return":
                    game_menu.game_menu(screen)
                    break

                elif answer.lower() == 'exit':
                    exit_game = True
                    break
            
            end_screen(screen, score)

        p.display.update()
        clock.tick(fps)
        
    p.quit()