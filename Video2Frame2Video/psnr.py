import cv2
from skimage.metrics import mean_squared_error
from skimage.metrics import peak_signal_noise_ratio
from skimage.metrics import structural_similarity
print("""
MSE 越小，则 PSNR 越大；PSNR越大，代表着图像质量越好。

    PSNR高于40dB说明图像质量极好(即非常接近原始图像)
    在30-40dB通常表示图像质量是好的(即失真可以察觉但可以接受)
    在20-30dB说明图像质量差
    低于20dB图像不可接受
""")
pre_pic = input('处理后图片的路径：')
raw_pic = input('原始高清图片路径：')

img1 = cv2.imread(pre_pic)
img2 = cv2.imread(raw_pic)

MSE = mean_squared_error(img1, img2)
PSNR = peak_signal_noise_ratio(img1, img2)
SSIM = structural_similarity(img1, img2, multichannel=True)

print('\nMSE均方误差: ', MSE)
print('PSNR峰值信噪比（dB）: ', PSNR)
print('SSIM结构相似性: ', SSIM)
