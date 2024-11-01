import numpy as np
import imageio.v3 as img
import matplotlib.pyplot as plt

def mirror_combined(image):
    """
    Melakukan pencerminan horizontal dan vertikal secara bersamaan
    
    Parameters:
    image: array - Citra input
    
    Returns:
    tuple - (pencerminan_horizontal, pencerminan_vertikal, pencerminan_ganda)
    """
     
    height, width = image.shape[:2]
    
     
    horizontal = np.zeros_like(image)
    vertical = np.zeros_like(image)
    combined = np.zeros_like(image)   
    
     
    for y in range(height):
        for x in range(width):
             
            horizontal[y, x] = image[y, width - 1 - x]
            
             
            vertical[y, x] = image[height - 1 - y, x]
            
             
            combined[y, x] = image[height - 1 - y, width - 1 - x]
            
    return horizontal, vertical, combined

 
path = 'C:\\Users\\ASUS VIVOBOOK GO14\\Documents\\Semester 5\\pengolahan Citra Digital\\Sesi 6\\cherry-blossoms-full-bloom-against-pink-sky_715003-2971.jpg'
image = img.imread(path)
image = img.imread(path)

 
horizontal_mirror, vertical_mirror, combined_mirror = mirror_combined(image)

 
plt.figure(figsize=(15, 5))


plt.subplot(1, 4, 1)
plt.title('Gambar Asli')
plt.imshow(image)

 
plt.subplot(1, 4, 2)
plt.title('Pencerminan Horizontal')
plt.imshow(horizontal_mirror)


plt.subplot(1, 4, 3)
plt.title('Pencerminan Vertikal')
plt.imshow(vertical_mirror)


plt.subplot(1, 4, 4)
plt.title('Pencerminan H+V')
plt.imshow(combined_mirror)

plt.tight_layout()
plt.show()