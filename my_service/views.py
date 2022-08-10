from django.shortcuts import render
from my_service.models import VehicleModel, Vehicle, Service, Order, OrderDetail
from django.views import generic


# Create your views here.

def home(request):
    return render(request, 'index.html', )


def statistics(request):
    total_orders = Order.objects.all()
    total_done_orders = list(filter(lambda x: x.is_done, total_orders))
    total_vehicles = Vehicle.objects.all().count()
    total_services = Service.objects.all().count()

    context = {
        'total_orders': total_orders.count(),
        'total_done_orders': len(total_done_orders),
        'total_vehicles': total_vehicles,
        'total_services': total_services,

    }
    return render(request, 'statistics.html', context=context)


def vehicles(request):
    my_vehicles = Vehicle.objects.all()
    context = {
        'my_vehicles': my_vehicles

    }
    return render(request, 'vehicles.html', context=context)


def vehicle(request, vehicle_id):
    all_vehicles = Vehicle.objects.all()
    car = filter(lambda x: x.id == vehicle_id, all_vehicles)
    car_list = list(car)
    print(car_list)
    if car_list:
        a_car = (car_list)[0]
        context = {
            'my_vehicle': a_car
        }
    else:
        context = {

        }

    return render(request, 'vehicle.html', context=context)


class MyOrders(generic.ListView):
    model = Order
    context_object_name = 'my_orders'
    paginate_by = 1
    template_name = 'orders.html'


class MyOrder(generic.DetailView):
    model = Order

    context_object_name = 'my_order'

    template_name = 'order.html'
