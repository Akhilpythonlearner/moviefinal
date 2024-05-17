from django.shortcuts import render
from movies.models import MovieDetails
from django.db.models import Q

# Create your views here.

def searchResult(request):
    movie_details = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        movie_details =MovieDetails.objects.all().filter(Q(title__contains=query) | Q(description__contains=query))
    return render(request, 'search.html', {'query': query,'movie_details':movie_details})
