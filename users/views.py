from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from public.models import Post
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm, UserUpdateForm, UserProfileUpdateForm

def register (request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your account has been successfully created. You can now login.")
            return redirect('signin-page')

    else:
        form = UserSignupForm()

    return render(request, 'users/signup.html', {'form': form})

@login_required
def profile (request):
    if request.POST:
        u_updateForm = UserUpdateForm(request.POST, instance=request.user)
        u_updateProfileForm = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_updateForm.is_valid() or u_updateProfileForm.is_valid():
            u_updateForm.save()
            u_updateProfileForm.save()

            messages.success(request, f'Your Account as been updated successfully!')
            redirect('profile-page')

    else:
        u_updateForm = UserUpdateForm(instance=request.user)
        u_updateProfileForm = UserProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_updateForm': u_updateForm,
        'u_updateProfileForm': u_updateProfileForm
    }
    return render (request, 'users/profile.html', context)


class PostList(ListView):
    model=Post
    template_name='users/post_list.html'
