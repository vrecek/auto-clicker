from tkinter import Tk
from typing import Generic, TypeVar

T = TypeVar('T')

class CommonStyles(Generic[T]):
   def __init__(self, root: Tk, text: str, color: str = '#303030', font: tuple = ('Arial', 14), bg: str = 'whitesmoke') -> None:
      self.root: Tk = root
      self.txt: str = text
      self.clr: str = color
      self.font: tuple = font
      self.bg: str = bg
      self.widget: T = None

   
   def _noWidgetCheck(self) -> None:
      if not self.widget:
         raise('No widget was created. Create your widget first.')


   def returnWidget(self) -> T:
      self._noWidgetCheck()

      return self.widget

