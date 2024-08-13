import pygame as p
import threading
from main import display_text, listen_for_voice_input
import game_level
import end_screen

p.init()
fps = 30
clock = p.time.Clock()
Flags = {}

def loadFlags(dic):
    for key in dic.keys():
        Flags[key] = p.image.load("testFlags/" + key + ".png")

def game_loop(screen):
    dic = {'in' : 'India',
           'ca' : 'Canada'}
    loadFlags(dic)

    score = 0
    game_over = False

    for key, value in dic.items():
        new_score = game_level.game_level(screen, score, Flags[key], value)
        score = new_score

    end_screen.end_screen(screen, score)
    # while not exit_game:
    #     if game_finish:
    #         end_screen.end_screen(screen, score)

    #     elif game_over:
    #         pass

    #     else:
    #         for event in p.event.get():
    #             if event.type == p.QUIT:
    #                 exit_game = True

    #         screen.fill("green")

    #         for key, value in dic.items():
    #             screen.blit(Flags[key], (130, 200))
    #             #Displaying the score
    #             display_text(screen, "Score: " + str(score), 11, 11, 55, "black")
    #             display_text(screen, "Score: " + str(score), 10, 10, 55, "yellow")
    #             p.display.update()

    #             voice_thread = threading.Thread(target = listen_for_voice_input)
    #             voice_thread.start()

    #             voice_thread.join()

    #             answer = listen_for_voice_input()
    #             print(answer)
    #             if(answer == value):
    #                 print("Correct!")
    #                 score += 1

    #             elif answer.lower() == 'exit':
    #                 exit_game = True
    #                 break

    #             else:
    #                 score -= 1

    #                 if score == 0:
    #                     game_over = True
    #                     break
        
    #     game_finish = True
    #     p.display.update()
    #     clock.tick(fps)
        
    # p.quit()
