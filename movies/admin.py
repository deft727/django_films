from django.contrib import admin
from .models import Category,Ganre,Movie,MovieShots,Actor,Rating,RatingStar,Rewiews
from django.utils.safestring import mark_safe
from django import forms


from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description= forms.CharField(label="Описание",widget=CKEditorUploadingWidget())
    class Meta:
        model = Movie
        fields = '__all__'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=("id","name","url")
    list_display_links= ("name",)

class ReviewInline(admin.TabularInline):
    model=Rewiews
    extra=1
    readonly_fields=("name","email")
    
class MovieShotsInline(admin.TabularInline):
    model=MovieShots
    extra=1
    readonly_fields=("get_image",)
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.image.url} width="100 heigh="110"')
    get_image.short_description="Изображение"

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display=("title","category","url","draft")
    list_filter=("category","year")
    search_fields=("title","category__name")
    inlines=[MovieShotsInline,ReviewInline]
    save_on_top=True
    save_as=True
    list_editable=("draft",)
    form=MovieAdminForm
    # fields=(("actors","directors","genres"),)
    readonly_fields=("get_image",)
    fieldsets=(
        (None,{
            "fields":(("title","tagline"),)
        }),
    
        (None,{
                "fields":("description",("poster","get_image"))
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
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.poster.url} width="100 heigh="110"')
        
    get_image.short_description="Постер"

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
    list_display=("name","age","get_image")
    readonly_fields=("get_image",)
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.Image.url} width="50 heigh="60"')
    get_image.short_description="Изображение"

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display=("star","movie","ip")


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display=("title","movie","get_image")

    readonly_fields=("get_image",)
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.image.url} width="50 heigh="60"')
    get_image.short_description="Изображение"


# admin.site.register(Category,CategoryAdmin)
# admin.site.register(Ganre)
# admin.site.register(Movie)
# admin.site.register(MovieShots)
# admin.site.register(Actor)
# admin.site.register(Rating)
admin.site.register(RatingStar)
# admin.site.register(Rewiews)


admin.site.site_title="Django Movies"
admin.site.site_header="Django Movies"
