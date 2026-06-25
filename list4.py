def replace_placeholders(doc, context):
    for paragraph in doc.paragraphs:
        full_text = paragraph.text
        changed = False

        for key, value in context.items():
            if key in full_text:
                full_text = full_text.replace(key, str(value))
                changed = True

        if changed:
            if paragraph.runs:
                paragraph.runs[0].text = full_text
                for run in paragraph.runs[1:]:
                    run.text = ''
