import tkinter as tk
from PIL import Image
from PIL import ImageTk as itk
import fitz
import os
import io

class ImageViewer(object):

    def __init__(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(master = self.parent)

        self.canvas.bind("<MouseWheel>", self.zoom)
        self.canvas.bind('<ButtonPress-1>', lambda event: self.canvas.scan_mark(event.x, event.y))
        self.canvas.bind("<B1-Motion>", lambda event: self.canvas.scan_dragto(event.x, event.y, gain=1))

        self.imageLoad(os.path.dirname(__file__) + "\\minus.png")

    def zoom(self, event):
        pass

    def imageLoad(self, img):
        self.canvas.delete("all")
        self.canvas.xview("moveto", 0), self.canvas.yview("moveto", 0)
        if ".pdf" in img:
            doc = fitz.open(img)
            evImg = Image.new("RGB", (595,0))
            for page in doc:
                img = page.getPixmap(alpha = False)
                pngImg = img.getPNGData()
                pngImage = Image.open(io.BytesIO(pngImg))
                evImg = self.imageMerge(evImg, pngImage)
        else:
            evImg = Image.open(img)

        print(evImg)
        evImgItk = itk.PhotoImage(evImg)

        self.canvas.width, self.canvas.height = evImg.size

        self.canvas.create_image(self.canvas.width * 0.5, self.canvas.height * 0.5, image = evImgItk, anchor = "center")
        self.canvas.image = evImgItk
        

    def imageMerge(self, imgOne, imgTwo):
        newImg = Image.new("RGB", (imgOne.width, imgOne.height + imgTwo.height))

        newImg.paste(imgOne, (0, 0))
        newImg.paste(imgTwo, (0, imgOne.height))

        return newImg        
