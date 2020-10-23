from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import login ,authenticate,logout
from .forms import RegistrationForm ,AccountAuthenticationForm,example,upload_form,upload_form1,manuscript_detail_form,manuscript_upload_form
from .forms import file_upload_form,manuscript_attached_author_form,manuscript_attached_editor_form,manuscript_attached_reviewer_form,manuscript_info_form
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.conf.urls.static import static
from .models import upload,manuscript_detail
import datetime
import os

def manu(request):
    return render(request,'menuscriptpages/manuscript.html')







###########--------Main menu views -----{{{{{{{{{[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]}}}}}}}}}
def home1(request):
    return render(request,'pages/home1.html')
    
def index(request):
    return render(request,'index.html')
def archives(request):
    return render(request,'pages/Archives.html') 
def authorGuidelines(request):
    return render(request,'pages/Author_Guidelines.html')
def editorialboard(request):
    return render(request,'pages/Editorial_Board.html')
def help(request):
    return render(request,'pages/help.html') 
def currentIssue(request):
    return render(request,'pages/currentIssue.html')


#################---------login views----------{{{{{}}}}}}}{{{{{{{{{{[[[[[[[]]]]]]]}}}}}}}}}}
def about(request):
    
    return render(request,'login/About.html') 
def contact(request):
    return render(request,'pages/home1.html')
def registration_view(request):
    context ={}
    if request.POST:
        form  = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email                   = form.cleaned_data.get('email')
            raw_password            = form.cleaned_data.get('password1')
            first_name              = form.cleaned_data.get('First_Name')
            Middle_Name             = form.cleaned_data.get('Middle_Name')
            Last_Name               = form.cleaned_data.get('Last_Name')
            Degree                  = form.cleaned_data.get('Degree')
            Primary_Phone           = form.cleaned_data.get('Primary_Phone')
            Secondary_Email         = form.cleaned_data.get('Secondary_Email')
            Department              = form.cleaned_data.get('Department') 
            Institution             = form.cleaned_data.get('Institution')
            Street_Address          = form.cleaned_data.get('Street_Address')          
            City                    = form.cleaned_data.get('City')
            State_Province          = form.cleaned_data.get('State_Province')           
            Country                 = form.cleaned_data.get('Country')
            Zip_Postal_Code         = form.cleaned_data.get('Zip_Postal_Code') 
            Areas_of_Specialization = form.cleaned_data.get('Areas_of_Specialization')            
            User_Type               = form.cleaned_data.get('User_Type')
            account                 = authenticate(email=email,password=raw_password,First_name=first_name,Middle_Name = Middle_Name,Last_Name =Last_Name,Degree =Degree,Primary_Phone =Primary_Phone,
            Secondary_Email         = Secondary_Email,
            Department              = Department,
            Institution             = Institution,
            Street_Address          = Street_Address,
            City                    = City,
            State_Province          = State_Province,
            Country                 = Country,
            Zip_Postal_Code         = Zip_Postal_Code,
            Areas_of_Specialization = Areas_of_Specialization,
            User_Type               = User_Type,
            )
            

            login(request,account)
            return redirect('home1')
        else:
            context['registration_form']= form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request,'login/regs.html',context)


def logout_view(request):
    logout(request)
    return redirect('home1')


def login_view(request):
    try:
        request.session['name'] = request.POST['email']

    except KeyError:
        pass
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home1')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid:
            email =request.POST['email']
            password =request.POST['password']
            user = authenticate(email = email,password=password)
            if user:
                login(request,user)
                return redirect("home1")
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request,'login/login.html',context)



# def step1(request):
    
#     if request.method =='POST':
#         if form.is_valid:
#             request.session['aa'] = request.POST['a']
#             return HttpResponseRedirect(reverse('step2'))
#     return render(request,'login/step2.html')


# def step2(request):
#     form = manuscriptForm2(request.POST or None)
#     if request.method =='POST':
#         if form.is_valid:
#             request.session['b'] = request.cleaned_data['a']
#             return HttpResponseRedirect(reverse('step3'))
#     return render(request,'step1.html',{'form':form})
# def submitmanuscript(request):
#     if request.method == 'POST':
#         request.session['sf'] =  request.POST['title']
#         uf = upload_form1(request.POST,request.FILES)
#         if uf.is_valid:
#             new_upload = uf.save()
#             return redirect('step1')
#     else:
#         uf = upload_form1()
#     return render(request,'manuscriptpages/home.html',{'form':uf})


# def step3(request):
#     print(request.session['a'] + " " +request.session['b'])
#     return request.session['a'] + " " +request.session['b']


def example_view(request):
    if request.method =='POST':
        exampleform = example(request.POST)
        if exampleform.is_valid():
            a=exampleform.cleaned_data['a']
            b=exampleform.cleaned_data['b']
            c=exampleform.cleaned_data['c']
            d=exampleform.cleaned_data['d']
            e=exampleform.cleaned_data['e']
            request.session['1'] = a
            request.session['2'] = b
            request.session['3'] = c
            request.session['4'] = d
            request.session['5'] = e
            return HttpResponseRedirect('about')
    else:
        exampleform = example()
    return  render(request, 'login/step1.html', {'form': exampleform})




# def step1(request):
    
#     if request.method =='POST':
#         f = request.FILES['document']
#         fs = FileSystemStorage()
#         fs.save(f.name,f)
#         print(f.name)
#         return HttpResponseRedirect('step2')
    # return render(request,'manuscriptpages/step1.html')
# def step2(request):
#     if request.method =='POST':
#         return HttpResponseRedirect('step3')
#     return render(request,'manuscriptpages/step2.html')


##############--------manuscript views -----------{{{{{{{{{{{[[[[[[[[[[[[]]]]]]]]]]]]}}}}}}}}}}}
def step1(request):
    manuscript_details = manuscript_detail.objects.all()
    if request.method =='POST':
        formmanuscript = manuscript_detail_form(request.POST,request.FILES)
        if formmanuscript.is_valid():
            formmanuscript.save()
        return HttpResponseRedirect('step2')
    else:
        formmanuscript = manuscript_detail_form()
    return render(request,'manuscriptpages/step1.html',{'formmanuscript':formmanuscript,'manuscript_details':manuscript_details})

def step2(request):
    if request.method =='POST':
        form  = file_upload_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('step3')
    else:
        form = file_upload_form()
    return render(request,'manuscriptpages/step2.html',{'form':form})

def step3(request):
    if request.method =='POST':
        form  = manuscript_info_form(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('step4')
    else:
        form = manuscript_info_form()
    return render(request,'manuscriptpages/step3.html',{'form':form})

def step4(request):
    if request.method =='POST':
        form  =manuscript_attached_author_form(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('step5')
    else:
        form = manuscript_attached_author_form()
    return render(request,'manuscriptpages/step4.html',{'form':form})


def step5(request):
    if request.method =='POST':
        form  = manuscript_attached_editor_form(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('step6')
    else:
        form = manuscript_attached_editor_form()
    return render(request,'manuscriptpages/step5.html',{'form':form})


def step6(request):
    if request.method =='POST':
        form  = manuscript_attached_reviewer_form(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('step7')
    else:
        form = manuscript_attached_reviewer_form()
    return render(request,'manuscriptpages/step6.html',{'form':form})
def step7(request):
    if request.method =='POST':
        return HttpResponseRedirect('step8')
    return render(request,'manuscriptpages/step7.html')
def step8(request):
    if request.method =='POST':
        return HttpResponseRedirect('step1')
    return render(request,'manuscriptpages/step8.html')




def manuscript_upload_view(request):
    if request.method == 'POST':
        form = manuscript_upload_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('author')
    else:
        form = manuscript_upload_form()
    return render(request,'manuscriptpages/manuscripyt_upload.html',{'form':form})





#+++++++++++++++++++==========file uploads steps================___----

# def step1(request):
#     if request.method == 'POST':
#         a = upload.objects.get(title = request.session['sf'])
#         uf = upload_form(request.POST,request.FILES,instance=a)
#         if uf.is_valid:
#             uf.save()
#             return redirect('step2')
#     else:
#         uf = upload_form()
  
#     return render(request,'manuscriptpages/step1.html',{'form':uf})


# def step2(request):
#     uploads = upload.objects.all()
#     return render(request,'manuscriptpages/step2.html',{'uploads':uploads})


# ################# pdf file deletion def --------------{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}
def delete_upload(request,pk):
    if request.method =='POST':
        book  = upload.objects.get(pk=pk) 
        book.delete()
    return redirect('step2')



# def script(request):
#     if request.method == 'POST':
#         request.session['sf'] =  request.POST['title']
#         uf = upload_form1(request.POST,request.FILES)
#         #  request.session['fs']= request.FILES['book']
#         if uf.is_valid:
#             newa = uf.save()
#             return redirect('step1')
#     else:
#         uf = upload_form1()
#     return render(request,'manuscriptpages/home.html',{'form':uf})





#######--------Home Of Users views---------{{{{]]]]]]]]]{{{{]=======++________-----==}}}}}}}}
def home(request):
    return render(request,'manuscriptpages/home.html')

def author(request):
    return render(request,'account/author.html')

def editor(request):
    return render(request,'account/editor.html')

def publisher(request):
    return render(request,'account/publisher.html')

def reviewer(request):
    return render(request,'account/reviewer.html')

