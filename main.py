import time
from PIL import ImageGrab
import pyautogui


def Jump(data):
    for i in range(350, 400):
        for j in range(650, 700):
            if data[i, j] < 100:
                pyautogui.press("up")
                return
    for i in range(300, 350):
        for j in range(610, 650):
            if data[i, j] < 100:
                pyautogui.press("down")
                return


time.sleep(2)
pyautogui.press("space")
while True:
    image = ImageGrab.grab().convert("L")
    data = image.load()
    Jump(data)

# time.sleep(2)
# image = ImageGrab.grab().convert("L")
# data = image.load()

# for i in range(300, 350):
#     for j in range(610, 650):
#         data[i, j] = 0
# image.show()
