from django.shortcuts import render

import datetime



# Create your views here.
def wishes3(request):
    date1 = datetime.datetime.now()
    msg1 = 'Hello User/Client...GOOD';
    hr = int(date1.strftime('%H'));
    imgs = 'GT1.jpg';
    if hr < 12:
        msg1 += ' Morning!!'
        imgs = 'REGT4.jpg';
    elif hr < 16:
        msg1 += ' Afternoon!!'
        imgs = 'GT1.jpg';
    elif hr < 20:
        msg1 += ' Evening!!'
        imgs = 'GT3.jpg';
    else:
        msg1 = 'Hello User/Client...Very Good Night!!'
        imgs = 'REGT5.jpg';
    dict1 = {'date1': date1, 'msg1': msg1, 'imgs': imgs}
    return render(request, 'FirstApp/wishes3.html', context=dict1);


def imagegallery(request):
    date1 = datetime.datetime.now()
    msg1 = '***DJango-Image-Gallery***';
    dict1 = {'date1': date1, 'msg1': msg1}
    return render(request, 'FirstApp/imggallery.html', context=dict1);


def imagegallery2(request):
    date1 = datetime.datetime.now()
    msg1 = '***DJango-Image-Gallery(Product)***';
    dict1 = {'date1': date1, 'msg1': msg1}
    return render(request, 'FirstApp/imggallery2.html', context=dict1);

def hyperlinks(request):
    date1 = datetime.datetime.now()
    msg1 = '***DJango-Hyperlinks***';
    dict1 = {'date1': date1, 'msg1': msg1}
    return render(request, 'FirstApp/hyperlinks.html', context=dict1);
