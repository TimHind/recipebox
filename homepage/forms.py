from django import forms
from homepage.models import Recipe, Author

class RecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(max_length=50)
    timereq = forms.CharField(max_length=50)
    #author = forms.ModelChoiceField(queryset=Author.objects.all())

class AuthorForm(forms.ModelForm):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Author
        fields = ["name", "bio"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
