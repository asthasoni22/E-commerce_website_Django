from datetime import date

from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return str(self.name)


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return str(self.name)


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return str(self.headline)

class Category(models.Model):
    categotyname = models.CharField(max_length = 200)
    img  =  models.ImageField(upload_to = 'category')

    def __str__(self) :
        return str(self.categoryname)

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    img=models.ImageField(upload_to='product')
    price = models.IntegerField()
    description = models.TextField()
    quantity=models.IntegerField()


class UserRegister(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    message=models.TextField()

class Ordermodel(models.Model):
    productid=models.CharField(max_length=200)
    productqty=models.CharField(max_length=200)
    userId = models.CharField(max_length=200)
    userName = models.CharField(max_length=200)
    userEmail = models.EmailField()
    userContact = models.IntegerField()
    address = models.CharField(max_length=200)
    orderAmount = models.IntegerField()
    paymentMethod = models.CharField(max_length=200)
    transactionId = models.CharField(max_length=200)
    orderDate = models.DateTimeField(auto_created=True,auto_now=True)

    def __str__(self):
        return str(self.userName)
