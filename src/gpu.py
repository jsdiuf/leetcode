from timeit import default_timer as timer

import numpy as np
from matplotlib.pyplot import imshow, show
from numba import jit


@jit
def mandel(x, y, max_iters):
    """
      1，判断N=x+yi这个复数 的模是否大于2 是返回0
      2，如果不是则将此复数变为N=N^2+N继续测试直到满足条件返回迭代的次数
      3，达到最大迭代数 返回最大迭代数
    """
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z * z + c
        if (z.real * z.real + z.imag * z.imag) >= 4:
            return i

    return max_iters


@jit
def create_fractal(min_x, max_x, min_y, max_y, image, iters):
    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            color = mandel(real, imag, iters)
            image[y, x] = color


def main():
    image = np.zeros((2000, 2000), dtype=np.uint8)
    start = timer()
    create_fractal(-2.0, 1.0, -1.0, 1.0, image, 20)
    dt = timer() - start

    print("Mandelbrot created in %f s" % dt)
    imshow(image)
    show()


if __name__ == '__main__':
    main()
