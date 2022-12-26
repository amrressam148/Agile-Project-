from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'aiesec/signUp/SignUpForm.html')

def login(request):
    return render(request,"aiesec/Login/Login.html")


def submit(request):
    #fname=request.GET['Fname']
    #lname=request.GET['Lname']
    #email=request.GET['Mail']
    # password = request.GET['password']
    # phone = request.GET['PhoneNumber']
    # email = request.GET['Mail']
    gender = request.GET['Gender']
    # role = request.GET['Role']
    # country = request.GET['Country']

    return render(request,"aiesec/SubmitSignUp.html")





