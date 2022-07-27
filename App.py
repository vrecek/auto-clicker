import re
from tkinter import Tk
from typing import Callable


from screeninfo import get_monitors

class App():
   def __init__(self, title: str, w: int, h: int, bg: str) -> None:
      self.title = title
      self.width = w
      self.height = h
      self.background = bg


   def init(self, center: bool = False) -> Tk:
      coords = ''

      if center:
         screen = get_monitors()
         SCREEN_WIDTH = screen[0].width
         SCREEN_HEIGHT = screen[0].height

         x = int((SCREEN_WIDTH - (self.width + 20)) / 2)
         y = int((SCREEN_HEIGHT - (self.width + 50)) / 2)

         coords = f'+{x}+{y}'
      
      root = Tk()
      root.title(self.title)
      root.resizable(False, False)
      root.geometry(f'{self.width}x{self.height}{coords}')
      root.config(background = self.background)

      self.root = root

      return root


   def unfocusUnclick(self, ids: list[str]) -> None:
      def func(e):
         widgetId = str(e.widget)

         isWidgetClicked = any(
            list(
               map(
                  lambda x: bool( re.search(x, widgetId) ), 
                  ids
               )
            )
         )
            
         if not isWidgetClicked:
            self.root.focus_set()


      self.root.bind('<Button-1>', func)

   
   def loop(self, loopAfter: Callable[[], None] = None) -> None:
      if loopAfter:
         self.root.after(1, loopAfter)

      self.root.mainloop()
