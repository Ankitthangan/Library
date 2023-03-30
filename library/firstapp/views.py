from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from .models import Book

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.method == "POST":
        print(request.POST)
        Bid = request.POST.get("book_id")
        name = request.POST.get("book_name")
        price = request.POST.get("price")
        author = request.POST.get("author")
        qty = request.POST.get("qty")
        published = request.POST.get("is_pub")
        # print(name, price,author, qty, published)
        if published == "yes":
            published = True
        else:
            published = False
        if not Bid:
            Book.objects.create(name= name, price= price, author= author, qty= qty, is_published= published)
        
        else:
            book_obj = Book.objects.get(id = Bid)
            book_obj.name = name
            book_obj.price = price
            book_obj.author = author
            book_obj.qty = qty
            book_obj.is_published = published
            book_obj.save()
        

        return redirect("home_page")
        # return HttpResponse("Success")
    if request.method == "GET":
        # return render(request, "home.html", {"name": "Ankit"})
        return render(request, "home.html", context= {"all_books": Book.objects.all()})

@login_required
def all_active_books(request):
    return render(request , "show_books.html", {"books": Book.objects.filter(is_active = True), "active" : True})

@login_required
def update_books(request, pk): # pk and id are tyhe both the same things
    book_obj = Book.objects.get(id = pk)
    return render(request, "home.html", context= {"single_book": book_obj})


@login_required
def delete_book(request, pk):
    book_obj = Book.objects.get(id = pk)
    book_obj.delete()
    return redirect("all_active_books")

@login_required
def soft_delete(request, pk):
    book_obj = Book.objects.get(id = pk)
    book_obj.is_active = False
    book_obj.save()
    return redirect("all_active_books")


@login_required
def show_inactive_book(request):
    return render(request, "show_books.html",{"books" : Book.objects.filter(is_active = False), "inactive" : True})


@login_required
def restore_book(request, id):
    book_obj = Book.objects.get(id = id)
    book_obj.is_active = True
    book_obj.save()
    return redirect("all_active_books")








# class based views  

from django.views import View

class BookView(View):

    def get(self, request):
        return HttpResponse("in  get method")

    def post(self, request):
        return HttpResponse("in post method")
    
    def put(self, request):
        return HttpResponse("in put method")
    
    def delete(self, request):
        return HttpResponse("in delete method")






# CRUD operations 

from django.views.generic.edit import CreateView

class BookCretae(CreateView):
    model = Book
    fields = '__all__'
    success_url = "/cbv/"   # manditory 


from django.views.generic.list import ListView


class BookRetrive(ListView):
    model = Book
    # queryset = Book.objects.filter(is_active = 1)


from django.views.generic.detail import DetailView
class BookDetail(DetailView):
    model = Book
    # queryset = Book.objects.filter(is_active = 1)  # modified query set




from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    # success_url = '/cbv-list/'
    success_url = reverse_lazy("BookRetrive")


# template view 
from django.views.generic import TemplateView

class Template(TemplateView):
    
    template_name = "home.html"
    
    


# 33 pending


## paginations ##

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def index(request):
    book_list = Book.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(book_list, 3)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'index.html', { 'books': books })