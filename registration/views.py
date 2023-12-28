from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .models import Material,Department,Order,Course
from .forms import OrderForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='registration:login')
def dashboard(request):
    return render(request, 'dashboard.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password2']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('registration:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "Registration successful. Please log in.")
                return redirect('registration:login')
        else:
            messages.info(request, "Password not matching")
            return redirect('registration:register')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('registration:dashboard')  # Redirect to the dashboard page after login
        else:
            messages.info(request, 'Invalid Username/Password')
            return redirect('registration:login')

    return render(request, 'login.html')
def order(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'order_confirm.html', {'message': 'Order Confirmed'})
    else:
        form = OrderForm()

    return render(request, 'order.html', {'form': form, 'departments': departments})