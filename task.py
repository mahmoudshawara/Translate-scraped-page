import os
from googletrans import Translator
from bs4 import BeautifulSoup
translator = Translator()
# read all html file is the main directory and sub directories
dirpath = '/home/websites/task'
htmlfiles = []
for dirpath, subdirs, files in os.walk(dirpath):
    for x in files:
        if x.endswith(".html"):
            htmlfiles.append(os.path.join(dirpath, x))
            #print(htmlfiles)
# creat function that take the path of the html file and return translated page 
def translate_file (path):
    print(path) # print file being translated
    f=open(path ,'r+')
    document= f.read()
    #print(str(document))
    soup = BeautifulSoup(document,'html.parser')
    text_elements = [element for element in soup.find_all(string=True) if element.parent.name not in ['script', 'style']]
    if text_elements:
        for element in text_elements:
        #Extract the text from the element
            text = element.get_text(strip=True)
        # Skip the element if it's empty
            if not text:
                continue
            # Translate the text
            translated_text = translator.translate(text, src='en', dest='hi')
            # Replace the text in the element
            element.replace_with(translated_text.text)
    f.write(str(soup))
    f.close() 
    return(soup)          
for html in htmlfiles:
    translate_file(html)
