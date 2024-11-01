import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def Translasi(image, shiftX, shiftY):
    """
    Melakukan translasi pada citra dengan pergeseran pada sumbu X dan Y
    
    Parameters:
    image: array - Citra input
    shiftX: int - Jumlah pergeseran horizontal (positif ke kanan, negatif ke kiri)
    shiftY: int - Jumlah pergeseran vertikal (positif ke bawah, negatif ke atas)
    
    Returns:
    array - Citra hasil translasi
    """
     
    imgTranslasi = np.roll(image, shift=shiftY, axis=0)   
    imgTranslasi = np.roll(imgTranslasi, shift=shiftX, axis=1)   
    
      
    if shiftY > 0:
        imgTranslasi[:shiftY, :] = 0    
    elif shiftY < 0:
        imgTranslasi[shiftY:, :] = 0    
        
    if shiftX > 0:
        imgTranslasi[:, :shiftX] = 0    
    elif shiftX < 0:
        imgTranslasi[:, shiftX:] = 0    
        
    return imgTranslasi

 
image = img.imread("C:\\Users\\ASUS VIVOBOOK GO14\\Documents\\Semester 5\\pengolahan Citra Digital\\Sesi 6\\cherry-blossoms-full-bloom-against-pink-sky_715003-2971.jpg")

 
imgResult = Translasi(image, shiftX=50, shiftY=-300)


plt.figure(figsize=(10,10))
plt.subplot(2,1,1)
plt.imshow(image)
plt.subplot(2,1,2)
plt.imshow(imgResult)
plt.show()