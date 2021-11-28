from django.shortcuts import render, redirect
from .models import Location,Category,Image

# views 
def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request,'photos/index.html',{'images':images[::-1],'locations':locations})

def image_location(request,location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'photos/location.html', {'location_images':images})

def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_category = request.GET.get('category')
        searched_categories = Image.search_by_category(search_category)
        print(searched_categories)
        message = f'{search_category}'
        return render(request, 'photos/search.html', {'message':message,'images':searched_categories})
    else:
        message = 'You need to search for an image category'
        return render(request, 'photos/search.html', {'message':message})