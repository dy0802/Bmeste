from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="static/Bmeste/profile_img", default="None.jpg")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.author_name

class Piece(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE,)
    title = models.CharField(max_length=200, default="")
    default_location_lat = models.FloatField(default=0)
    default_location_lng = models.FloatField(default=0)

    def __str__(self):
        return self.title

class Piece_detail(models.Model):
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE,)
    piece_detail = models.CharField(max_length=200, default="")
    location_lat = models.FloatField(default=0)
    location_lng = models.FloatField(default=0)
    description = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.piece_detail
