from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def home(request):
    logged = False
    if 'user_id' in request.session:
        user = Student.objects.get(id=request.session['user_id'])
        if user.authent:
            logged = True
            return render(request, 'messapp/home.html', {'user': user, 'logged': logged})
        else:
            del request.sesion['user_id']
    return render(request, 'messapp/home.html', {'logged': logged})

def reg(request):
    if 'user_id' in request.session:
        user = Student.objects.get(id=request.session['user_id'])
        if user.authent:
            return redirect('messapp:home')
        else:
            del request.sesion['user_id']
    form = RegForm()
    if request.method=='POST':
        print(request.POST)
        print('\nform valid\n')
        form = RegForm(request.POST)
        print('\n\ncreating new user\n\n')
        newStud = form.save(commit=False)
        newStud.save()
        print('new student saved!\n\n')
        return redirect('messapp:login')
    return render(request, 'messapp/reg.html', {'form': form})

def login(request):
    form = LoginForm()
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        for x in Student.objects.all():
            if username==x.username and password==x.password:
                x.authent = True
                x.save()
                request.session['user_id'] = x.id
                return redirect('messapp:home')
    return render(request, 'messapp/login.html', {'form': form})

def logout(request):
    if 'user_id' in request.session:
        user = Student.objects.get(id=request.session['user_id'])
        if user.authent:
            user.authent = False
            user.save()
            del request.session['user_id']
            return render(request, 'messapp/logout.html', {})
        else:
            del request.session['user_id']
            return redirect('messapp:login')
    else:
        return redirect('messapp:login')
    

def feedback(request):
    if 'user_id' in request.session:
        user = Student.objects.get(id=request.session['user_id'])
        if user.authent:
            return render(request, 'messapp/feedback.html', {'user': user})
        else:
            del request.session['user_id']
    return redirect('messapp:login')

def profile(request):
    if 'user_id' in request.session:
        user = Student.objects.get(id=request.session['user_id'])
        if user.authent:
            return render(request, 'messapp/profile.html', {'user': user})
        else:
            del request.session['user_id']
    return redirect('messapp:login')

def select_dates(request):
    if 'user_id' in request.session:
        user = Student.objects.get(id=request.session['user_id'])
        if user.authent:
            return render(request, 'messapp/select_dates.html', {'user': user})
        else:
            del request.session['user_id']
    return redirect('messapp:login')










def showCalender(request):
    form = MyForm()
    return render(request, 'messapp/cal.html', {'form': form})