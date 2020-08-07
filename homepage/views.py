from django.shortcuts import render
from homepage.models import Recipe, Author

def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {'recipes': my_recipes} )

def post_detail(request, post_id):
    my_recipe = Recipe.objects.filter(id=post_id).first()
    return render(request, "post_detail.html", {"post": my_recipe})

def author_detail(request, auth_id):
    current_auth = Author.objects.filter(id=auth_id).first()
    my_recipes = Recipe.objects.all()
    return render(request, "author_detail.html", {"auth": current_auth, "recipes": my_recipes})