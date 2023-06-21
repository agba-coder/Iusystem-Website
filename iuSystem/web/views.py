import os
from django.shortcuts import render
from .models import Participant

from django.shortcuts import render, redirect
from django.contrib import messages

from django.conf import settings
import random

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

from decouple import config
import ssl, smtplib
from django.template.loader import render_to_string
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

from django.conf import settings
from django.core.mail import send_mail, BadHeaderError

#from .forms import RegistrationForm

# Create your views here.


def home(request):
    return render(request, "index.html")


def contact(request):
    
    if request.method == "POST":
       name = request.POST["name"]
       from_email = request.POST["email"]
       message = request.POST["message"]
       
       subject = f"Mail From Your Website From {name}"
       message = message
       EMAIL_HOST_USER = settings.EMAIL_HOST_USER
       
       try:
           send_mail(subject, message, from_email, ["iusystem02@gmail.com", "hi.agbacoder@gmail.com"])
       except BadHeaderError:
           messages.error(request, 'Inavalid Header Found!')
           return render(request, "Contactus.html")
       
       messages.success(request, 'Mail Sent✅!')
       return render(request, "Contactus.html")
       
    return render(request, "Contactus.html")


def team(request):
    return render(request, "team.html")


def register(request):
    
    if request.method == "POST":
        #form = RegistrationForm()
        
        pic = request.FILES.get("pic")
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        age = request.POST["age"]
        category = request.POST["category"]
        school = request.POST["school"]
        gender = request.POST["gender"]
        print(age)
        # print(image)
        print(category)
        username = firstname + " " + lastname

        if Participant.objects.filter(first_name=firstname).exists():
            if Participant.objects.filter(last_name=lastname).exists():
                print('Username Taken')
                messages.error(request, 'Candidate Already Exist!')
                return render(request, 'Registration.html')#, {'error': 'Username is already taken!'})
            
            elif Participant.objects.filter(email=email).exists():
                print('email Taken')
                messages.error(request, 'Email Already Taken!')
                return render(request, 'Registration.html')
            
        else:
            key = "IUS"
            num = random.randrange(000000, 999999)
            reg_num = key + str(num)
            print(reg_num)
            x = random.randrange(0000,9999)
            ref = firstname + lastname + str(x)
            print(ref)
            participant = Participant.objects.create(profile_image=pic, first_name = firstname, last_name=lastname, registration_number=reg_num, email=email, gender=gender, phone_number=phone, age=age, category=category, name_of_school=school, reference=ref)
            participant.save()
            print('Successfully Registered Candiddate')
            messages.success(request, 'Successfully Registered Candiddate!')
            
            context = {"reg_num": reg_num, "ref": ref, "username": username, "email": email, "paystack_pub_key": settings.PAYSTACK_PUBLIC_KEY}
            
            return render(request, "make-payment.html", context)
            
    return render(request, "Registration.html")

def competition(request):
    return render(request, "competition.html")


def makePayment(request):
    # name = Participant.completed = True
    # print(name)
    context = {"paystack_pub_key": settings.PAYSTACK_PUBLIC_KEY}

    return render(request, "make-payment.html", context)


# pass iusystem