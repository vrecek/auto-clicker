from __future__ import annotations
from tkinter import *
from typing import TypeVar
from Widgets.ABSTRACT import CommonStyles

T = TypeVar('T')

class TLabel(CommonStyles[T]):
   def __init__(
      self, 
      root: Tk, 
      txt: str, 
      font: tuple = ('Arial', 15), 
      bg: str = 'whitesmoke',
      clr: str = 'black'
      ) -> None:

         super().__init__(root, txt, clr, font, bg)


   def labelNormalPrint(self, x: int, y: int) -> TLabel:
      label = Label(self.root, text = self.txt, font = self.font, bg = self.bg, fg = self.clr)
      label.place(x = x, y = y)

      self.widget = label

      return self


   def labelSizePrint(self, x: int, y: int, w: int, h: int = 0) -> TLabel:
      if h <= 0:
         fontSize = self.font[1]
         h = fontSize * 2

      label = Label(self.root, text = self.txt, font = self.font, bg = self.bg, fg = self.clr)
      label.place(x = x, y = y, width = w, height = h)

      self.widget = label
      
      return self

   
   def changeText(self, newTxt: str):
      self._noWidgetCheck()

      self.widget['text'] = newTxt

      pass