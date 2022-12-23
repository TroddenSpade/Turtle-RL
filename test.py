from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = Image.open('Unknown.jpeg')
x = np.array(img)
x[220 < x] = 255

result = Image.fromarray(x)
result.save('out.png')

plt.imshow(x)
plt.show()