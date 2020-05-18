#images and numpy
import numpy as np

import matplotlib.pyplot as plt
#matplotlib inline

from PIL import Image
pic = Image.open('../DATA/00-puppy.jpg')
pic
type(pic)
pic_arr = np.asarray(pic)
pic_arr.shape
plt.imshow(pic_arr)

pic_red = pic_arr.copy()
plt.imshow(pic_red[:,:,0],cmap='gray')
plt.imshow(pic_red[:,:,1],cmap='gray')
plt.imshow(pic_red[:,:,2],cmap='gray')
pic_red[:, :, 1] = 0    # Zero out contribution from green
pic_red[:, :, 2] = 0    # Zero out contribution from blue
plt.imshow(pic_red)
plt.imshow(pic_red[:,:,0],cmap='gray')

