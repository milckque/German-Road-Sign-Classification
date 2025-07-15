from PIL import Image

img = Image.open("1A6C4C65-5B80-476D-8356-C896F0B2DC66_4_5005_c.jpeg")

print(f"Image size: {img.size}")
print(f"Image mode: {img.mode}")