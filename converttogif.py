import os
import imageio

png_dir = './images'
images = []
l = os.listdir(png_dir)
for file_name in sorted(os.listdir(png_dir))[::2]:

    if file_name.endswith('.png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave('./bubble.gif', images,fps=120)