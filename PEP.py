#MODULES NEEDED

import PyPDF2
from pytesseract import pytesseract
from PIL import Image
from youtube_transcript_api import YouTubeTranscriptApi
from boilerpy3 import extractors
import pytesseract
import os
import pywhatkit as kit
import pyttsx3           
from deep_translator import GoogleTranslator

#D:\\SANJAI\\1.pdf
#or
#D:\\SANJAI\\12.7.pdf

def pdf():
    file=open('PDF.txt','a+')
    direc=input('enter directory of pdf : ')
    pdfFileObj = open(direc, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num=pdfReader.numPages
    print(num)
    for loop in range(num):
        pageObj = pdfReader.getPage(loop) 
        print(pageObj.extractText())
        file.write(pageObj.extractText())
    pdfFileObj.close()
    file.close()

#D:\\SANJAI\\PEP\\1.png

def image():
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    file=open('IMAGE.txt','a+')
    direc=input('enter directory of image : ')
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(direc))
    print(text)
    file.write(text)
    file.close()

def youtubecap():
    file=open('CAP.txt','a+',encoding='utf-8')
    link=input('enter video path (youtube) : ')
    i=link.split('/')
    srt = YouTubeTranscriptApi.get_transcript(i[-1], languages=['en'])
    temp=str(srt)
    file.write(temp)
    file.close()
    print(srt)
youtubecap()

def web():
    extractor = extractors.CanolaExtractor()
    file=open('web.txt','a+',encoding='utf-8')
    link=input('wep site link : ')
    doc = extractor.get_doc_from_url(link)
    page_title = doc.title
    page_contents = doc.content
    file.write(page_title)
    file.write(page_contents)
    file.close()
    print(page_title, end = "\n\n")
    print(page_contents)


#D:\\SANJAI\\PEP\\1.png

def hand():
    os.chdir(r"D:\SANJAI\PEP")
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = Image.open("1.png")  
    text = pytesseract.image_to_string(img)  
    kit.text_to_handwriting(text, rgb=[250, 0, 0])

#D:\\SANJAI\\PEP\\1.png
    
def translate():
    img = Image.open('1.png')     
    print(img)                          
    pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    result = pytesseract.image_to_string(img)
    with open('translate.txt',mode ='a') as file:
        file.write(result)
        file.close()
        print(result)
        translated = GoogleTranslator(source='auto', target='ta').translate(y)
        file.write(translated)
        file.close()
        print(translated)






