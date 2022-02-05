import os
import cv2
import time


def Resize(base_dir, save_dir, width, high):
    filelist = os.listdir(base_dir)
    print('\n一共{}张图片待处理'.format(len(filelist)))
    if not os.path.exists(base_dir):
        print('输入路径不存在或错误!')
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    for filename in filelist:
        img = cv2.imread(base_dir + filename)
        img1 = cv2.resize(img, (width, high), interpolation=cv2.INTER_CUBIC)

        cv2.imwrite(save_dir + filename, img1)
        print('已经将' + filename + '处理完了......')
    print('*****处理完毕!*****')


if __name__ == '__main__':
    base_dir = './pic/lr_pic/'
    save_dir = './pic/lr_resize/'
    width = 1920
    high = 1080
    Resize(base_dir, save_dir, width, high)
