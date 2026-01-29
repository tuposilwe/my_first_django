from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.name}"

class PriorityChoices(models.IntegerChoices):
    LOW = 1, 'LOW'
    MEDIUM= 2, 'Medium'
    HIGH = 3, 'High'

class App(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    is_verified = models.BooleanField(default=False)
    uploadDate = models.DateField(null=True,blank=True)
    priority = models.IntegerField(choices=PriorityChoices.choices,null=True,blank=True)

    owner = models.ForeignKey(Person,
                               on_delete=models.CASCADE,
                               related_name='apps',
                               blank=True,
                               null=True
                               )

    def __str__(self):
        return f"{self.id} - {self.title}"


# Create your models here.
