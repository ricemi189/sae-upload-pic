i# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import time
import os
try:
    import Image
    import ImageDraw
    import ImageFont
except:
    from PIL import Image, ImageDraw, ImageFont
import StringIO


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

        bucket = sae.storage.Bucket(domain_name)
        content = bucket.get_object_contents(pic_name)
        buf = StringIO.StringIO(content)
        img = Image.open(buf)
        buf2 = StringIO.StringIO()
        draw = ImageDraw.Draw(img)
        x,y = img.size
        font_size = 18
        font = ImageFont.truetype(
            os.path.join(os.path.dirname(os.path.realpath(__file__)),
                     'font.ttf'),
            font_size)
        logo = u'@阿小信的博客'
        draw.text((x/2, y/2), logo, font=font)
        img.save(buf2, 'png')
        bucket.put_object(pic_name, buf2.getvalue())
        buf2.close()
        buf.close()
        return render_to_response('home.html', {'pic_url': url})
    return render_to_response('home.html')
