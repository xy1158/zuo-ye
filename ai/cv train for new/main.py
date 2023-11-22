import cv2
import numpy as np

data = np.array([1, 5, 8, 7])
print(data)  # 打印出来虽然是列表但是他的类型不是列表，而是numpy.ndarray
print(type(data))

# 想要知道数据的大小
print(len(data))
print(data.shape[0])  # 但是这个返回的值却是以numpy.ndarray的形式输出的

# 上面这种方法shape的好处在于多为列表的应用
data2 = np.array([[1, 2, 5], [3, 5, 7], [4, 7, 9]])
# 如果打印data2，我们会得到这个二维列表（矩阵）的行列数
print(data2.shape)

print(np.sum(data2, axis=0))  # axis是轴的意思，行为1，列为0

# 用numpy求均值
print(np.mean(data2[0]))

# 切片
print(data2[1:3, 1:3])

img = cv2.imread("R-C.jpg")
# cv2.imshow("image",img)
# cv2.waitKey()

print(img.shape)

center_x_img = int(img.shape[0]/2)
center_y_img = int(img.shape[1]/2)
print(center_x_img)

img[center_x_img-100:center_x_img+100, center_y_img-100:center_y_img+100, 0:3] = [0, 0, 0]

cv2.imshow("img", img)
cv2.waitKey()