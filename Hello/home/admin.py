from django.contrib import admin
from home.models import Blog, Author, Entry
from home.models import *
# Register your models here.

class blogregister(admin.ModelAdmin):
    list_display = ['name','tagline']
admin.site.register(Blog,blogregister)
admin.site.register(Author)
admin.site.register(Entry)

admin.site.register(Category)

class productregister(admin.ModelAdmin):
    list_display=['name','price','description']

admin.site.register(Product,productregister)


class userregister(admin.ModelAdmin):
    list_display=['name','email','password']

admin.site.register(UserRegister,userregister)


class contactdisplay(admin.ModelAdmin):
    list_display=['name','email','phone']
admin.site.register(Contact,contactdisplay)



admin.site.register(Ordermodel)