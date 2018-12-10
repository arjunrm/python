import cv2
import numpy

img = cv2.imread('smallgray.png', 0)
print(img)

print(img[0:2, 2:4])
print(img.shape)

for i in img:
    print(i)

for i in img.T:
    print(i)

for i in img.flat:
    print(i)

img2 = numpy.hstack((img, img))
print(img2)
print(img2.shape)

img2 = numpy.vstack((img, img))
print(img2)
print(img2.shape)

img2 = numpy.hsplit(img, 5)
print(img2)
print(img2[0])

