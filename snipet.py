from rembg import remove
from PIL import Image
print("Attempting to remove background...")
try:
    img = Image.open("photo.jpg")
    remove(img).save("no_bg.png")
    print("Background removed successfully. Saved as no_bg.png")
except FileNotFoundError:
    print("Error: 'photo.jpg' not found. Please ensure the file exists in the current directory.")