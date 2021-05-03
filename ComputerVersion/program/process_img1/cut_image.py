import sys

sys.path.append(r'./imgStrengthen/')
import Image_process as ImgP
import cv2

# 调用摄像头摄像头
cap = cv2.VideoCapture(0)
c = 0
while (True):  # 按帧提取图像
    # 获取摄像头拍摄到的画面，提取每一帧
    rval, img = cap.read()  # 25帧/秒
    timeF = 375  # 视频帧计数间隔频率15s
    if (c % timeF == 0):  # 每隔timeF帧进行存储操作
        cv2.imwrite('./../../data/img1/' + str(c) + 'origin.jpg', img)  # 存储原图像

        img = ImgP.strength(img)  # 调用图像处理的函数

        cv2.imwrite('./../../data/img1/' + str(c) + '.jpg', img)  # 存储为图像
    c = c + 1
    print(c)
    # 实时展示效果画面，输出每一帧
    cv2.imshow('frame', img)
    # 每5毫秒监听一次键盘动作
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
# 最后，关闭所有窗口
cap.release()
cv2.destroyAllWindows()
