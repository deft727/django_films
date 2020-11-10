from django.shortcuts import render,redirect
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Movie,Category,Actor,Ganre
from .forms import RewiewForm
from django.db.models import Q


class GanreYear():
    def get_genres(self):
        return Ganre.objects.all()
    
    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


class MoviesView(GanreYear,ListView):
    model=Movie
    queryset=Movie.objects.filter(draft=False)
    # template_name="movies/movies.html"


class MovieDetailView(GanreYear,DetailView):
    model=Movie
    slug_field="url"


class AddReview(View):
    def post(self,request,pk):
        form=RewiewForm(request.POST)
        movie=Movie.objects.get(id=pk)
        if form.is_valid():
            form=form.save(commit=False)
            if request.POST.get("parent",None):
                form.parent_id=int(request.POST.get("parent"))
            form.movie=movie
            # print(pk,type(pk))
            # print(form.name)
            form.save()
        return redirect(movie.absoluteUrl())


class ActorView(GanreYear,DetailView):
    model=Actor
    template_name='movies/actor.html'
    slug_field="name"

class FilterMoviesView(GanreYear,ListView):
    def get_queryset(self):
        queryset=Movie.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(genres__in=self.request.GET.getlist('genre'))
            )
        return queryset