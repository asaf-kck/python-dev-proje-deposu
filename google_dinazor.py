#Where you can get the game?
#http://www.trex-game.skipser.com/
from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *

class coordinates():
    replayBtn = (959, 359)
    dinosaur = (243, 375)
    
def pressSpace():
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')

def restartGame():
    pyautogui.click(coordinates.replayBtn)

def imageGrab(): #Create the box according to your own screen resolutions, otherwise you may encounter an error.
    box = (195,372,234,403)                                  
    image = ImageGrab.grab(box)
    image = ImageOps.grayscale(image)
    arr = array(image.getcolors())
    return arr.sum()
      
def main():
    
    print("Starting Game...")                
    while True:
        if(imageGrab() != 1456):
           pressSpace()
        

main()