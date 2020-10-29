from django.db import models
from datetime import date
from django.urls import reverse


class Category(models.Model):
    name= models.CharField('Категория',max_length=150)
    description= models.TextField('Описание')
    url = models.SlugField(max_length=160,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'


class Actor(models.Model):
    name=models.CharField('Имя',max_length=100)
    age=models.PositiveSmallIntegerField('Возраст',default=0)
    description= models.TextField('Описание')
    Image=models.ImageField('Изображение',upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Актеры и режисеры'
        verbose_name_plural='Актеры и режисеры'
    

class Ganre(models.Model):
    name=models.CharField('Имя',max_length=100)
    description= models.TextField('Описание')
    url=models.SlugField(max_length=160,unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Жанр"
        verbose_name_plural="Жанры"


class Movie(models.Model):
    title=models.CharField('Название',max_length=100)
    tagline=models.CharField('Слоган',max_length=100,default='')
    description= models.TextField('Описание')
    poster=models.ImageField('постер',upload_to='movies/')
    year=models.PositiveSmallIntegerField('Дата выхода',default=2019)
    counry=models.CharField('Страна',max_length=30)
    directors=models.ManyToManyField(Actor,verbose_name="режисер",related_name='film_director')
    actors=models.ManyToManyField(Actor,verbose_name="актеры",related_name='film_actor')
    genres=models.ManyToManyField(Ganre,verbose_name='Жанры')
    world_premiere=models.DateField('Премьера в мире',default=date.today)
    budget=models.PositiveIntegerField('Бюджет',default=0,help_text='указать сумму в доллараж')
    fees_in_usa=models.PositiveIntegerField(
        'Сборы в США',default=0,help_text='указать сумму в долларах'
    )
    fess_in_word=models.PositiveIntegerField(
        'Сборы в Мире',default=0,help_text='указать сумму в долларах'
    )
    category=models.ForeignKey(
        Category,verbose_name='Категория',on_delete=models.SET_NULL,null=True
    )
    url=models.SlugField(max_length=160,unique=True)
    draft=models.BooleanField('Черновик',default=False)

    def __str__(self):
        return self.title

    def absoluteUrl(self):
        return reverse ('movie_detail',kwargs={'slug':self.url})

    def get_review(self):
        return self.rewiews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name='Фильм'
        verbose_name_plural='Фильмы'


class MovieShots(models.Model):
    title=models.CharField('Заголовок',max_length=100)
    description= models.TextField('Описание')
    image=models.ImageField('Изображение',upload_to='movie_shots/')
    movie=models.ForeignKey(Movie,verbose_name='Фильм',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='кадр из фильма'
        verbose_name_plural='кадры из фильма'


class RatingStar(models.Model):
    value=models.SmallIntegerField('Значение',default=0)
    def __str__(self):
        return self.value
    
    class Meta:
        verbose_name='звезда рейтинга'
        verbose_name_plural='звезды рейтинга'

class Rating(models.Model):
    ip=models.CharField('IP адрес',max_length=15)
    star=models.ForeignKey(RatingStar,on_delete=models.CASCADE,verbose_name='звезда')
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,verbose_name='фмльм')

    def __str__(self):
        return f"{self.star}-{self.movie}"

    class Meta:
        verbose_name='Рейтинг'
        verbose_name_plural='Рейтинги'

class Rewiews(models.Model):
    email=models.EmailField()
    name=models.CharField('Имя',max_length=100)
    text=models.TextField('Сщщобщение',max_length=5000)
    parent=models.ForeignKey(
        'self',verbose_name='Родитель',on_delete=models.SET_NULL,blank=True,null=True
    )
    movie=models.ForeignKey(Movie,verbose_name='фильм',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}-{self.movie}"

    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'