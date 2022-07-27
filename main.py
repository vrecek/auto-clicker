from tkinter import *
from App import App
from Clicker import Clicker
from Widgets.TButton import TButton
from Widgets.TInput import TInput
from Widgets.TLabel import TLabel


BACKGROUND_COLOR= '#e4ede6'
WIDTH = 400
HEIGHT = 500


app = App('Auto clicker', WIDTH, HEIGHT, BACKGROUND_COLOR)
root = app.init(True)
app.unfocusUnclick(['input'])


# # # # # # # # # # # # # # # # # # # # # # # WIDGETS # # # # # # # # # # # # # # # # # # # # # # # # # #

titleLabel = TLabel[Label](root, 'AUTO CLICKER', ('Arial', 18, 'bold'), 'royalblue', 'whitesmoke')

cpsLabel = TLabel[Label](root, 'Clicks per second (min: 1, max: 200)', ('Helvetica', 10, 'bold'), BACKGROUND_COLOR, '#050505')
cpsInput = TInput[Entry](root, 235, 5, font = ('Helvetica', 9, 'bold'), borderSize = 2, id = 'input-cps')

keyInput = TInput[Entry](root, 235, 5, font = ('Helvetica', 9, 'bold'), borderSize = 2, id = 'input-key')
keyLabel = TLabel[Label](root, 'Key activate (default: o)', ('Helvetica', 10, 'bold'), BACKGROUND_COLOR, '#050505')

clicksLabel = TLabel[Label](root, 'TOTAL CLICKS: 0', ('Calibri', 10, 'bold'), BACKGROUND_COLOR)

startBtn = TButton[Button](root, int(WIDTH / 2), 60, 'START', color = '#ffffff', bg = 'royalblue', borderWidth = 0)
infoLabel = TLabel[Label](root, '*You must toggle the button every change!', ('Arial', 8, 'bold'), BACKGROUND_COLOR, 'red')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 


# # # # # # # # # # # # # # # # # # # # # # WIDGET FUNCS # # # # # # # # # # # # # # # # # # # # # # # # #

startToggled = False
def startOnclick() -> None:
   global startToggled

   startToggled = not startToggled

   cps = cpsInput.returnWidget().get()
   key = keyInput.returnWidget().get() 
   btn = startBtn.returnWidget()

   if startToggled:
      clicker.hotkey(key, lambda: clicker.swapActive())
      clicker.setCPS(cps)
      btn.config(background = 'crimson')
      btn.config(text = 'STOP')

      return

   clicker.clearHotkeys()
   btn.config(background = 'royalblue')
   btn.config(text = 'START')


def hotkeyOnlyOneChar(val: str) -> bool:
   if len(val) > 1: return False

   return True

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# # # # # # # # # # # # # # # # # # # # # PLACE WIDGETS # # # # # # # # # # # # # # # # # # # # # # # # #

titleLabel.labelSizePrint(0, 0, WIDTH, 50)

cpsLabel.labelNormalPrint(5, 80)
cpsInput.inputPrint(5, 105).validateInput('number').setInputValue(1)

keyLabel.labelNormalPrint(5, 150)
keyInput.inputPrint(5, 175).validateInput('alpha', hotkeyOnlyOneChar).setInputValue('o')

clicksLabel.labelNormalPrint(5, 220)

infoLabel.labelNormalPrint(5, 275)
startBtn.buttonPrint(WIDTH / 4, HEIGHT - 80).setOnclick(startOnclick)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# # # # # # # # # # # # # # # # # # # # # CLICKER # # # # # # # # # # # # # # # # # # # # # # # # # # # #

clicker = Clicker(maxCPS = 200)

def clickerLoop():
   global startToggled

   if startToggled and clicker.isActive():
      clicker.click()
      clicksLabel.changeText(f'TOTAL CLICKS: { clicker.getClicks() }')

   root.after(1, clickerLoop)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 



app.loop(clickerLoop)