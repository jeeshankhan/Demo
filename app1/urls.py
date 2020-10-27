from django.urls import path
from  app1 import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [

    # path('home',views.script,name='script'),
    path('manu',views.manu,name='manu'),


#####3--------Account----------------[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
    #path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('regs',views.registration_view,name='regs'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('contact',views.contact,name='contact'),


#######-----------Main Menu---------]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

    path('',views.home1,name='home1'),
    path('archives',views.archives,name='archives'),
    path('authorGuidelines',views.authorGuidelines,name='authorGuidelines'),
    path('editorialboard',views.editorialboard,name='editorialboard'),
    path('currentIssue',views.currentIssue,name='currentIssue'),
    path('help',views.help,name='help'),
    #path('submitmanuscript',views.submitmanuscript,name='submitmanuscript'),
    path('step10',views.example_view,name='step10'),


#######---------ManuScript----------]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]][[[[[[[[[[[[[[

    path('step1',views.step1,name='step1'),
    path('step2',views.step2,name='step2'),
    path('step3',views.step3,name='step3'),
    path('step4',views.step4,name='step4'),
    path('step5',views.step5,name='step5'),
    path('step6',views.step6,name='step6'),
    path('step7',views.step7,name='step7'),
    path('step8',views.step8,name='step8'),
    path('dockupload/<int:pk>/',views.delete_upload,name='delete_upload'),
    path('dockupload',views.dockuploadview,name='dockupload'),
    path('manuscriptpdf',views.manuscriptpdf,name='manuscriptpdf'),
    path('pdfprint',views.pdfprint,name='pdfprint'),


    #######--------Home Of Users views---------{{{{]]]]]]]]]{{{{]=======++________-----==}}}}}}}}

    path('home',views.home,name='home'),
    path('author',views.author,name='author'),
    path('editor',views.editor,name='editor'),
    path('publisher',views.publisher,name='publisher'),
    path('reviewer',views.reviewer,name='reviewer'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 