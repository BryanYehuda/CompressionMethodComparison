from math import log10, sqrt
import cv2
import numpy as np
  
def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

def SNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):
        return 100
    snr = 20 * log10(np.mean(original) / sqrt(mse))
    return snr
  
def main():
    original = cv2.imread("raw.png")
    compressed = cv2.imread("lossless.png", 1)
    mse = np.mean((original - compressed) ** 2)
    snr = SNR(original, compressed)
    psnr = PSNR(original, compressed)
    print(f"MSE value is {mse}")
    print(f"SNR value is {snr} dB")
    print(f"PSNR value is {psnr} dB")
       
if __name__ == "__main__":
    main()