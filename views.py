from django.shortcuts import render, redirect  # Added redirect import
from .models import *  # Make sure the model is correctly imported
from django.contrib.auth.models import User
from django.contrib import messages


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



        

  

