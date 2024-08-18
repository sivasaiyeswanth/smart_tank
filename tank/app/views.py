from django.shortcuts import render
from .models import *
# Create your views here.
def tank_status(request):
    tank = TankData.objects.latest('last_updated')
    if tank.current_level < tank.threshold:
        # Logic to turn on the pump
        tank.pump_status = True
    else:
        # Logic to turn off the pump
        tank.pump_status = False
    if request.method == 'POST':
        threshold = request.POST.get('threshold')
        tank.threshold = int(threshold)
        
        tank.save()
    return render(request, 'tank_status.html', {'tank': tank})












