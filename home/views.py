from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("hi")

def home(request):
    if request.method == 'POST':
        form = img_input(request.POST, request.FILES) # 꼭 !!!! files는 따로 request의 FILES로 속성을 지정해줘야 함
    else:
        form = img_input()
    return render(request, 'home.html')

def result(request):
    return HttpResponse("hi")