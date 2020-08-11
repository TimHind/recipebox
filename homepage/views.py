from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import Recipe, Author
from homepage.forms import RecipeForm, AuthorForm


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

def recipe_form_view(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
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
    
    form = RecipeForm
    return render(request, "generic_form.html", {"form": form})

def author_form_view(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))
    
    form = AuthorForm()
    return render(request, "generic_form.html", {"form": form})

