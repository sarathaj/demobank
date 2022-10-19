from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import user_login

def index(request):
    return render(request, './myapp/index.html')


def user_details_add(request):
    return render(request, './myapp/user_details_add.html')


def new_page(request):
    return render(request, './myapp/new_page.html')







from .models import user_details

def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='user')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}

            return render(request, 'myapp/login.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/login.html',context)
    else:
        return render(request, 'myapp/login.html')



def register(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        # lname = request.POST.get('lname')
        # gender = request.POST.get('gender')
        # age = request.POST.get('age')
        # addr = request.POST.get('addr')
        # pin = request.POST.get('pin')
        # email = request.POST.get('email')
        # contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=fname
        #status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='user')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=0, gender=0, age=0,address=0, pin=0, contact=0, email=0 )
        ud.save()

        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/login.html',context)

    else:
        return render(request, 'myapp/register.html')




def user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=email
        #status = "new"

        ul = user_login(uname=uname, passwd=0, u_type='user')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=0, gender=gender, age=age,address=addr, pin=pin, contact=contact, email=email )
        ud.save()

        print(user_id)
        context = {'msg': 'application accepted'}
        return render(request, 'myapp/login.html',context)

    else:
        return render(request, 'myapp/user_details_add.html')




def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)




