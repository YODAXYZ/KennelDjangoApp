from django.db import models


class Animal(models.Model):
    nickname = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    receipt_date = models.DateField()
    TYPE_OF_ANIMAL = [
        ('C', 'Cat'),
        ('D', 'Dog'),
        ('R', 'Reptile'),
        ('E', 'Else'),
    ]
    type = models.CharField(max_length=2, choices=TYPE_OF_ANIMAL)
    sterilized = models.BooleanField(blank=True)
    image = models.ImageField(upload_to='img/', blank=True)

    def __str__(self):
        return f'{self.nickname} \n'