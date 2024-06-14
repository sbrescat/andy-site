from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

from news.models import Comments


# Create your views here.

@login_required
def profile_view(request):
    author = request.user
    comments = Comments.objects.filter(author=author)  # Замените на ваш способ получения комментариев пользователя
    context = {
        'user': author,
        'comments': comments,
    }
    return render(request, 'users/profile.html', context)

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Обновление сессии пользователя
            messages.success(request, 'Пароль успешно изменён!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка. Измените данные.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})

#def logout_user(request):
#return HttpResponse("logout")
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            #form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(reverse('home'))
    else:
        form = AuthenticationForm()
        return render(request, "users/login.html", {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('home'))

# cd = form.cleaned_data
# user = authenticate(request, username=cd['username'],
# password=cd['password'])
# if user and user.is_active: