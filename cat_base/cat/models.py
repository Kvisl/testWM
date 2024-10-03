from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Breed(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cat(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    colour = models.CharField(max_length=20)
    age = models.IntegerField()
    description = models.TextField(default='')
    breed = models.ForeignKey(Breed, related_name='cats', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.colour}, {self.age} months'


class Rating(models.Model):
    cat = models.ForeignKey(Cat, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)] , default=1)  # Добавьте значение по умолчанию

    class Meta:
        unique_together = ('cat', 'user')

    def __str__(self):
        return f'{self.user.username} - {self.cat.colour} - {self.score}'
