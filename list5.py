def generate_document_bytes(profile_obj, template_filename):
    template_path = os.path.join(
        settings.BASE_DIR,
        'mainNNV',
        'templates',
        'docs',
        template_filename
    )

    doc = Document(template_path)
    context = get_common_context(profile_obj)
    replace_placeholders(doc, context)

    file_stream = BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)

    return file_stream, template_path
