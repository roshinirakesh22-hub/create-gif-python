import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ['cat-pic(1).jpeg', 'cat-pic(2).jpeg']
images = []

# Target size (use the first image size)
first_img = Image.open(filenames[0])
target_size = first_img.size  # (width, height)

for filename in filenames:
    img = Image.open(filename)
    img = img.resize(target_size)
    images.append(np.array(img))

# Create GIF
iio.imwrite(
    'cat.gif',
    images,
    duration=1.0,
    loop=0
)

