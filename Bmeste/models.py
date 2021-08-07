from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=200, default="")
    name_rus = models.CharField(max_length=200, default="")
    description = models.TextField(default="")
    img = models.ImageField(upload_to="static/Bmeste/profile_img", default="None.jpg")
    birth = models.IntegerField(default=0)
    death = models.IntegerField(default=0)
    
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.name

class Piece(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,)
    title = models.CharField(max_length=200, default="",)
    title_rus = models.CharField(max_length=200, default="",)
    default_location_lat = models.FloatField(default=0)
    default_location_lng = models.FloatField(default=0)
    default_location_zoom = models.FloatField(default=0)

    def __str__(self):
        return self.title

class Piece_detail(models.Model):
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE,)
    piece_detail = models.CharField(max_length=200, default="",)
    piece_detail_rus = models.CharField(max_length=200, default="",)
    location_lat = models.FloatField(default=0)
    location_lng = models.FloatField(default=0)
    location_heading = models.FloatField(default=0)
    location_pitch = models.FloatField(default=0)
    description = models.TextField(default="")

    def __str__(self):
        return self.piece_detail

class Comment_piece(models.Model):
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_text = models.CharField(max_length=200, default="", null=True)
    comment_user = models.CharField(max_length=20, default="", null=True)
    comment_date = models.DateTimeField('date published', default=timezone.now)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '%s - %s' % (self.comment_user, self.comment_text)