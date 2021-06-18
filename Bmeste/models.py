from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="static/Bmeste/profile_img", default="None.jpg")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.author_name

class Pieces(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE,)
    title = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.title