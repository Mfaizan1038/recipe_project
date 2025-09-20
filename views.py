from django.shortcuts import render, redirect  # Added redirect import
from .models import *  # Make sure the model is correctly imported
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.core.paginator import Paginator
from django.db.models import Q,Sum

def recipes(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')


        # Create the recipe object
        Recipe.objects.create(
            name=name,
            description=description,
            image=image
        )
        return redirect('/recipes/')
    queryset=Recipe.objects.all()
    context={'recipe':queryset}

    return render(request, "recipes.html",context)

def update_recipe(request,id):
    queryset=Recipe.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')
        queryset.name=name
        queryset.description=description
        if image:
            queryset.image=image
        queryset.save()
        return redirect('/recipes/')


    context={'receipe':queryset}
    return render(request, "recipe_update.html",context)



def delete_recipe(request,id):
    queryset=Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')

def login_page(request):
     if request.method == "POST":
       
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
             messages.error(request, "invalid username")
             return redirect('/login/')
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request, "invalid password")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/recipes/')

        

     return render(request,'login.html')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_Name")
        last_name = request.POST.get("last_Name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user=User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "username taken")
            return redirect('/register/')
        
        
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.error(request, "Account created")

        return redirect('/register/')      
        
    return render(request, 'register.html')


def get_student(request):
    queryset=Student.objects.all()
    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(Q(student_name__icontains=search)|Q(department__department__icontains=search))
    paginator = Paginator(queryset, 25) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request,'student.html',{'queryset': page_obj})

def see_marks(request, student_id):
    queryset = Student_marks.objects.filter(student__student_id__student_id=student_id)
    total_marks = queryset.aggregate(total_marks=Sum('marks'))
    return render(request, 'see_marks.html', {
        'total_marks': total_marks,'queryset':queryset
    })