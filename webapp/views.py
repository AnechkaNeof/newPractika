from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateClientForm, UpdateClientForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Client

from django.contrib import messages

# Homepage

def home(request):

    return render(request, 'webapp/index.html')

# - Register

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Аккаунт успешно создан!" )
            return redirect("my-login")

    context = {'form': form}

    return render(request, 'webapp/register.html', context=context)

#  - Login a user

def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    
    context = {'form': form}

    return render(request, 'webapp/my-login.html', context=context)

#  - Dashboard

@login_required(login_url='my-login')
def dashboard(request):
    my_clients = Client.objects.all()
    context = {'clients': my_clients}
    return render(request, 'webapp/dashboard.html', context=context)

# - Create a record
@login_required(login_url='my-login')
def create_record(request):
    form = CreateClientForm()
    if request.method == "POST":
        form = CreateClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Карточка успешно создана!" )
            return redirect("dashboard")
    context = {'form': form}
    return render(request, 'webapp/create-record.html', context=context)

# - Update a record
@login_required(login_url='my-login')
def update_record(request, pk):
    record = Client.objects.get(id=pk)
    form = UpdateClientForm(instance=record)
    if request.method == "POST":
        form = UpdateClientForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Карточка была обновлена!" )
            return redirect("dashboard")
    context = {'form': form}
    return render(request, 'webapp/update-record.html', context=context)

# - Read / View a singular record

@login_required(login_url='my-login')
def singular_record(request, pk):
    all_records = Client.objects.get(id=pk)
    context = {'client':all_records}
    return render (request, 'webapp/view-record.html', context=context)

# - Delete a record
@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Client.objects.get(id=pk)
    record.delete()
    messages.success(request, "Карточка была удалена!" )
    return redirect("dashboard")

# - User logout

def user_logout(request):
    auth.logout(request)
    messages.success(request, "Вы вышли из аккаунта!" )
    return redirect("my-login")



