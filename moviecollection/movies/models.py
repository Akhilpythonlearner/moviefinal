from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('movies:movie_details_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class MovieDetails(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=150, unique=True)
    poster = models.ImageField(upload_to='moviedetails', blank=True)
    description = models.CharField(max_length=250)
    release_date = models.DateField()
    actors = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trailer_Link = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('movies:detailedOfMovie', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ('title',)
        verbose_name = 'MovieDetail'
        verbose_name_plural = 'MovieDetails'


class CommentSection(models.Model):
    user = models.CharField(max_length=250, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=250, blank=False)
    movie_id = models.ForeignKey(MovieDetails, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.user

    class Meta:
        ordering = ('user',)
        verbose_name = 'CommentSection'
        verbose_name_plural = 'CommentSections'