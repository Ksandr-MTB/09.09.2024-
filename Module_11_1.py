from PIL import Image

a = Image.open('obrazec_1.jpg')
print(a.format, a.size, a.mode)
a.show()
b = a.convert('L')
b.show()
b.save('obrazec_black_white.jpg')
print(b.format, b.size, b.mode)
a.save('obrazec_small.JPEG')

qq = Image.open('obrazec_small.JPEG')
qq.show()
print(qq.format, qq.size, qq.mode)
size_ = (258, 258)
qq.thumbnail(size_)
qq.save('obrazec_small_1.JPEG')

qw = Image.open('obrazec_small_1.JPEG')
qw.show()
print(qw.format, qw.size, qw.mode)
import numpy

image_filenames = ['obrazec_1.jpg', 'obrazec_black_white.jpg']
images = [Image.open(i) for i in image_filenames]
images[0].save('gif_1.gif', save_all=True, append_images=images[1:], duration=500,
               loop = 0)
qwe = open('gif_1.gif')
# qwe.show()
# print(qwe.format, qwe.size, qwe.mode)

import matplotlib.pyplot
import random

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 3, 5, 7, 9, 10, 7, 5, 3, 1]
x_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# for i in range(10):
#     x.append(random.randint(1, 10))
#     y.append(random.randint(1, 10))
fig, ax = matplotlib.pyplot.subplots()
ax.set_title('Какой-то график')
ax.set_xlabel('Кордината горизонтальная Х')
ax.set_ylabel('Кордината вертикальная У')
ax.grid()



ax.plot(x, y)
ax.plot(y_1, x_1)

print(f'{x}\n{y}')
matplotlib.pyplot.show()
