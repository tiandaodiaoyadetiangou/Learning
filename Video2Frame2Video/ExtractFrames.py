import cv2 as cv
import time
import os
import sys

"""
请修改路径与文件名,我做测试的视频为60FPS
生成了1w5张图片，耗时接近500秒，占空间3.5G

"""


def ExtractFrames():
    time0 = time.time()
    # 这里拆开了文件名和文件路径避免各种乱七八糟的错误
    video_name = filename
    video_path = './video/' + video_name
    image_path = './pic/lr_pic'

    if not os.path.exists(image_path):
        os.makedirs(image_path)

    if not os.path.isfile(video_path):
        print(video_path + ' 不存在')
        sys.exit(1)

    # 捕获视频帧
    cap = cv.VideoCapture(video_path)

    # 视频帧转jpg图片
    has_frame = True
    idx = 0
    while has_frame:
        has_frame, frame = cap.read()
        if has_frame:
            file_name = f'{idx:6d}.jpg'
            cv.imwrite(os.path.join(image_path, file_name), frame)
            print('正在处理：', file_name, '...')
        idx += 1
    time1 = time.time()
    time_delta = time1 - time0
    cap.release()
    print('视频分帧完成！')
    print('\n用时(秒)：', time_delta)


if __name__ == '__main__':
    filename = 'alice_lr.mp4'
    ExtractFrames()
