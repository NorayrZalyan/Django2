from django.db import models

# Create your models here.




# header
class h_Header(models.Model):
    logo = models.ImageField('page logo' , upload_to='media')
    name = models.CharField('page name' , max_length=20)
    bgimg = models.ImageField('img' , upload_to='media')
    tel = models.CharField('tel' , max_length=20)
    email = models.CharField('email' , max_length=70)
    address = models.CharField('address' , max_length=100)
    have_text = models.TextField('1 havet text' , default=" ")
    def __str__(self):
        return self.name
class h_what_do_we_have(models.Model):
    number = models.IntegerField('number' , default=1)
    text = models.TextField('text')
    def __int__(self):
        return self.number
# end header






# about
class About(models.Model):
    name = models.CharField('name' , max_length=30 )
    p = models.TextField('text')
    img = models.ImageField('img' , upload_to='media')
    def __str__(self):
        return self.name



# Classes
class Classes(models.Model):
    img = models.ImageField('img' , upload_to='media')
    classes_name = models.CharField('Classes name' , max_length=50)

    def __str__(self):
        return self.classes_name



# Blog
class Blog(models.Model):
    ing = models.ImageField('img' , upload_to='media')
    date = models.DateField('date')
    p = models.CharField('paragraf' , max_length=35)
    text = models.TextField('')
    def __int__(self):
        return self.date
    


# students
class students(models.Model):
    img = models.ImageField('img' ,upload_to='media')
    name = models.CharField('students name' , max_length=20)
    about = models.TextField('')
    def __str__(self):
        return self.name


# Call Back
class footer(models.Model):
    name = models.CharField('img name' , max_length=20 , default='img')
    img = models.ImageField('img' , upload_to='media')
    facebook = models.CharField('facebook link' , max_length=100 )
    instagram = models.CharField('instagram link' , max_length=100 )
    youtube = models.CharField('youtube link' , max_length=100 )
    def __str__(self):
        return self.name