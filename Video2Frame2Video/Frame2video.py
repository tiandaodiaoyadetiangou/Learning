import os
import cv2
import time

# pic = './pic/lr_pic/0.jpg'
# imgr = cv2.imread(pic)
time0 = time.time()
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
path = './pic/lr_pic/'
filelist = os.listdir(path)


def generate_video(video_path, fps):
    img0 = filelist[0]
    img1 = path + str(filelist[0])
    img2 = cv2.imread(img1)
    # size=(img2.shape[1],img2.shape[0])
    videowriter = cv2.VideoWriter(video_path, fourcc, fps, (img2.shape[1], img2.shape[0]))

    for filename in filelist:
        img = cv2.imread(path + filename)
        videowriter.write(img)
        print('已经将' + filename + '处理完了......')
    videowriter.release()
    print("完成！")
    time1 = time.time()
    time_delta = time1 - time0
    print("\n作业用时：", time_delta)


if __name__ == '__main__':
    pic_path = './pic/lr_pic'
    video_path = './video/demo.mp4'
    fps = 60
    generate_video(video_path, fps)
