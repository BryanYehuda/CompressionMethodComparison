import io
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from urllib.request import urlopen
import IPython

image_url='file:///D:/downloads/LossyComparison/raw.jpg'
def get_image_from_url(image_url='http://i.imgur.com/8vuLtqi.png', size=(128, 128)):
    file_descriptor = urlopen(image_url)
    image_file = io.BytesIO(file_descriptor.read())
    image = Image.open(image_file)
    img_color = image.resize(size, 1)
    img_grey = img_color.convert('L')
    img = np.array(img_grey, dtype=float)
    return img

def get_2D_dct(img):
    return fftpack.dct(fftpack.dct(img.T, norm='ortho').T, norm='ortho')

def get_2d_idct(coefficients):
    return fftpack.idct(fftpack.idct(coefficients.T, norm='ortho').T, norm='ortho')

def get_reconstructed_image(raw):
    img = raw.clip(0, 255)
    img = img.astype('uint8')
    img = Image.fromarray(img)
    return img

pixels = get_image_from_url(image_url=image_url, size=(256, 256))
dct_size = pixels.shape[0]
dct = get_2D_dct(pixels)
reconstructed_images = []

for ii in range(dct_size):
    dct_copy = dct.copy()
    dct_copy[ii:,:] = 0
    dct_copy[:,ii:] = 0
    
    r_img = get_2d_idct(dct_copy);
    reconstructed_image = get_reconstructed_image(r_img);
    reconstructed_images.append(reconstructed_image);

fig = plt.figure(figsize=(16, 16))
for ii in range(64):
    plt.subplot(8, 8, ii + 1)
    plt.imshow(reconstructed_images[ii], cmap=plt.cm.gray)
    plt.grid(False);
    plt.xticks([]);
    plt.yticks([]);
    if ii == 63:
        plt.imsave('hasilDCT.jpg', reconstructed_images[ii], cmap=plt.cm.gray);
    
plt.show();