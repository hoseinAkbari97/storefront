from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        message = EmailMessage(
            'subject', 'message', 'info@moshbuy.com',
            ['abc@moshbuy.com']
        )
        message.attach_file(
            'playground/static/images/Screenshot (91).png'
        )
        message.send()
    except BadHeaderError:
        pass
    
    return render(request, 'hello.html', {'name': 'Mosh'})
