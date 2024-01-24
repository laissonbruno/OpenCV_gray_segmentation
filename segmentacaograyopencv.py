# -*- coding: utf-8 -*-
"""segmentacaoGrayOpenCV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12oREIOHE2zqRiFy_QPQv3p5uP6zuVzs7
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

import requests
url = "https://images.pexels.com/photos/951007/pexels-photo-951007.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
r = requests.get(url)

with open ('test.jpg', 'wb') as f:
  f.write(r.content)

img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(gray, (3,3), 0)

sobelx = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobelxy = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

plt.figure(figsize=(18,19))
plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title('original')
plt.axis('off')

plt.subplot(222)
plt.imshow(sobelxy, cmap='gray')
plt.title('Sobel X Y')
plt.axis('off')

plt.subplot(223)
plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X')
plt.axis('off')

plt.subplot(224)
plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y')
plt.axis('off')