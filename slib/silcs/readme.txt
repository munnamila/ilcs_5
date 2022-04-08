

keypoints_plot(src, src_img = None, plot_in_pic = False, show_accuracy = False)

描述：将Openpose输出的(1, 25, 3)的矩阵输入，得到25个身体坐标点的可视化图。


parameter:
src: 输入的(1, 25, 3)的矩阵
src_img: 原始图片
plot_in_pic：是否显示原始图片

example：
import numpy as np
import silcs

data = np.load('~.npz')
keypoints_plot(data['pose'][2000])