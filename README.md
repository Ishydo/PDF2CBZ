# PDF2CBZ

## There is no magic

Before you go, just know how this works : it creates a (or several) folder(s) containing an image for each page of the PDF file(s), then zip it, then **rename it** to .cbz extension.

It is a transformation, not a conversion.

Because yes, renaming a .zip to a .cbz file (like a disrespectful brute) works perfectly. The resulting file will work on ebook 99% of the time.

There is no specific conversion applied between .zip to .cbz. It is just about gaining time during the operation if (like me) you have a lot of PDF file to transform.

The PDF -> images is done with wand.

## How to use it

Clone the repo, create a virtualenv and install requirements (script is using wand & slugify).

```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

Unleash the beast

```
python3 pdf_to_cbz.py
```

And follow the instructions (please be a good and intelligent user, input are not controlled)

## Options

```
What mode do you want to use?
  1 - Simple PDF conversion
  2 - Multiple PDF in folder
```

1 - You have to specify the path to a single PDF file that will be converted

2 - You will have to specify a folder containing the multiple PDF files to convert (non .pdf or.PDF files will be ignored)

```
Do you want to keep the images folder(s)?
```

The script creates a folder per PDF to convert containing an image for each page of your file(s). This option allows you to keep this (those) folder(s). This may take a certain disk space if converting a lot of files!

```
Do you want to keep the zip file(s)?
```

After creating the images folder the script zip it before renaming it to .cbz. This option allows you to keep this (those) zip file(s) containing the images. It is basically the same question as the previous option but for a zip file.

```
Do you want top keep the PDF file(s)?
```

Define if your original PDF file will be deleted or not.
