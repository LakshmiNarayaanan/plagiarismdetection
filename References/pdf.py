import PyPDF2

import requests
file_url = "https://faculty.fuqua.duke.edu/~brav/Alon_Brav_papers.pdf"

r = requests.get(file_url, stream = True)

with open("syed.pdf","wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):

         # writing one chunk at a time to pdf file
         if chunk:
             pdf.write(chunk)
    pdf.close()
filename = "syed.pdf"

pdfFileObj = open(filename,'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

num_pages = pdfReader.numPages
count = 0
text = ""

while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

print (text)