from django.shortcuts import render, redirect
from .forms import *
from .models import *
from datetime import datetime

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
            # check if feedback is done for this month or not
            if user.feedback.create_time.month == datetime.now().month:
                print('wow !! Feedback done for this month !!')
            else:
                # month changed, so delete the previous feedback object and make the student's feedbck field empty, turn the feedback_given field off
                f = user.feedback
                f.delete()
                
                user.feedback_given = False
                user.save()
                
                if user.feedback:
                    print('not deleted\n\n')
                else:
                    print('deleted\n')
                print('nooooppsyyyyyyy, we need to delete prev model')
            if user.feedback:
                # check if mnonth has expired
                print('\nfeedback creation time : ' + str(user.feedback.create_time) + '\n')
                print('ohhhhhhh yeahhhhh!!')
            else:
                print('nooooooooooooooooouuuu!')
            
            if request.method=='POST':
                print(request.POST)
                
                # check if he/she has already rated 
                if user.feedback:
                    f = user.feedback
                    f.uniform_and_punctuality = request.POST['uniform_and_punctuality']
                    f.cleanliness_and_hygiene = request.POST['cleanliness_and_hygiene']
                    f.waste_disposal = request.POST['waste_disposal']
                    f.quality_of_ingredients = request.POST['quality_of_ingredients']
                    f.overall_satisfaction_of_breakfast = request.POST['overall_satisfaction_of_breakfast']
                    f.overall_satisfaction_of_lunch = request.POST['overall_satisfaction_of_lunch']
                    f.overall_satisfaction_of_dinner = request.POST['overall_satisfaction_of_dinner']
                    f.save()
                else:
                    # create a new feedback object

                    newFeed = Feedback(
                        uniform_and_punctuality = request.POST['uniform_and_punctuality'],
                        cleanliness_and_hygiene = request.POST['cleanliness_and_hygiene'],
                        waste_disposal = request.POST['waste_disposal'],
                        quality_of_ingredients = request.POST['quality_of_ingredients'],
                        overall_satisfaction_of_breakfast = request.POST['overall_satisfaction_of_breakfast'],
                        overall_satisfaction_of_lunch = request.POST['overall_satisfaction_of_lunch'],
                        overall_satisfaction_of_dinner = request.POST['overall_satisfaction_of_dinner'],
                    )
                    newFeed.save()

                    # connect the feedback object to the student

                    user.feedback = newFeed
                    user.save()

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