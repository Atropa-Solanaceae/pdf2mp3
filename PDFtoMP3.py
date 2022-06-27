from PyPDF2 import PdfFileReader
from pyttsx3 import init
import os

def getText():
    try:
        txt = ""
        with open('[yourfile].pdf', 'rb') as f:
            pdfReaderObj = PdfFileReader(f)
            numPages = pdfReaderObj.getNumPages()
            for pageN in range(numPages):
                page = pdfReaderObj.getPage(pageN)
                pageContent = page.extractText()
                txt += pageContent
            return txt
    except:
        print("\n\n\nSorry, your pdf either has an invalid name or the program could not find it")
        print("Please make sure you're running this program while inside the directory the pdf is located in")

try:
    os.system('pip install PyPDF2')
    os.system('pip install pyttsx3')
except:
    print("The modules needed for this program were not installed automatically, please use pip to install PyPDF2 and pyttsx3 and run again")

txt = getText()
engine = init()
engine.save_to_file(txt, 'outputfile.mp3')
engine.runAndWait()
