import pygame as p
import voiceInput
import game_menu

p.init()
WIDTH = 700
HEIGHT = 512
fps = 30
clock = p.time.Clock()

Images = {}

def listen_for_voice_input():
    return voiceInput.voiceInput()

def loadImages(dic):
    for key in dic.keys():
        Images[key] = p.image.load("testFlags/" + key + ".png")

def display_text(screen, text, x, y, size, color):
    font = p.font.SysFont(None, size)
    img = font.render(text, True, color)
    screen.blit(img, [x, y])

def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    p.display.set_caption("Echo Nations!")

    game_menu.game_menu(screen)

    # dic = {'in' : 'India',
    #        'ca' : 'Canada'}
    # loadImages(dic)

    # for key, value in dic.items():
    #     screen.blit(Images[key], (130, 0))
    #     p.display.update()
    #     answer = voiceInput.voiceInput()
    #     print(f"Your answer: {answer}")
    #     if(answer == value):
    #         print("Correct!")

if __name__ == '__main__':
    main()