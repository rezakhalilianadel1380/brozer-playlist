from django.db import models
# Create your models here.


class Album(models.Model):
    title_fa = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='songs/cover_image/')
    release_date = models.DateField()
    track_items = models.IntegerField()
    artist_id=models.ForeignKey('song.Artist', on_delete=models.SET_NULL,null=True)
    featuring=models.ManyToManyField('song.Artist',related_name='featuring',blank=True)



    def __str__(self):
        return self.title_fa
    
    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'