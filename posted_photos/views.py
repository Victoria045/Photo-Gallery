from django.shortcuts import render,redirect

# views 
def index(request):
     
    return render(request,'photos/index.html')
