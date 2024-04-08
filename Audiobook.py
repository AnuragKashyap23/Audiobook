import pyttsx3
import PyPDF2
book = open('compnet.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)

stop_page = 5
speaker = pyttsx3.init()
for num in range(4, pages):
    page = pdfReader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()

    if num == stop_page:
        speaker.stop()
        break  # Exit the loop if you want to stop reading altogether
    
    speaker.runAndWait()