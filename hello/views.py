
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.core.mail import send_mail
from hello.forms import ContactForm


def home (request):
    if request.method == 'GET':
        form = ContactForm(request.POST or None)
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form_email = form.cleaned_data.get('contact_email')
            form_name = form.cleaned_data.get('contact_name')
            form_mobile = form.cleaned_data.get('contact_mobile')
            m = settings.EMAIL_HOST_USER
            subject = 'mail from django'
            message = form.cleaned_data.get('content')
            to_email = [m,'captainmagedashmawy@gmail.com']
            msg = 'mobile number: ' + form_mobile +"\n" + 'Name: ' + form_name +"\n" + 'Email: ' + form_email +"\n" + 'Message: ' + message

            try:
                send_mail(subject , msg ,m,to_email,fail_silently = False)

            except BadHeaderError:
                return HttpResponse('Invalid header found')

            return redirect('success')

    return render(request, 'index.html', {'form': form})


def suc (request):
    return render(request,'success.html', {})

