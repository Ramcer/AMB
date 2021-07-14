import numpy as np
import matplotlib.pyplot as plt
import pyautogui as pa
import cv2
import pytesseract
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
import time

"""print(pa.position())
screenshot = pa.screenshot(region=(690, 195, 140, 35))
screenshot.save("screenshot.png")
screenshot.show()"""



Datos=np.load("DatosGan.npy")
plt.style.use('ggplot')
fig = plt.figure()
line, = plt.plot(Datos[0],Datos[1],'-')
plt.title("Datos")
plt.show()



"""t1=time.time()
time.sleep(2)
t2=time.time()
print(t2-t1)"""
