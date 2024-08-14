import pygame as p
import threading
import sys
import game_window
from main import display_text, listen_for_voice_input

p.init()
fps = 30
clock = p.time.Clock()

def game_menu(screen):
    left_flag = p.image.load("assets/left-flag.png")
    right_flag = p.image.load("assets/right-flag.png")
    screen.fill("darkcyan")

    #Displaying Game Title
    screen.blit(left_flag, [85, 70])
    screen.blit(right_flag, [512, 70])
    display_text(screen, "Echo Nations!", 175, 105, 70, "black")
    display_text(screen, "Echo Nations!", 170, 100, 70, "white")

    #Displaying commands
    display_text(screen, 'Speak ("play") to Play Game', 90, 245, 55, "black")
    display_text(screen, 'Speak ("play") to Play Game', 85, 240, 55, "white")

    display_text(screen, 'Speak ("exit") to Exit Game', 33, 403, 30, "black")
    display_text(screen, 'Speak ("exit") to Exit Game', 30, 400, 30, "white")
    
    exit_game = False
    answer = None
    valid_commands = {'play', 'exit'}
    result = []

    voice_thread = threading.Thread(target = listen_for_voice_input, args = (result,))
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
            if answer in valid_commands:
                if answer.lower() == 'play':
                    game_window.game_loop(screen)
                    break

                elif answer.lower() == 'exit':
                    exit_game = True
                    break
            
            game_menu(screen)

        p.display.update()
        clock.tick(fps)
    p.quit()