from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django import forms

#send_mail()

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    message = forms.CharField()
    

def send_contact_mail(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            send_mail('Email from jlcaro.com Contact',message,email,['me@jlcaro.com'],fail_silently=True)
            return HttpResponseRedirect(reverse('email_success'))
    else:
        contact_form = ContactForm()
    return render_to_response('contact',{'contact_form':contact_form},context_instance=RequestContext(request))


