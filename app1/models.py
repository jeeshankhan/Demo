from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from datetime import date,datetime

# Create your models here.
# class Registration(models.Model):
#     First_Name = models.CharField(max_length=100)
#     Middle_Name = models.CharField(max_length=100, blank=True)
#     Last_Name = models.CharField(max_length=100, blank=True)
#     Email = models.EmailField(max_length=254)
#     Password = models.CharField(max_length=20)
#     Degree = models.CharField(max_length=20)
#     Primary_Phone = models.IntegerField(blank=True)
#     Secondary_Phone = models.IntegerField(blank=True)
#     Fax_Number = models.IntegerField(blank=True)
#     Secondary_Email = models.EmailField(max_length=254, blank=True)
#     Department = models.CharField(max_length=100)
#     Institution = models.CharField(max_length=100)
#     Street_Address = models.CharField(max_length=200)
#     City = models.CharField(max_length=50)
#     State_Province = models.CharField(max_length=100)
#     Country = models.CharField(max_length=20)
#     Zip_Postal_Code = models.IntegerField()
#     Areas_of_Specialization = models.CharField(max_length=200)
#     User_Type = models.CharField(max_length=30)
#     def __str__(self):
#         return self.First_Name


class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):

        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an username")
        user = self.model(
               email = self.normalize_email(email),
               username=username,
            
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self , email, username, password):
        user = self.create_user(
        email = self.normalize_email(email),
        password=password,
        username=username,
        )
        user.is_admin =True
        user.is_staff =True
        user.is_superuser=True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):

    First_Name              = models.CharField(max_length=100,blank=True)
    Middle_Name             = models.CharField(max_length=100,blank=True)
    Last_Name               = models.CharField(max_length=100,blank=True)
    username                = models.CharField(max_length=30,unique=True)
    email                   = models.EmailField(verbose_name="email",max_length=254,unique=True)
    Password                = models.CharField(max_length=20)
    Degree                  = models.CharField(max_length=20,blank=True)
    Primary_Phone           = models.CharField(max_length=12, blank=True)
    Secondary_Email         = models.EmailField(max_length=254,blank=True)
    Department              = models.CharField(max_length=100,blank=True)
    Institution             = models.CharField(max_length=100,blank=True)
    Street_Address          = models.CharField(max_length=200,blank=True)
    City                    = models.CharField(max_length=50,blank=True)
    State_Province          = models.CharField(verbose_name="State or Province" ,max_length=100,blank=True)
    Country                 = models.CharField(max_length=20,blank=True)
    Zip_Postal_Code         = models.CharField(max_length=15,blank=True)
    Areas_of_Specialization = models.CharField(max_length=200,blank=True)
    User_Type               = models.CharField(max_length=30,blank=True)
    date_joined             = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    is_reviewer             = models.BooleanField(default=False)
    is_editor               = models.BooleanField(default=False)
    is_publisher            = models.BooleanField(default=False)
    
  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username']
    objects = MyAccountManager()

    def __str__(self):
        return self.email
    def has_perm(self,perm, obj=None):
        return self.is_admin
    def has_module_perms(self,app_lable):
        return True
    
    

# class Person(models.Model):
#     fn = models.CharField(max_length=40)

# class Pet(models.Model):
#     name = models.CharField(max_length=40)

class Manuscript(models.Model):
    a = models.CharField(max_length=20)
    b = models.CharField(max_length=20)
    c = models.CharField(max_length=20)
    d = models.CharField(max_length=20)
    e = models.CharField(max_length=20)
    def __str__(self):
        return self.a
class upload(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    book  = models.FileField(upload_to="book/pdf")
    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
         self.book.delete()
         super().delete(*args,**kwargs)


TYPE_CHOICES = [
    ('Invited Review', 'Invited Review'),
    ('Original Artical', 'Original Artical'),
    ('Book Review', 'Book Review'),
    ('Letter To The Editor','Letter To The Editor'),
]



class manuscript_detail(models.Model):

    manuscript_key      = models.BigAutoField(primary_key=True,unique=True)
    Type_choices        = models.CharField( verbose_name="Type",max_length=25,choices=TYPE_CHOICES)
    title               = models.CharField(max_length=200)
    running_head        = models.CharField(max_length=200)
    abstract            = models.TextField(max_length=500)
    upload_date         = models.DateField(default=datetime.today)
    upload_by           = models.EmailField(max_length=254)
    keyword             = models.CharField(max_length=300,blank=True,null=True)
    cover_letter        = models.FileField(upload_to='pdf/cover_letter/%y/%m/%d')
    def __str__(self):
        return self.manuscript_key
class file_upload(models.Model):
    manuscript_key = models.CharField(max_length=100,blank=True,null=True)
    file_to_upload1 = models.FileField(verbose_name='file_one',upload_to='pdf/articlefile1/%y/%m/%d')
    file_to_upload2 = models.FileField(verbose_name='file_two',upload_to='pdf/articlefile2/%y/%m/%d',blank=True,null=True)
    file_to_upload3 = models.FileField(verbose_name='file_three',upload_to='pdf/articlefile3/%y/%m/%d',blank=True,null=True)
    desingnation_for_file_one = models.CharField(max_length=30)
    desingnation_for_file_one = models.CharField(max_length=30,blank=True,null=True)
    desingnation_for_file_one = models.CharField(max_length=30,blank=True,null=True)
    def __str__(self):
        return self.manuscript_key

class manuscript_attached_author(models.Model):
    manuscript_key = models.CharField(max_length=100,blank=True,null=True)
    first_author = models.EmailField(max_length=254)
    co_author_second  = models.EmailField(max_length=254,null=True,blank=True)
    co_author_third  = models.EmailField(max_length=254,null=True,blank=True)
    institution_with_address_main_author = models.CharField(max_length=200)
    institution_with_address_second_author = models.CharField(max_length=200,null=True,blank=True)
    institution_with_address_first_author = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.manuscript_key

class manuscript_attached_reviewer(models.Model):
    manuscript_key = models.CharField(max_length=100,blank=True,null=True)
    first_reviewer = models.EmailField(max_length=254)
    second_reviewer  = models.EmailField(max_length=254,null=True,blank=True)
    third_reviewer  = models.EmailField(max_length=254,null=True,blank=True)
    institution_with_address_first_reviewer = models.CharField(max_length=200)
    institution_with_address_second_reviewer = models.CharField(max_length=200,null=True,blank=True)
    institution_with_address_third_reviewer = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.manuscript_key
class manuscript_attached_editor(models.Model):
    manuscript_key = models.CharField(max_length=100,blank=True,null=True)
    first_editor = models.EmailField(max_length=254,blank=True,null=True)
    second_editor  = models.EmailField(max_length=254,null=True,blank=True)
    third_editor  = models.EmailField(max_length=254,null=True,blank=True)
    institution_with_address_first_editor = models.CharField(max_length=200,null=True,blank=True)
    institution_with_address_second_editor = models.CharField(max_length=200,null=True,blank=True)
    institution_with_address_third_editor = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.manuscript_key

class manuscript_info(models.Model):
    manuscript_key = models.CharField(max_length=100,blank=True,null=True)
    number_of_figures = models.IntegerField()
    number_of_color_figures = models.IntegerField()
    number_of_tables = models.IntegerField()
    number_of_words = models.IntegerField()
    def __str__(self):
        return self.manuscript_key

class manuscript_upload(models.Model):
    your_email = models.EmailField(max_length=254)
    upload_file = models.FileField(upload_to='article/')
    def __str__(self):
        return self.your_email





