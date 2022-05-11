import pyautogui as pg
import time

time.sleep(3)
pg.hotkey('alt', 'tab')

for i in range(0, 50):
    pg.write('Python')
    pg.press('Enter')

pg.hotkey('alt', 'tab')
print('Done!')
