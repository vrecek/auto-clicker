from __future__ import annotations
from tkinter import *
from typing import Callable
from Widgets.ABSTRACT import CommonStyles

class TButton(CommonStyles[Button]):
   def __init__(
      self,
      root: Tk,
      w: int,
      h: int,
      txt: str,
      font: tuple = ("Helvetica", 14),
      bg: str = 'whitesmoke',
      borderClr: str = '#303030',
      borderWidth: int = 1,
      color: str = '#303030'
      ) -> None:

         super().__init__(root, txt, color, font, bg)
         self.width = w
         self.height = h
         self.borderClr = borderClr
         self.borderWidth = borderWidth


   def buttonPrint(self, x: int, y: int) -> TButton:
      f = Frame(self.root, highlightbackground = self.borderClr, highlightthickness = self.borderWidth)
      
      btn = Button(
         f, 
         relief = FLAT,
         text = self.txt, 
         fg = self.clr, 
         bg = self.bg, 
         font = self.font, 
         cursor = 'hand2',
         width = self.width,
         height = self.height
      )

      btn.pack()
      f.pack()

      self.widget = btn
      self.frame = f

      f.place(x = x, y = y, width = self.width, height = self.height)

      return self


   def setOnclick(self, clickFunc: Callable[[], None]) -> TButton:
      self._noWidgetCheck()

      self.widget.config(command = clickFunc)

      return self


   def returnFrame(self) -> Frame:
      self._noButtonCheck()

      return self.frame
