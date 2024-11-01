import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def scaleImage(image, scale_factor):
    """
    Melakukan scaling (zoom) pada gambar
    
    Parameters:
    image: array - Citra input
    scale_factor: float - Faktor scaling (0-1 untuk memperkecil, >1 untuk memperbesar)
    
    Returns:
    array - Citra hasil scaling
    """
    height, width = image.shape[:2]
    
    # Hitung dimensi baru
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)
    
    # Buat gambar kosong dengan dimensi baru
    scaled_image = np.zeros((new_height, new_width, 3), dtype=image.dtype)
    
    # Hitung rasio scaling
    y_ratio = height / new_height
    x_ratio = width / new_width
    
    # Lakukan scaling untuk setiap piksel
    for y in range(new_height):
        for x in range(new_width):
            # Hitung posisi piksel di gambar asli
            src_y = int(y * y_ratio)
            src_x = int(x * x_ratio)
            
            # Salin nilai piksel
            scaled_image[y, x] = image[src_y, src_x]
            
    return scaled_image

def rotateImage(image, degree):
    """
    Melakukan rotasi gambar dengan sudut tertentu
    
    Parameters:
    image: array - Citra input
    degree: float - Sudut rotasi dalam derajat
    
    Returns:
    array - Citra hasil rotasi
    """
    # Konversi sudut ke radian dan hitung sin cos
    radian_deg = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)
    
    # Ambil dimensi gambar
    height, width = image.shape[:2]
    
    # Hitung dimensi gambar output
    max_dim = int(np.sqrt(height**2 + width**2))
    
    # Buat gambar kosong dengan dimensi yang cukup
    outputImage = np.zeros((max_dim, max_dim, 3), dtype=image.dtype)
    
    # Tentukan titik pusat rotasi
    centerY, centerX = max_dim//2, max_dim//2
    
    # Lakukan rotasi untuk setiap piksel
    for y in range(-height//2, height//2):
        for x in range(-width//2, width//2):
            # Hitung koordinat baru setelah rotasi
            newX = int(cos_deg * x - sin_deg * y) + centerX
            newY = int(sin_deg * x + cos_deg * y) + centerY
            
            # Pastikan koordinat baru berada dalam batas gambar
            if 0 <= newX < max_dim and 0 <= newY < max_dim:
                # Salin nilai piksel ke posisi baru
                outputImage[newY, newX] = image[y + height//2, x + width//2]
                
    return outputImage

# Membaca gambar
image = img.imread('C:\\Users\\ASUS VIVOBOOK GO14\\Documents\\Semester 5\\pengolahan Citra Digital\\Sesi 6\\cherry-blossoms-full-bloom-against-pink-sky_715003-2971.jpg')

# Lakukan scaling (zoom minus) dengan faktor 0.5 (setengah dari ukuran asli)
scaled_image = scaleImage(image, 0.5)

# Melakukan rotasi 45 derajat pada gambar yang sudah di-scale
rotated_image = rotateImage(scaled_image, 45)

# Tampilkan hasil
plt.figure(figsize=(15, 5))

# Gambar asli
plt.subplot(1, 3, 1)
plt.title('Gambar Asli')
plt.imshow(image)

# Gambar hasil scaling
plt.subplot(1, 3, 2)
plt.title('Hasil Scaling (0.5x)')
plt.imshow(scaled_image)

# Gambar hasil rotasi
plt.subplot(1, 3, 3)
plt.title('Hasil Rotasi (45 derajat)')
plt.imshow(rotated_image)

plt.show()