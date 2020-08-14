from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import Recipe, Author
from homepage.forms import AddRecipeForm, AddAuthorForm


def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {'recipes': my_recipes} )

def post_detail(request, post_id):
    my_recipe = Recipe.objects.filter(id=post_id).first()
    return render(request, "post_detail.html", {"post": my_recipe})

def author_detail(request, auth_id):
    current_auth = Author.objects.filter(id=auth_id).first()
    my_recipes = Recipe.objects.all()
    return render(request, "author_detail.html", {"auth": current_auth})

def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title = data.get('title'),
                description = data.get('description'),
                timereq = data.get('timereq'),
                instructions = data.get('instructions'),
                author = data.get('author')
            )
            return HttpResponseRedirect(reverse("homepage"))
    
    form = AddRecipeForm
    return render(request, "generic_form.html", {"form": form})

def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))
    
    form = AddAuthorForm()
    return render(request, "generic_form.html", {"form": form})

