if __name__ == '__main__':
    from docxtpl import DocxTemplate

    doc = DocxTemplate("5HG035877_CNS3.0.docx")
    context = {'partnumbername': "World company"}
    doc.render(context)
    doc.save("generated_doc.docx")
