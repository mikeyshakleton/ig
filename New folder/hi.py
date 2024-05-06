from PIL import Image
im = Image.open("assets/button.gif")
w,h = im.size
print(w,h)
