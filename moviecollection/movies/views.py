from django.shortcuts import render,redirect,get_object_or_404
from .models import Category,MovieDetails,CommentSection
from django.urls import reverse
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.contrib import messages,auth
from .forms import CommentForm
from django.db.models import Sum,Count


# Create your views here.

def allMoviedetails(request, c_slug=None):
    c_page=None
    movie_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        movie_list= MovieDetails.objects.all().filter(category=c_page)
    else:
        movie_list= MovieDetails.objects.all()
    paginator=Paginator(movie_list,50)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        movies = paginator.page(page)
    except(EmptyPage, InvalidPage):
        movies = Paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'category': c_page, 'moviedetails': movies, 'c_slug': c_slug})

def detailedOfMovie(request, c_slug, movie_slug):
    try:
        details = MovieDetails.objects.get(category__slug=c_slug,slug=movie_slug)
        comments = details.comments.all()

        if request.method == 'POST':
            comment_Box = request.POST.get('comment', )
            comment = CommentSection(movie_id=details, user=request.user.username, message=comment_Box)
            comment.save()
            # sum_of=CommentSection.objects.filter(movie_id=details).aggregate(Sum(movie_id))
            return redirect('movies:detailedOfMovie', c_slug=c_slug, movie_slug=movie_slug)
    except Exception as e:
        raise e
    return render(request,'details.html', {'details': details,'comments':comments})


