from django.db import models
from album.models import Album

class Song(models.Model):
    title_fa = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    release_date = models.DateField()
    album_id = models.ForeignKey(Album, on_delete=models.SET_NULL,null=True,blank=True)
    genre_id = models.ManyToManyField('Genre')
    category_id = models.ManyToManyField('Category')
    file_path= models.FileField(upload_to='songs/')
    lyrics_en = models.TextField(null=True,blank=True)
    lyrics_fa = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to='songs/covers/')

    def __str__(self):
        return f'{self.title_en} by {self.artist_id.stage_name_en}'

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'


class Artist(models.Model):
    firstname_fa = models.CharField(max_length=100,blank=True)
    lastname_fa = models.CharField(max_length=100,blank=True)
    firstname_en = models.CharField(max_length=100,blank=True)
    lastname_en = models.CharField(max_length=100,blank=True)
    date_brith = models.DateField(null=True,blank=True)
    stage_name_fa = models.CharField(max_length=100)
    stage_name_en = models.CharField(max_length=100)
    career_start_date = models.DateField()
    nationality =models.ForeignKey('Country',on_delete=models.SET_NULL,null=True)
    bio_fa = models.TextField()
    bio_en = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.firstname_fa}'

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

class Genre(models.Model):
    title_fa = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    brief= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title_fa}'

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

class Category(models.Model):
    title_fa = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title_fa}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Country(models.Model):
    name_fa = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title_fa}'

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'