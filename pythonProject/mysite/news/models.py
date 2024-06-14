from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Articles(models.Model):
    title = models.CharField('Название', max_length=500)
    summary = models.CharField('Саммари', max_length=500)
    full_text = models.TextField('Статья')
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    banner = models.ImageField(upload_to='media/', default=None, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comments(models.Model):
    post = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(default=timezone.now)
    full_text = models.TextField('Комментарий')

    def __str__(self):
        return 'Комментарий {} by {}'.format(self.full_text, self.author)

    #def get_absolute_url(self):
        #return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
