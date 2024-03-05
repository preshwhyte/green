from django.shortcuts import render,redirect
from .models import News,Volunteer, SubscribedUsers,Contact
from .forms import VolunteerForm,NewsForm, NewsletterForm,RegisterForm,LoginForm,ContactForm
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.template.loader import render_to_string

import csv

# Create your views here.

def home(request):
    news=News.objects.all()
    p=Paginator(News.objects.all(), 2)
    page=request.GET.get('page')
    listed=p.get_page(page)

    L=Paginator(News.objects.all().order_by('-date'), 2)
    page=request.GET.get('page')
    list=L.get_page(page)

    submitted=False
    if request.method=="POST":
        form=VolunteerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/news/?submitted=True')
    else:
        form=VolunteerForm
        if 'submitted' in request.GET:
            submitted=True

    return render(request, 'index.html', {'form':form, 'listed':listed,'news':news, 'list':list})


def member_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition'] ='attachment; filename=member.csv'
    members=Volunteer.objects.all()

    writer=csv.writer(response)

    writer.writerow(['full_name', 'email','subject','cv', 'comment' ])

    # lines=['this is my world']
    lines=[]

    for mem in members:
        writer.writerow([mem.full_name, mem.email,mem.subject,mem.cv, mem.comment])

    
    return response

def news(request):

    news=News.objects.all()
    p=Paginator(News.objects.all().order_by('-date'), 2)
    page=request.GET.get('page')
    listed=p.get_page(page)
    return render(request, 'news.html',{'news':news, 'listed':listed})

def newsdetail(request, pk):
    detail=News.objects.get(id=pk)
    return render(request,'newsdetail.html', {'news':detail})

def addnews(request):
    if request.method=="POST":
        newsform=NewsForm(request.POST,request.FILES)
        if newsform.is_valid():
            newsform.save()
            return redirect('home')
    else:
        newsform=NewsForm()

    return render(request, 'addnews.html',{'newsform':newsform})

def search(request):
    if request.method=="POST":
        searched=request.POST['searches']
        searches=News.objects.filter(title__contains=searched)
        return render(request, 'newsSearch.html',{'searches':searches, 'searched':searched})
    else:
        return render(request, 'newsSearch.html')


def search_result(request, search_result):
    result=News.objects.get(id=search_result)
    return render(request, 'searchresult.html', {'news':result})

def contact(request):
    
    submitted=False
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/?submitted=True')
    else:
        form=ContactForm
        if 'submitted' in request.GET:
            submitted=True


        # First instance

    #     message = request.POST.get('message')
    #     name = request.POST.get('name')
    #     email=request.POST.get('email')
    #     ctx = {
    #        'name' : name,
    #        'email':email,
    #        'message' : message
    #    }
    #     message = render_to_string('mail.html', ctx)
    #     send_mail('Contact Form',
    #     message,
    #     settings.EMAIL_HOST_USER,
    #     [email], 
    #     fail_silently=False, html_message=message)
        
        # second instance
 
        # first_name=request.POST['first-name']
        # last_name=request.POST['last-name']
        # email=request.POST['email']
        # message=request.POST['message']
        # send_mail(
        #     first_name,
        #     message,
        #     'settings.EMAIL_HOST_USER',
        #     # 'omnipresh2@gmail.com',
        #     [email],
        #     fail_silently=False)
    return render(request,'contacts.html',{'form':form, 'submitted':submitted})

def contact_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition'] ='attachment; filename=contact.csv'
    contacts=Contact.objects.all()

    writer=csv.writer(response)

    writer.writerow(['name', 'email','message', 'date' ])

    # lines=['this is my world']
    lines=[]

    for contact in contacts:
        writer.writerow([contact.name, contact.email,contact.message,contact.date])

    
    return response


def about(request):
    return render(request, 'about.html')

def causes(request):
    return render(request, 'causes.html')

def environ(request):
    return render(request, 'environ.html')

def health(request):
    return render(request, 'health.html')

def leader(request):
    return render(request, 'leader.html')

def peace(request):
    return render(request, 'peace.html')

def smart(request):
    return render(request, 'smart.html')

def others(request):
    return render(request, 'others.html')


def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request, 'Registration sucessfull')
            return redirect('home')
        else:
            messages.error(request,'not valid')
    
    else:
        form=RegisterForm()

    return render(request,'register.html',{'form':form})



def signin(request):
    form=LoginForm(request.POST or None)
    
    if request.method=='POST':
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None and user.is_admin:
                login(request,user)
                return redirect('home')
            elif user is not None and user.is_member:
                login(request,user)
                return redirect('about')
            elif user is not None and user.is_users:
                login(request,user)
                return redirect('home')
        else:
            messages.error(request, 'Your login details are incorrect') 
    return render(request,'login.html',{'form':form})

def signout(request):
    logout(request)
    messages.success(request, 'you\'ve successfully loggedout')
    return redirect('home')


def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not name or not email:
            messages.error(request, "You must type legit name and email to subscribe to a Newsletter")
            return redirect("/")

        if get_user_model().objects.filter(email=email).first():
            messages.error(request, f"Found registered user with associated {email} email. You must login to subscribe or unsubscribe.")
            return redirect(request.META.get("HTTP_REFERER", "/")) 

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))  


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')

            mail = EmailMessage(subject, email_message, f"PyLessons <{request.user.email}>", bcc=receivers)
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request, "Email sent succesfully")
            else:
                messages.error(request, "There was an error sending email")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('/')

    form = NewsletterForm()
    form.fields['receivers'].initial = ','.join([active.email for active in SubscribedUsers.objects.all()])
    return render(request=request, template_name='newsletter.html', context={'form': form})
