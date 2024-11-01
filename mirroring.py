import numpy as np
import imageio.v3 as img
import matplotlib.pyplot as plt

def mirror_image(image):
    """
    Membuat pencerminan horizontal dan vertikal dari gambar input
    
    Parameters:
    image: array - Citra input
    
    Returns:
    tuple - (pencerminan_horizontal, pencerminan_vertikal)
    """
     
    height, width = image.shape[:2]
    
     
    horizontal = np.zeros_like(image)
    vertical = np.zeros_like(image)
    
     
    for y in range(height):
        for x in range(width):
            horizontal[y, x] = image[y, width - 1 - x]
            
      
    for y in range(height):
        for x in range(width):
            vertical[y, x] = image[height - 1 - y, x]
            
    return horizontal, vertical

 
path = 'C:\\Users\\ASUS VIVOBOOK GO14\\Documents\\Semester 5\\pengolahan Citra Digital\\Sesi 6\\cherry-blossoms-full-bloom-against-pink-sky_715003-2971.jpg'
image = img.imread(path)

 
horizontal_mirror, vertical_mirror = mirror_image(image)

 
plt.figure(figsize=(10, 5))

 
plt.subplot(1, 3, 1)
plt.title('Gambar Asli')
plt.imshow(image)

 
plt.subplot(1, 3, 2)
plt.title('Pencerminan Horizontal')
plt.imshow(horizontal_mirror)

 
plt.subplot(1, 3, 3)
plt.title('Pencerminan Vertikal')
plt.imshow(vertical_mirror)

plt.show()