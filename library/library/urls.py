"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from firstapp import views

from Users import views as user_view 

from django.contrib.auth import views as auth_viws

class NewLoginView(auth_viws.LoginView):
    template_name = "login.html"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('welcome/', views.home, name= "home_page"),

    path('show-books/', views.all_active_books, name= "all_active_books"),

    path('update/<int:pk>', views.update_books, name= "update_book"),

    path('delete-book/<int:pk>/', views.delete_book, name= "delete_book"),

    path('soft-delete/<int:pk>', views.soft_delete, name= "soft_delete"),

    path('inactive-books/', views.show_inactive_book, name= "inactive_books"),

    path('restore-books/<int:id>/', views.restore_book, name= "restrore_book"),


    ## path for user views

    path('register/', user_view.register_requset, name= "register"),

    path('login/', user_view.login_request, name= "login_request"),

    path('logout/', user_view.logout_request, name="logout_request"),



    # class based views 
    
    path('bookview/', views.BookView.as_view(), name= "bookview"),
    path('cbv/', views.BookCretae.as_view(), name="BookCretae"), 
    path('cbv-list/', views.BookRetrive.as_view(), name= "BookRetrive"),
    path('cbv-list/<int:pk>/', views.BookDetail.as_view(), name= 'BookDetail'),
    path('update/<int:pk>/', views.BookUpdate.as_view(), name='BookUpdate'),

    #template view url
    path('template/', views.Template.as_view(), name= 'Template'),

    # login url for class based view

    path('login-cbv/', user_view.LoginPageView.as_view(), name= "LoginPageView"),

    # short cut for login def class in the same file above 
    path('new-login/', NewLoginView.as_view(), name = "NewLoginView"),  # to get complerte view of form do 1 change :-> login_form relace by form 



    #pagination url

    path('index/', views.index, name= 'index'),




]
