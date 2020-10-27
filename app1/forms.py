from django import forms
from django.contrib.auth.forms import UserCreationForm,authenticate
from  .models import Account,upload,manuscript_detail,manuscript_info,manuscript_attached_reviewer,manuscript_attached_editor,manuscript_attached_author,file_upload,manuscript_upload
from .models import dockupload,reviewer_comment
from django.db import models
from django.forms import ModelForm
from datetime import date,time

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254,help_text='Email Required ')
    class Meta:
        model = Account
        fields = ("First_Name","Middle_Name","Last_Name","email","username","password1","password2",
        "Primary_Phone","Secondary_Email","Degree","Department",
        "Institution","Areas_of_Specialization","Zip_Postal_Code","Street_Address",
        "City","State_Province","Country","User_Type",)
class AccountAuthenticationForm(forms.ModelForm):
    password= forms.CharField(label='Password',widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields =('email','password')
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email,password=password):
                raise forms.ValidationError("Invalid login")


# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Person

# class PetForm(forms.ModelForm):
#     class Meta:
#         model = Pet
#         exclude = ('owner',)

# class manuscriptForm1(forms.ModelForm):
#     class Meta:
#         model = Manuscript
#         fields = [
#             'a','b','c'
#         ]
# class manuscriptForm2(forms.ModelForm):
#     class Meta:
#         model = Manuscript
#         fields = [
#             'd','e'
#         ]
# class example(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length=254)

class example(forms.Form):
    a = forms.CharField(max_length=20)
    b = forms.CharField(max_length=20)
    c = forms.CharField(max_length=20)
    d = forms.CharField(max_length=20)
    e = forms.CharField(max_length=20)
    
class upload_form(forms.ModelForm):
    class Meta:
        model = upload
        fields =('author','book',)

class upload_form1(forms.ModelForm):
    class Meta:
        model = upload
        fields =('title',)
class manuscript_detail_form(forms.ModelForm):
    class Meta:
        model = manuscript_detail
        fields =('Type_choices','title','running_head','abstract','upload_by','keyword','cover_letter',)



class file_upload_form(forms.ModelForm):
    class Meta:
        model = file_upload
        fields =('manuscript_key','file_to_upload1','file_to_upload2','file_to_upload3','desingnation_for_file_one','desingnation_for_file_one','desingnation_for_file_one',)


class manuscript_attached_author_form(forms.ModelForm):
    class Meta:
        model = manuscript_attached_author
        fields =('manuscript_key','first_author','co_author_second','co_author_third','institution_with_address_main_author','institution_with_address_second_author' ,'institution_with_address_first_author',) 

class manuscript_attached_reviewer_form(forms.ModelForm):
    class Meta:
        model = manuscript_attached_reviewer
        fields =('manuscript_key','first_reviewer','second_reviewer','third_reviewer','institution_with_address_first_reviewer','institution_with_address_second_reviewer','institution_with_address_third_reviewer',) 
   
class manuscript_attached_editor_form(forms.ModelForm):
    class Meta:
        model = manuscript_attached_editor
        fields =('manuscript_key','first_editor','second_editor','third_editor', 'institution_with_address_first_editor','institution_with_address_second_editor','institution_with_address_third_editor',)


class manuscript_info_form(forms.ModelForm):
    class Meta:
        model = manuscript_info
        fields =('manuscript_key','number_of_figures','number_of_color_figures','number_of_tables','number_of_words',)


class manuscript_upload_form(forms.ModelForm):
    class Meta:
        fields = ('email','upload_file',) 
class dockuploadform(forms.ModelForm):
   
    class Meta:
        model = dockupload
        fields = ('your_email','ubload_file')

class reviewer_comment_form(forms.ModelForm):
   
    class Meta:
        model = reviewer_comment
        fields = ('manuscript_key','email','file_upload')

    

