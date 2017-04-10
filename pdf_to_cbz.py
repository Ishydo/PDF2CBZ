import os
import sys
from wand.image import Image
from wand.display import display
from itertools import product
from slugify import slugify
import shutil
import re


def save_images_with_safe_numerotation(target_folder, image_sequence):
    '''This will save images with a suffix that will not cause any problem
    with the default system order.
    Example :   Default behaviour   (0, 1, 100, 101, 102, 103, 2, 3, 4)
                Solution            (000, 001, 002, 003, ...)
    Note : this could be replaced with a nice "sorted" on files
    '''
    index = 0
    for img in image_sequence.sequence:
        img_page = Image(image=img)

        # Old schooool
        if index < 10:
            suffix = "00{0}".format(index)
        elif index >= 10 and index < 100:
            suffix = "0{0}".format(index)
        else:
            suffix = index

        img_page.save(filename="{0}/img{1}.jpg".format(target_folder, suffix))
        index += 1

def pdf2cbz(filename, keep_image_files, keep_zip_file, keep_pdf_file):

    target_folder = filename.split(".")[0]

    print("Start reading pdf. This could take a minute...")
    pages = Image(filename=filename)
    print("PDF successfully read.")

    print("{0} pages detected".format(len(pages.sequence)))

    os.mkdir(target_folder)

    print("Images are temporarily saved for creating the cbz archive.")
    #pages.save(filename="{0}/".format(target_folder))
    save_images_with_safe_numerotation(target_folder, pages)
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
        shutil.copyfile("{0}.zip".format(target_folder), "{0}.cbz".format(target_folder))

    if not keep_pdf_file:
        os.remove(filename)

    '''first_page = pages.sequence[0]

    with Image(first_page) as i:
        display(i)'''

def pdf2cbz_folder(folder, keep_image_files, keep_zip_file, keep_pdf_file):
    files = [f for f in os.listdir(folder)]
    files = filter(lambda f: f.endswith(('.pdf','.PDF')), files)

    for f in files:
        filename, extension = os.path.splitext(f)
        filename_slugified = "{0}{1}".format(slugify(filename), extension)
        shutil.copyfile("{0}/{1}".format(folder, f), "{0}/{1}".format(folder, filename_slugified))

        pdf2cbz("{0}/{1}".format(folder, filename_slugified), keep_image_files, keep_zip_file, keep_pdf_file)

        os.remove("{0}/{1}".format(folder, filename_slugified))

        print("------------- FINISHED A PDF ----------------")

if __name__ == "__main__":

    print("--------------------------------------------------")
    print("Will create a .cbz ebook compatible file from pdf.")
    print("Made with love for mangas lovers reading on ebook.")
    print("--------------------------------------------------")

    pdf_file = "naruto1.pdf"

    mode = int(input("What mode do you want to use?\n\t 1 - Single PDF conversion\n\t 2 - Multiple PDF in folder\n Your choice: "))

    if mode == 1:
        print("Ok, will convert a single PDF.\n")
        pdf_file = input("Please enter the PDF file name:")
    elif mode == 2:
        print("Ok, will convert all PDF files in a folder.")
        folder = input("Please enter folder path:")
    else:
        print("Invalid input")
        sys.exit()

    keep_image_files_input = input("Do you want to keep the images folder(s)? ")
    keep_image_files = keep_image_files_input in ['True', 'true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']

    keep_zip_file_input = input("Do you want to keep the zip file(s)? ")
    keep_zip_file = keep_zip_file_input in ['True', 'true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']

    keep_pdf_file_input = input("Do you want to keep the PDF file(s)? ")
    keep_pdf_file = keep_pdf_file_input in ['True', 'true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']

    if mode == 1:
        pdf2cbz(pdf_file, keep_image_files, keep_zip_file, keep_pdf_file)
    elif mode == 2:
        pdf2cbz_folder(folder, keep_image_files, keep_zip_file, keep_pdf_file)
