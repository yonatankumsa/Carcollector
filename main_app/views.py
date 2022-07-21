from django.shortcuts import render, redirect

# Add the following import
from django.http import HttpResponse
from .models import Car,Shop
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .forms import ModsForm
from django.views.generic import ListView, DetailView
# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
   return render(request, 'about.html')

def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  id_list = car.shop.all().values_list('id')
  shop_car_doesnt_have = Shop.objects.exclude(id__in=id_list)
  mods_form = ModsForm()
  return render(request, 'cars/detail.html', {
    'car': car, 'mods_form': mods_form,
    'shop': shop_car_doesnt_have
  })

def add_mods(request, car_id):
  # create a ModelForm instance using the data in request.POST
  form = ModsForm(request.POST)
  # validate the form
  if form.is_valid():
    new_mods = form.save(commit=False)
    new_mods.car_id = car_id
    new_mods.save()
  return redirect('detail', car_id=car_id)


class CarCreate(CreateView):
  model = Car
  fields = '__all__'
  success_url = '/cars/'
  
class CarUpdate(UpdateView):
  model = Car
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['model', 'description', 'price']
  success_url ='/cars/'

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'  

class ShopList(ListView):
  model = Shop

class ShopDetail(DetailView):
  model = Shop

class ShopCreate(CreateView):
  model = Shop
  fields = '__all__'

class ShopUpdate(UpdateView):
  model = Shop
  fields = ['name', 'address']

class ShopDelete(DeleteView):
  model = Shop
  success_url = '/shop/'

def assoc_shop(request, car_id, shop_id):
  Car.objects.get(id=car_id).shop.add(shop_id)
  return redirect('detail', car_id=car_id)