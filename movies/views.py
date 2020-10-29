from django.shortcuts import render,redirect
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Movie
from .forms import RewiewForm

class MoviesView(ListView):
    model=Movie
    queryset=Movie.objects.filter(draft=False)
    # template_name="movies/movies.html"


class MovieDetailView(DetailView):
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
