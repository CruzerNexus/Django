from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import NewUrl
from .forms import ShortUrlForm

import random
import string


def submit_url(request):
    lettersNDigits = string.ascii_letters + string.digits
    random_code = ''.join(random.choice(lettersNDigits) for i in range(6))
    myUrl = NewUrl.objects.order_by('-id')[0]
    if request.method == 'POST':
        form = ShortUrlForm(request.POST)
        if form.is_valid():
            submit_url = form.cleaned_data['submit_url']
            myUrl = NewUrl(url=submit_url, code=random_code)
            myUrl.save()
            form = ShortUrlForm()
            return HttpResponseRedirect(reverse('shorturlapp:index'))
    else:
        form = ShortUrlForm()
    context = {'form': form, 'myUrl': myUrl}
    return render(request, 'shorturlapp/index.html', context)


def short_url(request, random_code):
    # GET request to go to site with short_url code
    this_url = NewUrl.objects.get(code=random_code)
    this_url.clicks += 1
    this_url.save()
    return HttpResponseRedirect(this_url.url)
    # will add one to the "count" in database
