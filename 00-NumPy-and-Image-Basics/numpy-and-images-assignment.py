 
import numpy as np
arr = np.ones((5,5))*10
arr

# This line sets a "seed" so you get the same random numbers we do
np.random.seed(101)
# This line creates an array of random numbers
arr = np.random.randint(low=0,high=100,size=(5,5))
arr.max()
arr.min()

import matplotlib.pyplot as plt

from PIL import Image

pic = Image.open('../DATA/00-puppy.jpg')

pic
pic_arr = np.asarray(pic)
pic_arr.shape
pic_blue = pic_arr.copy()
pic_blue[:, :, 0] = 0    # Zero out contribution from red
pic_blue[:, :, 1] = 0    # Zero out contribution from green
plt.imshow(pic_blue)