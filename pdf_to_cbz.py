import os
from wand.image import Image
from wand.display import display
from itertools import product
import shutil


def pdf2cbz(filename, keep_image_files, keep_zip_file, keep_pdf_file):

    target_folder = filename.split(".")[0]


    print("Start reading pdf. This could take a minute...")
    pages = Image(filename=filename)
    print("PDF successfully read.")

    print("{0} pages detected".format(len(pages.sequence)))

    os.mkdir(target_folder)

    print("Images are temporarily saved for creating the cbz archive.")
    pages.save(filename="{0}/{1}.jpg".format(target_folder, target_folder))
    print("Images successfully saved!")

    print("Zipping images in archive.")
    shutil.make_archive("{0}".format(target_folder), 'zip', target_folder)
    print("Archive zipped")

    if not keep_image_files:
        shutil.rmtree(target_folder)
        print("Removed image folder")

    if not keep_zip_file:
        print("Renaming archive to .cbz")
        os.rename("{0}.zip".format(target_folder), "{0}.cbz".format(target_folder))
        print("Your .cbz manga is ready!")
    else:
        print("cp then rename :)")

    if not keep_pdf_file:
        os.remove(filename)

    first_page = pages.sequence[0]

    with Image(first_page) as i:
        display(i)

if __name__ == "__main__":

    print("--------------------------------------------------")
    print("Will create a .cbz ebook compatible file from pdf.")
    print("Made with love for mangas lovers reading on ebook.")
    print("--------------------------------------------------")

    pdf_file = "naruto1.pdf"

    pdf2cbz(pdf_file, False, False, False)
