from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Date, Calendar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
# Create your views here.


def calendar_view(request):
    user = request.user  # 获取当前登录的用户
    if not isinstance(user, User):
        raise ValueError(f"Expected a User instance, got {type(user)} instead.")
    calendar = get_object_or_404(Calendar, user=user)  # 确保传递的是 User 实例
    dates = Date.objects.filter(calendar=calendar)
    return render(request, 'holidays/calendar.html', {'dates': dates})

@login_required
def add_holiday(request, year, month, day):
    calendar = get_object_or_404(Calendar, user=request.user)
    date, created = Date.objects.get_or_create(year=year, month=month, day=day)
    if request.method == "POST":
        holiday_info = request.POST.get('holiday_info')
        calendar.add_holiday(date, holiday_info)
        return redirect('calendar_view')
    return render(request, 'holidays/add_holiday.html', {'date': date})

@login_required
def remove_holiday(request, year, month, day):
    calendar = get_object_or_404(Calendar, user=request.user)
    date = get_object_or_404(Date, year=year, month=month, day=day)
    if request.method == "POST":
        calendar.remove_holiday(date)
        return redirect('calendar_view')
    return render(request, 'holidays/remove_holiday.html', {'date': date})

@login_required
def profile_view(request):
    return render(request, 'holidays/profile.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('calendar_view')
    else:
        form = UserCreationForm()
    return render(request, 'holidays/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('calendar_view')
    else:
        form = AuthenticationForm()
    return render(request, 'holidays/login.html', {'form': form})

