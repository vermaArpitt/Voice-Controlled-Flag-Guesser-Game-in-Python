import pygame as p
import voiceInput

Images = {}

def loadImages(dic):
    for key in dic.keys():
        Images[key] = p.image.load("testFlags/" + key + ".png")

def main():
    dic = {'in' : 'India',
           'ca' : 'Canada'}
    loadImages(dic)

    p.init()
    screen = p.display.set_mode((512, 512))

    for key, value in dic.items():
        screen.blit(Images[key], (130, 0))
        p.display.update()
        answer = voiceInput.voiceInput()
        print(f"Your answer: {answer}")
        if(answer == value):
            print("Correct!")
            
    p.quit()


if __name__ == '__main__':
    main()