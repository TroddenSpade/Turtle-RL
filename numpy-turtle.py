import numpy as np
from skimage.io import imsave

from numpy_turtle import Turtle


def main():
    """Create the Sierpinski triangle
    https://en.wikipedia.org/wiki/Sierpinski_triangle
    """

    angle = 2 * np.pi / 3
    cols = 512
    rows = int(np.ceil(cols * np.sin(angle / 2)))

    a = np.zeros((rows, cols, 4))

    t = Turtle(a)
    t.position = rows, 0
    t.rotate(np.pi / 2)
    t.circle(60)

    

    imsave('images/sierpinski_triangle.png', a)


if __name__ == '__main__':
    main()