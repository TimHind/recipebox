from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from homepage.models import Recipe, Author
from homepage.forms import RecipeForm, AuthorForm, LoginForm


def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {'recipes': my_recipes} )

def post_detail(request, post_id):
    my_recipe = Recipe.objects.filter(id=post_id).first()
    return render(request, "post_detail.html", {"post": my_recipe})

def author_detail(request, auth_id):
    current_auth = Author.objects.filter(id=auth_id).first()
    return render(request, "author_detail.html", {"auth": current_auth})

@login_required
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
                author = request.user.author
            )
            return HttpResponseRedirect(reverse("homepage"))
    
    form = RecipeForm
    return render(request, "generic_form.html", {"form": form})

@login_required
@staff_member_required
def author_form_view(request):
    """ Help from Peter """
    if request.method == "POST":
        form = AuthorForm(request.POST)
        data = form.data
        new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
        new_author = form.save(commit=False)
        new_author.user = new_user
        new_author.save()
        return HttpResponseRedirect(reverse("homepage"))
    
    form = AuthorForm()
    return render(request, "generic_form.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))

    form = LoginForm()
    return render (request,  "generic_form.html", {"form": form} )

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
            Author.objects.create(name=data.get("username"), user=new_user)
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))
    
    form = SignupForm()
    return render(request, "generic_form.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))