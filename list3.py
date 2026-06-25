@login_required
def profile(request):
    profile_obj, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile_obj.fio = request.POST.get('fio', '')
        profile_obj.spec = request.POST.get('spec', '')
        profile_obj.grupa = request.POST.get('grupa', '')

        kurs_value = request.POST.get('kurs')
        profile_obj.kurs = int(kurs_value) if kurs_value else None

        profile_obj.obuch = request.POST.get('obuch', '')
        profile_obj.vid = request.POST.get('vid', '')
        profile_obj.kod = request.POST.get('kod', '')

        profile_obj.save()

        messages.success(request, "Данные успешно сохранены")
        return redirect('/profile/')

    return render(request, 'profile.html', {
        'profile': profile_obj,
    })
