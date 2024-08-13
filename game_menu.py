import pygame as p
import threading
import game_window
from main import display_text, listen_for_voice_input

p.init()
fps = 30
clock = p.time.Clock()

def game_menu(screen):
    screen.fill("black")
    display_text(screen, "Echo Nations!", 200, 200, 70, "white")
    
    exit_game = False
    answer = None
    valid_commands = {'start', 'exit'}
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
                if answer == "start":
                    game_window.game_loop(screen)
                    break

                elif answer.lower() == 'exit':
                    exit_game = True
                    break
            
            game_menu(screen)

        p.display.update()
        clock.tick(fps)
    p.quit()