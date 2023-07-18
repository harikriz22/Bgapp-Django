from django.db import models

# Create your models here.

from django.contrib.auth.models import User
# class Customer(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     date_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name


class UsrProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=300, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    proimg = models.ImageField(null=True, blank=True, upload_to='profiles/')

    def __str__(self):
        return self.user.username


class Newsfeed(models.Model):
    usr = models.ManyToManyField(
        User, related_name='newsfeed')
    name = models.CharField(max_length=500)
    newsimg = models.ImageField(upload_to='news/')
    datez = models.DateField(auto_now=True)
    des = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class Categorie(models.Model):
    name = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name


class Productss(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    breif = models.CharField(null=True, max_length=400)
    description = models.CharField(max_length=2000, null=True)
    price = models.IntegerField(null=True)
    Category = models.ForeignKey(
        Categorie, null=True, on_delete=models.CASCADE, related_name='categorie')

    def __str__(self):
        return self.name


# class Order(models.Model):
#     product = models.ForeignKey(Productss, null=True, on_delete=models.SET_NULL)
#     customer = models.ForeignKey(
#         User, null=True, on_delete=models.SET_NULL)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, default='PENDING')

#     def __str__(self):
#         return self.name
