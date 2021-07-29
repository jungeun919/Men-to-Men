from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    return render(request, 'mail/index.html')

def sendEmail(request):
    try:
        inputReceiver = request.POST['inputReceiver']
        inputTitle = request.POST['inputTitle']
        inputContent = request.POST['inputContent']

        content = {'inputReceiver':inputReceiver, 'inputTitle':inputTitle, 'inputContent':inputContent}

        msg_html = render_to_string('mail/email_format.html', content)

        msg = EmailMessage(subject=inputTitle, body=msg_html, from_email="djangoemailtester001@gmail.com", bcc=inputReceiver.split(','))
        msg.content_subtype = 'html'
        msg.send()
        return render(request, 'mail/sendSuccess.html')
    except:
        return render(request, 'mail/sendFail.html')