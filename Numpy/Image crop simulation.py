import numpy as np

#Image crop simulation
image_size = np.random.randint(0,256,size=(6,6)) #Creating the image
print(f'Image size: {image_size}')

#Extracting the top-left 3x3
top_left = image_size[0:3,0:3]
print(f'Top-left: {top_left}')

#Extracting the bottom-right 2x4
bottom_right = image_size[4:6,2:6]
print(f'Bottom-right: {bottom_right}')

#Extracting alternate row
alternate_row = image_size[0:5:2, 0:6]
print(f'Alternate row: {alternate_row}')

#Extracting alternate column
alternate_column = image_size[0:6, 0:5:2]
print(f'Alternate column: {alternate_column}')

#Extracting the center
center = image_size[2:4, 2:4]
print(f'Center: {center}')
