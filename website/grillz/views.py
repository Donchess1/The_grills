from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'grillz/index.html')

def timetable(request):
    return render(request, 'grillz/timetable.html')

def review(request):
    return render(request, 'grillz/review.html')
def signup(request):
    return render(request, 'shop/signup.html')
