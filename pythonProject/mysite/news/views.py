from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormMixin
from .forms import SearchForm
from .models import Articles, Comments
from .forms import ArticlesForm, CommentsForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView


# Create your views here.
class ArticleListView(ListView):
    model = Articles
    template_name = 'news/news_home.html'
    context_object_name = 'articles'
    ordering = '-date'  # По умолчанию сортируем по убыванию даты добавления

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', self.ordering)  # Получаем значение ordering из GET-параметров
        return queryset.order_by(ordering)  # Применяем сортировку к queryset

class NewsDetailView(DetailView, FormMixin):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'
    form_class = CommentsForm

    def get_success_url(self):
        return reverse_lazy('news_detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.post_id = self.get_object().id
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class NewsUpdateView(UpdateView):
    model = Articles
    form_class = ArticlesForm
    template_name = 'news/news_update.html'
    success_url = reverse_lazy('news')


class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news_delete.html'
    success_url = '/news/'


@login_required(login_url='users:login')
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('news')
        else:
            error = 'Ошибка'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)


class CommentCreateView(CreateView):
    model = Comments
    form_class = CommentsForm
    template_name = 'news/add_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('news')


class CommentDeleteView(DeleteView):
    model = Comments
    template_name = 'news/delete_comment.html'
    success_url = reverse_lazy('news')


#@login_required(login_url='users:login')
#def delete(request, id):
#post = Articles.objects.get(id=id)
#post.delete()
#return redirect('news')

class NewsSearchView(ListView):
    model = Articles
    template_name = 'news/search.html'
    context_object_name = 'articles'
    form_class = SearchForm

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context
