from django.db import models

# Create your models here.
class Author(models.Model):
    #The Author Model stores information about book authors
  name = models.CharField(max_length=300)

  def __str__(self):
      return self.name
  


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    
