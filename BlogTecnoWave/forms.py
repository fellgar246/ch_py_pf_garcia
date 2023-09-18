from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Agrega un título'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Agrega un tag'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id': 'user_id', 'type': 'hidden' }),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Agrega una breve entrada del texto de tu posteo'}),
        }

class PostEditForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ('title', 'title_tag','body', 'snippet', 'header_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Agrega un título'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Agrega un tag'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Agrega una breve entrada del texto de tu posteo'}),
        }

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu nombre de usuario'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu comentario aquí'}),
        }