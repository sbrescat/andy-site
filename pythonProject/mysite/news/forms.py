from .models import Articles, Comments
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django import forms

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = {'title', 'summary', 'full_text', 'date', 'banner'}

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'

            }),
            "summary": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Саммари'

            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',
                'rows': 5
            }),
        }


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = {'date', 'full_text'}

        widgets = {

            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст комментария'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата комментария'
            }),

        }
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)