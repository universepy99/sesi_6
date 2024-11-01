import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def rotateImage(image, degree):
    """
    Melakukan rotasi gambar dengan sudut tertentu
    
    Parameters:
    image: array - Citra input
    degree: float - Sudut rotasi dalam derajat
    
    Returns:
    array - Citra hasil rotasi
    """
    
    radian_deg = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)
    
    
    height, width = image.shape[:2]
    
    
    max_dim = int(np.sqrt(height**2 + width**2))
    
    
    outputImage = np.zeros((max_dim, max_dim, 3), dtype=image.dtype)
    
    
    centerY, centerX = max_dim//2, max_dim//2
    
   
    for y in range(-height//2, height//2):
        for x in range(-width//2, width//2):
            
            
            
            newX = int(cos_deg * x - sin_deg * y) + centerX
            newY = int(sin_deg * x + cos_deg * y) + centerY
            
            
            if 0 <= newX < max_dim and 0 <= newY < max_dim:
                
                outputImage[newY, newX] = image[y + height//2, x + width//2]
                
    return outputImage

# Membaca gambar
image = img.imread('C:\\Users\\ASUS VIVOBOOK GO14\\Documents\\Semester 5\\pengolahan Citra Digital\\Sesi 6\\cherry-blossoms-full-bloom-against-pink-sky_715003-2971.jpg')

# Melakukan rotasi 45 derajat
rotated_image = rotateImage(image, 45)

# Tampilkan hasil
plt.figure(figsize=(12, 6))

# Gambar asli
plt.subplot(1, 2, 1)
plt.title('Gambar Asli')
plt.imshow(image)

# Gambar hasil rotasi
plt.subplot(1, 2, 2)
plt.title('Hasil Rotasi (45 derajat)')
plt.imshow(rotated_image)

plt.show()