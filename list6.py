@login_required
def download_all_documents_zip(request):
    profile_obj = Profile.objects.get(user=request.user)

    documents = [
        ('attestation_educational.docx',
         f'attestation_educational_{request.user.username}.docx'),
        ('attestation_industrial.docx',
         f'attestation_industrial_{request.user.username}.docx'),
        ('characteristic.docx',
         f'characteristic_{request.user.username}.docx'),
    ]

    zip_buffer = BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        pass

    response = HttpResponse(
        zip_buffer.getvalue(),
        content_type='application/zip'
    )

    response['Content-Disposition'] = (
        f'attachment; filename="documents_{request.user.username}.zip"'
    )

    return response
