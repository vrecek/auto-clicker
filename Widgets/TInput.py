from __future__ import annotations
from random import choices
import string
from tkinter import *
from typing import Callable, TypeVar
from Widgets.ABSTRACT import CommonStyles

T = TypeVar('T')

class TInput(CommonStyles[T]):
   def __init__(
      self, 
      root: Tk, 
      w: int, 
      pad: int,  
      borderClr: str = '#303030', 
      borderSize: int = 1,
      font: tuple = ('Arial', 15),
      bg: str = 'whitesmoke',
      clr: str = '#303030',
      id: str = ''
      ) -> None:
         super().__init__(root, '', clr, font, bg)
         self.pad = pad
         self.w = w
         self.borderSize = borderSize
         self.borderClr = borderClr
         self.isFocused = False

         randomId = ''.join(choices(string.ascii_lowercase, k = 6))
         self.id = id if id else randomId



   def inputPrint(self, x: int, y: int) -> TInput:
      entry = Entry(
         self.root, 
         font = self.font,
         relief = FLAT,
         borderwidth = self.pad, 
         highlightthickness = self.borderSize,
         highlightbackground = self.borderClr, 
         highlightcolor = self.borderClr,
         name = self.id
      )

      self.widget = entry

      entry.place(x = x, y = y, width = self.w)

      return self



   def setInputValue(self, val: int | str) -> TInput:
      self._noWidgetCheck()

      self.widget.insert(INSERT, val)

      return self



   def validateInput(self, type: str, additionalFunc: Callable[[str], bool] = None) -> TInput:
      self._noWidgetCheck()


      if type != 'number' and type != 'alpha':
         raise('"type" is neither ALPHA or NUMBER')


      def validate(e: str):
         isGood = e.isnumeric() if type == 'number' else e.isalpha()

         if len(e) == 0: return True

         if not isGood: return False
            
         if additionalFunc:
            return additionalFunc(e)
         
         return True


      vcmd = (self.root.register(validate), '%P')
      self.widget.config(validate = 'key', validatecommand = vcmd)


      return self
