import cv2
from skimage.metrics import peak_signal_noise_ratio as compare_psnr
from skimage.metrics import structural_similarity as compare_ssim

img1 = cv2.imread(r'./pic/hr_pic/   100.jpg')
img2 = cv2.imread(r'./pic/lr_pic/   100.jpg')


def PSNR_SSIM(hr, pre):
    psnr = compare_psnr(hr, pre)
    ssim = compare_ssim(hr, pre, multichannel=True)  # 对于多通道图像(RGB、HSV等)关键词multichannel要设置为True
    print('原图和输出图像比较后，PSNR：{}，SSIM：{}'.format(psnr, ssim))


PSNR_SSIM(img1, img2)
