import os
import cv2
import numpy as np

# path = "F:\\untitleds\learn\data\LR_vis"         # txt标注文件的根目录
# path_img = "F:\\untitleds\learn\data\crop_LR_visible"       # jpg图片的根目录
# path3 = "F:\data\mask\LR_vis"    # 裁剪出来的掩膜保存的根目录

path = "E:\mask_cut\RoadSence/test_vis_txt"         # txt标注文件的根目录
path_img = "E:\mask_cut\RoadSence\ours"       # jpg图片的根目录
path3 = "E:\mask_cut\RoadSence/vis_cut\ours_vis"    # 裁剪出来的掩膜保存的根目录

img_total = []
txt_total = []

file = os.listdir(path)     #获得txt目录下文件名

for filename in file:
    first,last = os.path.splitext(filename)
    if last == ".txt":                      # txt的后缀名，将文件前缀名加入列表
        img_total.append(first)             # 得到所需要的图像名列表
    else:
        txt_total.append(first)

for img_ in img_total:
    if img_ in img_total:
        filename_img = img_+".jpg"          # 图片的文件名    后缀名改为自己相同的
        # print('filename_img:', filename_img)
        path1 = os.path.join(path_img,filename_img)         #连接文件根目录和文件名，得到对应文件路径
        img = cv2.imread(path1)         #读取图像

        w, h, c = img.shape         #得到图像的长宽，用来确定对应掩膜的长宽
        # print(img.shape)

        filename_txt = img_+".txt"          # txt文件名
        # print('filename_txt:', filename_txt)

        with open(os.path.join(path,filename_txt),"r+",encoding="utf-8",errors="ignore") as f:      #打开txt文件
            mask = np.zeros((w, h), dtype=np.uint8)         # 用对应长宽制造掩膜
            path_tem = os.path.join(path,filename_txt)      # 打开的txt文件路径

            if not os.path.getsize(path_tem):               # txt文件是否为空
                filename_last = img_ + ".jpg"               # mask文件名
                cv2.imwrite(os.path.join(path3, filename_last), mask)       #保存mask文件
            else:
                for line in f:      #若不为空，一次读取txt文件的行
                    aa = line.split(",")        #以 ，为分界
                    print(aa)
                    a = int(aa[2])      #
                    b = int(aa[3])      #
                    c = int(aa[0])      #
                    d = int(aa[1])      #
                    mask[a:b, c:d] = 255        # 改变YOLO框内的数值

                filename_last = img_+".jpg"    # mask文件名
                cv2.imwrite(os.path.join(path3,filename_last),mask)         #保存mask文件

    else:
        continue


