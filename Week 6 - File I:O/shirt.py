#In a file called shirt.py, implement a program that expects exactly two command-line arguments:
#in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
#in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
#The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.
#Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default values for method, bleed, and centering, overlay the shirt with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.
#The program should instead exit via sys.exit:
#if the user does not specify exactly two command-line arguments,
#if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
#if the input’s name does not have the same extension as the output’s name, or
#if the specified input does not exist.
#Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.
#If you’d like to run your program on a photo of yourself, first drag the photo over to VS Code’s file explorer, into the same folder as shirt.py. No need to submit any photos with your code. But, if you would like, you’re welcome (but not expected) to share a photo of yourself wearing your virtual shirt in any of CS50’s communities!


import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("Incorrect number of arguments")
    else:
        open_file(sys.argv[1], sys.argv[2])

def open_file(file_in, file_out):
    _, ext1 = os.path.splitext(file_in)
    _, ext2 = os.path.splitext(file_out)
    try:
       if ext1 not in [".jpg", ".jpeg", ".png"] or ext2 not in [".jpg", ".jpeg", ".png"]:
           raise ValueError
       elif ext1 != ext2:#checking both files have the same extension
           raise ValueError
       else:
               file_input(Image.open(file_in), file_out)
    #except ValueError:
    #    sys.exit("File extension not valid")
    except FileNotFoundError:
        sys.exit("File not found")

def file_input(image_in, image_out):
    cs50 = Image.open("shirt.png")#opening shirt image to overlap
    cs50_size = cs50.size
    image_size = image_in.size

    if cs50_size != image_size:
        image_resize = ImageOps.fit(image_in, cs50_size)
        image_resize.paste(cs50, (0, 0), cs50)
        image_resize.save(image_out)
    else:
        image_in.paste(cs50, (0, 0), cs50)
        image_in.save(image_out)


if __name__ == "__main__":
    main()