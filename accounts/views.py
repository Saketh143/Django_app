from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.


def register(request):
    if request.method == 'POST':
        # Get values from post method .
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check for passwords

        if password == password2:
            # check for username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already taken !')
                return redirect('register')
            else:
                # check for email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already registered !')
                    return redirect('register')
                else:
                    # looks all good
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    user.save()
                    # for login after register
                    # auth.login(request,user)
                    # messages.success(request,"logged in succesfully")
                    # return redirect('index.html')

                    messages.success(request, "Registration successful , You can now login")
                    return redirect('login')
        else:
            messages.error(request, "passwords do not match !")
            return redirect('register')



    else:

        return render(request, 'accounts/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "logged in successfully ")
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password !')
            return redirect('login')


    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,"you logged out successfully")
        return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)

    context = {
        'contacts' : user_contacts
    }
    return render(request, 'accounts/dashboard.html',context)
