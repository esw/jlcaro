from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django import forms

#send_mail()

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30,label="Name:")
    email = forms.EmailField(label='E-Mail:')
    message = forms.CharField(widget=forms.Textarea,label="Message:")
    

def contact_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            send_mail('Contact Email from jlcaro.com',message,email,['me@jlcaro.com'],fail_silently=True)
            return HttpResponse('success')
    else:
        contact_form = ContactForm()
    return render_to_response('contact.html',{'contact_form':contact_form},context_instance=RequestContext(request))

def process_contact_view(request):
    if request.method == 'POST':
        contact_form = ContactForm

