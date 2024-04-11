# install pyttx3
# install pypdf2

import pyttsx3
import PyPDF2

with open('#file_name', 'rb') as book:

    full_text = ""

    reader = PyPDF2.PdfFileReader(book)

    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate", 100)

    for page in range(reader.numPages):
        next_page = reader.getPage(page)

        content = next_page.extractText()
        full_text += content

    audio_reader.save_to_file(full_text, "#your_file_name.mp3")
    audio_reader.runAndWait()

    