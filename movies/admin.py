from django.contrib import admin
from .models import Category,Ganre,Movie,MovieShots,Actor,Rating,RatingStar,Rewiews

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=("id","name","url")
    list_display_links= ("name",)

class ReviewInline(admin.TabularInline):
    model=Rewiews
    extra=1
    readonly_fields=("name","email")
    

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display=("title","category","url","draft")
    list_filter=("category","year")
    search_fields=("title","category__name")
    inlines=[ReviewInline]
    save_on_top=True
    save_as=True
    list_editable=("draft",)
    # fields=(("actors","directors","genres"),)
    fieldsets=(
        (None,{
            "fields":(("title","tagline"),)
        }),
    
        (None,{
                "fields":(("description","poster"),)
            }),
        
        (None,{
                "fields":(("year","world_premiere","counry"),)
            }),
        
        ("Actors",{
                "classes":("collapse",),
                "fields":(("actors","directors","genres","category"),)
            }),
        
        (None,{
                "fields":(("budget","fees_in_usa","fess_in_word"),)
            }),
        
        ("Options",{
                "fields":(("url","draft"),)
            }),
    )

@admin.register(Rewiews)
class ReviewAdmin(admin.ModelAdmin):
    list_display=("name","email","parent","movie","id")
    readonly_fields=("name","email")
    # list_display_links=("movie",)


@admin.register(Ganre)
class GenreAdmin(admin.ModelAdmin):
    list_display=("name","url")
  

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display=("name","age")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display=("ip",)


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display=("title","movie")


# admin.site.register(Category,CategoryAdmin)
# admin.site.register(Ganre)
# admin.site.register(Movie)
# admin.site.register(MovieShots)
# admin.site.register(Actor)
# admin.site.register(Rating)
admin.site.register(RatingStar)
# admin.site.register(Rewiews)