from django.shortcuts import render,redirect
# from .forms import ContactForm
from django.contrib import messages
from .models import Contact,AboutMe,Education,Skill,Projects,Link,Name_Details,Work_Known


# Create your views here.
def index(request):
    about = getabout_me()
    edcn = get_education_Details()
    skills = get_skills()
    projects = get_projects()
    links = get_links()
    name_details = get_name_details()
    work_details = get_work_known()
    return render(request,'index.html',{'about':about,'edcn':edcn,'skills':skills,'projects':projects,'links':links,'name_details':name_details,'work_details':work_details})

def contacts(request):
    if request.method == 'POST':
        
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        reg = Contact.objects.create(name=name, email=email,desc=desc)
        reg.save()
        messages.success(request, 'Your message has been sent!')
        return redirect('/')
    
    return render(request, 'contact.html')

def getabout_me():
    return AboutMe.objects.first()
    
def get_education_Details():
    return Education.objects.all()
    
def get_skills():
    return Skill.objects.all()

def get_projects():
    return Projects.objects.all()

def get_links():
    return Link.objects.order_by('created_at').last() #to retrieve erliest data

def get_name_details():
    return Name_Details.objects.last()

def get_work_known():
    return Work_Known.objects.all()