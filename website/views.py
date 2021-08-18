from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'home.html', {})
def index(request):
    return render(request,'index.html', {})
def appointment(request):
    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        date    = request.POST['date']
        email   = request.POST['email']
        treatment   = request.POST['treatment']
        note = request.POST['note']

        send_mail(
            first_name,
            last_name,
            date,
            email,
            treatment,
            note,
            ['pallavigupta2920@gmail.com', 'b180016@nitsikkim.ac.in']

            )

        return render(request,'appointment.html', {'first_name' : first_name, 'last_name' : last_name, 'date': date, 'treatment':treatment,'note':note})

    else:
        return render(request,'index.html',{})

def about(request):
    return render(request,'about.html', {})

def news(request):
    return render(request,'news.html', {})

def patients(request):
    return render(request,'patients.html', {})

def services(request):
    return render(request,'services.html', {})



def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        date    = request.POST['date']
        email   = request.POST['email']
        treatment   = request.POST['treatment']
        note = request.POST['note']

        # send_mail(
        #     first_name,
        #     last_name,
        #     date,
        #     email,
        #     treatment,
        #     note,
        #     ['pallavigupta2920@gmail.com', 'b180016@nitsikkim.ac.in']
        #
        #     )

        return render(request,'contact.html', {'first_name' : first_name})

    else:
        return render(request,'contact.html', {})
