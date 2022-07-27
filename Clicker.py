from typing import Callable
import keyboard as kb
import pyautogui as pg

class Clicker():  
   def __init__(self, maxCPS: int = 200) -> None:
      self._active = False
      self._pause = 1
      self._clicks = 0
      self.maxCps = maxCPS

      pg.PAUSE = 1


   def clearHotkeys(self) -> None:
      if kb._hotkeys:
         kb.unhook_all_hotkeys()


   def setCPS(self, num: str | int) -> None:
      isInt = type(num) is int

      if not isInt:
         try: 
            num = int(num)  

            if num > self.maxCps:
               num = self.maxCps
         except: num = 1

      cps = num / num ** 2

      self._pause = cps
      pg.PAUSE = cps


   def hotkey(self, key: str, func: Callable[[], None]) -> None:
      self.clearHotkeys()

      if not key:
         key = 'o'

      kb.add_hotkey(key, func)
      

   def swapActive(self) -> None:
      self._active = not self._active


   def click(self) -> None:
      self._clicks += 1
      pg.click()


   def isActive(self) -> bool:
      return self._active


   def getClicks(self) -> int:
      return self._clicks