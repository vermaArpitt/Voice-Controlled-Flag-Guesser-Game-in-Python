import pygame as p
import voiceInput
import game_menu

p.init()
WIDTH = 700
HEIGHT = 512
fps = 30
clock = p.time.Clock()

def listen_for_voice_input():
    return voiceInput.voiceInput()

def display_text(screen, text, x, y, size, color):
    font = p.font.SysFont(None, size)
    img = font.render(text, True, color)
    screen.blit(img, [x, y])

def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    p.display.set_caption("Echo Nations!")

    game_menu.game_menu(screen)

if __name__ == '__main__':
    main()