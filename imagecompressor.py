import PIL
from PIL import Image
from tkinter.filedialog import *

def intro():
    print("IMAGE COMPRESSOR" + "\n "+ "Bu program seçilen resim dosyasının kalitesini bozmadan boyutunu düşürmeye yarar")
intro()

def compression():
   file_path = askopenfilename()
   Image = PIL.Image.open(file_path)
   height,widht = Image.size
   Img = Image.resize((height,widht),PIL.Image.ANTIALIAS)
   save_path = asksaveasfilename()
   Img.save(save_path+"Img.jpeg")
compression()
