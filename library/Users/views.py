from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, authenticate, logout

# Create your views here.


from Users.forms import NewUserForm
def register_requset(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            print("in if condition")
            user = form.save()
            login(request, user)
            return redirect("home_page")
    form = NewUserForm()
    return render(request, "registration.html", {"registration_form": form})



def login_request(request):
    if request.method == "POST":
        print(request.POST)
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                print("in login methoid")
                return redirect("home_page")
            else:
                return redirect("register")
        else:
            return redirect("register")
    form = AuthenticationForm()
    return render(request, "login.html", {"login_form" : form})



def logout_request(request):
    logout(request)
    return redirect("login_request")



# class based login view
from django.views.generic import View

class LoginPageView(View):
    template_name = "login.html"
    form_class = AuthenticationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context = {"login_form" : form})

    def post(self, request):
        # form = AuthenticationForm(request, data = request.POST)
        form = self.form_class(data = request.POST)

        if form.is_valid():
            user = authenticate(username= form.cleaned_data["username"],
                                password= form.cleaned_data["password"])

            if user:
                login(request, user)
                return redirect("home_page")
        return render(request, self.template_name, context= {"login_form" : form})