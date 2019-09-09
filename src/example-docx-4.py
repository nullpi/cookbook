from docxcompose.composer import Composer
from docx import Document

doc1 = Document("1.docx")
composer = Composer(doc1)

doc2 = Document("2.docx")
composer.append(doc2)

composer.save("合并后的文件.docx")