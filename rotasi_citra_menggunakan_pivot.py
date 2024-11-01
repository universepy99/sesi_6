import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def rotateImageCorner(image, degree):
    """
    Melakukan rotasi gambar dengan pivot di pojok kiri atas (0,0)
    
    Parameters:
    image: array - Citra input
    degree: float - Sudut rotasi dalam derajat
    
    Returns:
    array - Citra hasil rotasi
    """
    
    radian_deg = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)
    
    
    height, width = image.shape[:2]
    
    
    new_height = int(abs(height * cos_deg) + abs(width * sin_deg))
    new_width = int(abs(width * cos_deg) + abs(height * sin_deg))
    
   
    outputImage = np.zeros((new_height, new_width, 3), dtype=image.dtype)
    
    
    for y in range(height):
        for x in range(width):
            
            newX = int(x * cos_deg - y * sin_deg)
            newY = int(x * sin_deg + y * cos_deg)
            
            
            if degree > 0:
                newX += int(height * sin_deg)
            else:
                newY += int(width * sin_deg)
            
            
            if 0 <= newX < new_width and 0 <= newY < new_height:
                outputImage[newY, newX] = image[y, x]
    
    return outputImage


image = img.imread('C:\\Users\\ASUS VIVOBOOK GO14\\Documents\\Semester 5\\pengolahan Citra Digital\\Sesi 6\\cherry-blossoms-full-bloom-against-pink-sky_715003-2971.jpg')



angles = [45, 90, -45]
plt.figure(figsize=(15, 5))


plt.subplot(1, 4, 1)
plt.title('Gambar Asli')
plt.imshow(image)


for i, angle in enumerate(angles, 2):
    rotated = rotateImageCorner(image, angle)
    plt.subplot(1, 4, i)
    plt.title(f'Rotasi {angle}°')
    plt.imshow(rotated)

plt.tight_layout()
plt.show()