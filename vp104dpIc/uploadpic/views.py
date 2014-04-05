from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import time


@csrf_exempt
def home(request):
    from os import environ
    online = environ.get("APP_NAME", "")
    if request.method == "POST" and online:
        import sae.storage
        domain_name = 'pics'
        s = sae.storage.Client()
        pic = request.FILES['pic']
        pic_suffix = pic.name.split('.')[-1]
        pic_name = str(time.time()) + '.' + pic_suffix
        ob = sae.storage.Object(pic.read())
        url = s.put(domain_name, pic_name, ob)
        return render_to_response('home.html', {'pic_url': url})
    return render_to_response('home.html')
