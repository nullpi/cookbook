from docx import Document

document = Document('新建docx文件.docx')

for paragraph in document.paragraphs:
    print(paragraph.text)