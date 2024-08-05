!pip install pillow numpy

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files


def encrypt_image(image_path, key):
   
    image = Image.open(image_path)
  
    image_array = np.array(image)

  
    encrypted_array = (image_array + key) % 256

   
    encrypted_image = Image.fromarray(np.uint8(encrypted_array))

    return encrypted_image

def decrypt_image(encrypted_image, key):
    
    encrypted_array = np.array(encrypted_image)

    
    decrypted_array = (encrypted_array - key) % 256

    
    decrypted_image = Image.fromarray(np.uint8(decrypted_array))

    return decrypted_image


uploaded = files.upload()


image_path = next(iter(uploaded))


key = 50  # Example key for encryption and decryption
encrypted_image = encrypt_image(image_path, key)


encrypted_image_path = "encrypted_image.png"
encrypted_image.save(encrypted_image_path)
plt.imshow(encrypted_image)
plt.title("Encrypted Image")
plt.show()


decrypted_image = decrypt_image(encrypted_image, key)


decrypted_image_path = "decrypted_image.png"
decrypted_image.save(decrypted_image_path)
plt.imshow(decrypted_image)
plt.title("Decrypted Image")
plt.show()
