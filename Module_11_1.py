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

