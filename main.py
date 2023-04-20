# Import Libraries
from fake_image_generator import create_base_image, create_microscope_image, create_dye_image, create_dye_image_with_lines, save_image
from compress_images import convert_to_quad_tree, compress, save
from detect_cancer_slow import find_overlap_slow
from detect_cancer_fast import find_overlap_fast, extract, find_black_pixels, return_global_black_pixels, reset_index
import time
from PIL import Image
import numpy as np

# Generate fake simulated images

# Create base image
size = 1000
base_image = create_base_image((size, size))

# Create microscope image
microscope_image, x, y, radius = create_microscope_image(base_image)

# Create dye image
base_image = create_base_image((size, size))
dye_image = create_dye_image(base_image, x, y, radius)

# dye_image = create_dye_image_with_lines(base_image, x, y)

# Save images
save_image(microscope_image, 'microscope_image.bmp')
save_image(dye_image, 'dye_image.bmp')
# Convert images to to compresssed format

# Convert microscope image to quad tree
microscope_image = np.array(microscope_image)
microscope_tree = convert_to_quad_tree(microscope_image, 0, 0, size-1, size-1)

# Convert dye image to quad tree
dye_image = np.array(dye_image)
dye_tree = convert_to_quad_tree(dye_image, 0, 0, size-1, size-1)

# Compress microscope image
microscope_compressed = compress(microscope_tree)

# Compress dye image
dye_compressed = compress(dye_tree)

# Save compressed images
save(microscope_compressed, 'microscope')
save(dye_compressed, 'dye')

# Calculate if parasite have cancer or not (Slow Verison)

# Get start time
start_time = time.time()

# Open microscope image
microscope_image = Image.open('microscope_image.bmp')
microscope_image = np.array(microscope_image)
# Open dye image
dye_image = Image.open('dye_image.bmp')
dye_image = np.array(dye_image)
# Get overlap
microscope_black_pixels, overlaped_black_pixels = find_overlap_slow(
    microscope_image, dye_image)

# Get end time
end_time = time.time()

# Print results
print('Slow Version:')
print('Overlap: ' + str((overlaped_black_pixels /
      microscope_black_pixels)*100)[:5] + '%')
if (overlaped_black_pixels/microscope_black_pixels)*100 > 10:
    print('Parasite have cancer')
else:
    print('Parasite do not have cancer')

# Print time
print('Time: ' + str(end_time - start_time)[:5] + 's')

# Calculate if parasite have cancer or not (Fast Verison)

# Get start time
start_time = time.time()

# Open compressed microscope image
with open('compressed_microscope.txt') as compressed_file:
    microscope_data = compressed_file.read()

# Open compressed dye image
with open('compressed_dye.txt') as compressed_file:
    dye_data = compressed_file.read()


# Extract microscope image
microscope_tree = extract(microscope_data, 0, 0, size, size, True)
black_pixels = return_global_black_pixels()
# Extract dye image
reset_index()
dye_tree = extract(dye_data, 0, 0, size, size)

# Get overlap
overlaped_black_pixels = find_overlap_fast(microscope_tree, dye_tree)

# Get end time
end_time = time.time()

# Print results
print('Fast Version:')
print('Overlap: ' + str((overlaped_black_pixels/black_pixels)*100)[:5] + '%')
if (overlaped_black_pixels/black_pixels)*100 > 10:
    print('Parasite have cancer')
else:
    print('Parasite do not have cancer')

# Print time
print('Time: ' + str(end_time - start_time)[:5] + 's')
