def register(request): 
if request.method == 'POST': 
  form = UserCreationForm(request.POST) 
  
  if form.is_valid(): user = form.save() 
    Profile.objects.get_or_create(user=user) 
    login(request, user) messages.success(request, f'Добро пожаловать, {user.username}!') 
    return redirect('/profile/') 
form = UserCreationForm() 
return render(request, "register.html", {"form": form})
