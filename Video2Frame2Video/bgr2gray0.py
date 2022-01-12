import os.path
import cv2  # 坑
import cv2.cv2
import time

input_dir = './pic/'
output_dir = './pic_gray/'

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

list_imgs = os.listdir(input_dir)
time0 = time.time()

for i in range(len(list_imgs)):

    imgs_name = list_imgs[i]
    img = cv2.cv2.imread(input_dir + imgs_name)
    gray = cv2.cv2.cvtColor(img, cv2.cv2.COLOR_BGR2GRAY)
    cv2.cv2.imwrite(os.path.join(output_dir, imgs_name), gray)
    print('正在处理：', imgs_name, '...')

time1 = time.time()
time_delta = time1 - time0

print('图片灰度处理完成！')
print('\n用时(秒)：', time_delta)
