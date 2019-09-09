from docxtpl import DocxTemplate

doc = DocxTemplate("收据模板.docx")
context = { 
                    'no' : '1848810', 
                    'date' : '2019-9-4', 
                    'payer' : '张三', 
                    'title' : '定金', 
                    'sum' : '¥800.00', 
                    'summary' : ('1，定金不可退；', '2，三天内支付余款，优惠200元'), 
                    'payee' : '李四'
                }
doc.render(context)
doc.save("一张收据.docx")