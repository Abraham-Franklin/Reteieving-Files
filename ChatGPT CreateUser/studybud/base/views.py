from django.shortcuts import render
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to a success page
            return redirect('success')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
