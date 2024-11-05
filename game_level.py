import pygame as p
import threading
import sys
import time
from main import display_text, listen_for_voice_input

p.init()
fps = 30
clock = p.time.Clock()

def game_level(screen, score, lives, flag, value):
    life = p.image.load("assets/life-icon.png")
    screen.fill("turquoise4")

    #Displaying the score
    display_text(screen, "Score: " + str(score), 13, 13, 55, "black")
    display_text(screen, "Score: " + str(score), 10, 10, 55, "yellow")

    #Displaying Lives
    if lives > 0:
        screen.blit(life, [465, 10])
    if lives > 1:
        screen.blit(life, [535, 10])
    if lives > 2:
        screen.blit(life, [605, 10])

    #Displaying the flag
    screen.blit(flag, (300, 200))
    
    #Displaying prompt
    display_text(screen, "Your Answer: ", 14, 351, 55, "black")
    display_text(screen, "Your Answer: ", 10, 347, 55, "white")

    exit_game = False
    answer = None
    result = []
    answer_display_time = None

    voice_thread = threading.Thread(target = listen_for_voice_input, args=(result,))
    voice_thread.start()

    while not exit_game:
        for event in p.event.get():
            if event.type == p.QUIT:
                exit_game = True 
                voice_thread.join()
                p.quit()
                sys.exit()

        if not voice_thread.is_alive() and len(result) != 0:  # Checking if the thread has finished
            answer = result.pop(0)
            answer_display_time = time.time()  # Setting the current time for displaying the answer

            # Displaying the answer text 
            display_text(screen, answer, 275, 347, 55, "white")
            print(answer)

        if answer_display_time and (time.time() - answer_display_time) > 3: #Added 3 second delay for displaying answer  
            if answer.lower() == value:
                return score + 1, lives
            elif answer.lower() == 'exit':
                return -2, -2
            else:
                return score, lives - 1

        p.display.update()
        clock.tick(fps)
