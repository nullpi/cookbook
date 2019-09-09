from docx import Document
document = Document()
document.add_paragraph('你好，Python')
document.save('新建docx文件.docx')