from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'a_users/profile.html', {'profile': profile})

@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    return render(request, 'a_users/profile_edit.html', {'form': form})