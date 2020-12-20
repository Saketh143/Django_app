from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if user is already made an enquiry

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)

            if has_contacted:
                messages.error(request, 'you have already contacted this listing')
                return redirect('/listings/' + listing_id)

        contact = Contact(name=name, email=email, phone=phone, listing_id=listing_id, listing=listing
                          , user_id=user_id)

        contact.save()
        # Send mail
        """
        send_mail(
            'Property Listing Inquiry' ,
            'There has been a inquiry for' + listing + '. Login in admin area for further details' ,
            'sakethamaragani0143@gmail.com' ,
            [realtor_email , 'sakethamargani1037@gmail.com'],
            fail_silently = False
        )"""

        messages.success(request, 'Your request is submitted successfully, realtor will back to you soon !')

        return redirect('/listings/' + listing_id)
