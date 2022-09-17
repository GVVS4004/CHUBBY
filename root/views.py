from django.shortcuts import redirect, render
from .models import CHUBBY
# Create your views here.


def home(request):
    chubby = CHUBBY.objects.all()
    return render(request, 'index.html', {'chubby': chubby})


def navigateForm(request, data=None):
    dataPresence = False
    if data:
        dataPresence = True
    return render(request, 'upload.html', {'data': data, 'dataPresence': dataPresence})


def pushData(request):
    if request.POST:
        restaurant = request.POST['rname']
        food = request.POST['fname']
        place = request.POST['place']
        cost = request.POST['price']
        rating = request.POST['rating']

        if request.POST.get('update', 0):
            id = request.POST['item-id']
            itemToBeUpdated = CHUBBY.objects.get(id=id)
            itemToBeUpdated.restaurant = restaurant
            itemToBeUpdated.food = food
            itemToBeUpdated.cost = cost
            itemToBeUpdated.place = place
            itemToBeUpdated.rating = rating
            if request.FILES:
                itemToBeUpdated.image = request.FILES['image']
            itemToBeUpdated.save()
            return redirect('/')
        data = CHUBBY(restaurant=restaurant, food=food, place=place,
                      cost=cost, rating=rating, image=request.FILES['image'])
        data.save()
        return redirect('/')
    return redirect('/form-data')


def deleteFood(request, id):
    CHUBBY.objects.filter(id=id)[0].delete()
    return redirect('/')


def updateFood(request, id):
    data = CHUBBY.objects.get(id=id)
    return navigateForm(request, data)
