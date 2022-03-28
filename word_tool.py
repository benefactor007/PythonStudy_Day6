if __name__ == '__main__':
    from docxtpl import DocxTemplate,RichText

    doc = DocxTemplate("5HG035877_CNS3.0.docx")
    rt = RichText('World company', italic = True)
    rt.add("Star", color='#ff00ff', style="Times New Roman")
    context = {'partnumbername': rt}

    doc.render(context)
    doc.save("generated_doc.docx")



    """
    from docxtpl import DocxTemplate, RichText
    
    tpl = DocxTemplate('test_files/richtext_tpl.docx')
    
    rt = RichText('an exemple of ')
    rt.add('a rich text', style='myrichtextstyle')
    rt.add('some violet', color='#ff00ff')
    
    context = {
        'example': rt,
    }
    
    tpl.render(context)
    tpl.save('test_files/richtext.docx')
    """