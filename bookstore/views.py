from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Regis_db, donate_db, contact_db


def home(request):
    return render(request, 'bookstore/home.html')


def login(request):
    if 'em' in request.session:
        em = request.session['em']
        return redirect('homeurl:dotame')
    elif request.method == 'POST':
        em = request.POST.get('emailid')
        pa = request.POST.get('password')

        if (len(Regis_db.objects.filter(emailid=em)) and
                len(Regis_db.objects.filter(password=pa))):
            request.session['em'] = em
            return redirect('homeurl:dotame')
    return render(request, 'bookstore/login.html')


def register(request):
    if request.method == "POST":
        name = request.POST['username']
        emailid = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        reg_db_obj = Regis_db()
        reg_db_obj.name = name
        reg_db_obj.emailid = emailid
        reg_db_obj.password = password

        reg_db_obj.confirm_password = confirm_password
        reg_db_obj.save()
        return redirect('homeurl:himanshu')

    return render(request, 'bookstore/register.html')


def hemu(request):
    return render(request, 'bookstore/home.html')


def dota(request):
    # # em = None
    # if (request.method == "GET"):
    #     if 'action' in request.GET:
    #         action = request.GET.get('action')
    #         if action == 'logout':
    #             if request.session.has_key('em'):
    #                 request.session.flush()
    #                 return redirect('homeurl:himanshu')
    # if 'em' in request.session:
    #     em= request.session['em']
    return render(request, 'bookstore/dota.html')


def copyright(request):
    return render(request, 'bookstore/copyright.html')


def donate(request):
    if request.method == "POST":
        Category = request.POST['Category']
        Book_Name = request.POST['Book_Name']
        Author_Name = request.POST['Author_Name']
        Donater_name = request.POST['Donater_name']
        Mob_no = request.POST['Mob_No']
        Email_id = request.POST['Email_id']
        City_name = request.POST['City_name']
        Select_State = request.POST['Select_State']

        reg_db_obj = donate_db(filename=request.FILES['filename'])

        reg_db_obj.Category = Category
        reg_db_obj.Book_Name = Book_Name
        reg_db_obj.Donater_name = Donater_name
        reg_db_obj.Mob_no = Mob_no
        reg_db_obj.Email_id = Email_id
        reg_db_obj.Author_Name = Author_Name
        reg_db_obj.City_name = City_name
        reg_db_obj.Select_State = Select_State

        reg_db_obj.save()
        messages.success(request, 'saved')
        print(1)
        return redirect('homeurl:add')

    return render(request, 'bookstore/donate.html')


def shortstory(request):
    return render(request, 'bookstore/shortstory.html')


def novels(request):
    return render(request, 'bookstore/novels.html')


def art(request):
    return render(request, 'bookstore/art.html')


def creative(request):
    return render(request, 'bookstore/creative.html')


def novels1(request):
    return render(request, 'bookstore/novels1.html')


def art1(request):
    return render(request, 'bookstore/art1.html')


def creative1(request):
    return render(request, 'bookstore/creative1.html')


def take(request):
    obj = donate_db.objects.all()

    return render(request, 'bookstore/take.html',
                  {'data': obj})


def contact(request):
    if request.method == "POST":
        Your_name = request.POST['Your_name']
        Email_Address = request.POST['Email_Address']
        Mobile_No = request.POST['Mobile_No']
        Message = request.POST['Message']

        reg_db_obj = contact_db()
        reg_db_obj.Your_name = Your_name
        reg_db_obj.Email_Address = Email_Address
        reg_db_obj.Mobile_No = Mobile_No
        reg_db_obj.Message = Message

        reg_db_obj.save()
        return redirect('homeurl:hemu')

    return render(request, 'bookstore/contact.html')


def logout(request):
    auth.logout(request)
    return render(request, 'bookstore/logout.html')


def add(request):
    return render(request, 'bookstore/add.html')


def view(request):
    return render(request, 'bookstore/view.html')
