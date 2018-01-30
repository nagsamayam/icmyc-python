from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage, BadHeaderError
from django.template import Context
from django.template.loader import render_to_string
from .tasks import dispatch_mail


def emailView(request):
    if request.method == 'GET':
        form = ContactForm(label_suffix='')
    else:
        form = ContactForm(request.POST, label_suffix='')
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            try:
                send_mail(subject, message, email, ['nag.samayam@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            
            return redirect('success')
            
    return render(request, 'pages/contact_us.html', {'form': form})


def successView(request):
    return HttpResponse("Success")


def sendTestMail(request):
    subject = "Complaint Posted"
    from_email, to_email = "nag.samayam@gmail.com", "nag.samayam@gmail.com"
    html_content = render_to_string('emails/complaint_posted.html', {'username': "Nageswara Rao"})
    dispatch_mail.apply_async((to_email, subject, html_content, from_email), countdown=10)
    dispatch_mail.delay(to_email, subject, html_content, from_email)
    return redirect('success')

