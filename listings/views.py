from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Merchant
from listings.forms import ContactUsForm, MerchantForm
from django.core.mail import send_mail




# Create your views here.

def merchandises(request):
    merchants=Merchant.objects.all().values()
    return render(
    request, 
    'listings/merchants.html', {
    'merchants':merchants
    })


def merchandises_details(request, id):
    merchant=Merchant.objects.get(id=id)
    
    template = loader.get_template()
    return render(request,
                  'listings/merchant-details.html',
                  {
        'merchant':merchant
    }
              )



def contact(request):
  if request.method == 'POST':
      form = ContactUsForm(request.POST)
      
      if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via Dushime Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['dondelicedushime@gmail.com'],
            )
            print('clleeaaanned', form.cleaned_data)
            return redirect('listings/')
      print('rrrr', request.method)
  else :
      form = ContactUsForm()
  return render(request,
          'listings/contact.html',
          {'form': form}) 
  
def merchant_create(request):
    if request.method == 'POST':
        
        if form.is_valid():
            
            merchant=form.save()
            return redirect('details', merchant.id)
    else:
        form=MerchantForm()
    return render(request,
              'listings/merchant_create.html',
          {
              'form': form,
          })
        
def merchant_update(request, id):
    merchant=Merchant.objects.get(id=id)
    if request.method == 'POST':
        form=MerchantForm(request.POST, instance=merchant)
        merchant=form.save()
        return redirect('details', merchant.id)
    else:
        form=MerchantForm()
    return render(request,
              'listings/merchant_update.html',
          {
              'form': form,
          })
    
    
def merchant_update(request, id):
        merchant=Merchant.objects.get(id=id)
    
        return render(request,
                  'listings/merchant_update.html',
                  {
        'merchant':merchant
    }
              )