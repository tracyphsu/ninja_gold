from django.shortcuts import render, redirect
import random
from datetime import datetime


def process_money(request):
    if not "gold" in request.session or "acitivites" not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')

def process_farm(request):
    activity = 'farm'
    farm_random = random.randint(10, 20)
    time_now = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    if 'gold' not in request.session:
        request.session['gold'] = 0
    request.session['gold'] += farm_random
    result = 'earn'
    current_gold = farm_random
    message = f"Earned {current_gold} from the Farm! ({time_now})"
    request.session['activities'].append({"message": message, "result": result})
    return render(request, 'index.html')

def process_cave(request):
    activity = 'cave'
    cave_random = random.randint(5, 10)
    time_now = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    if 'gold' not in request.session:
        request.session['gold'] = 0
    request.session['gold'] += cave_random
    result = 'earn'
    current_gold = cave_random
    message = f"Earned {current_gold} from the Cave! ({time_now})"
    request.session['activities'].append({"message": message, "result": result})
    return render(request, 'index.html')

def process_house(request):
    activity = 'house'
    house_random = random.randint(2, 5)
    time_now = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    if 'gold' not in request.session:
        request.session['gold'] = 0
    request.session['gold'] += house_random
    result = 'earn'
    current_gold = house_random
    message = f"Earned {current_gold} from the House! ({time_now})"
    request.session['activities'].append({"message": message, "result": result})
    return render(request, 'index.html')

def process_casino(request):
    activity = 'casino'
    casino_random = random.randint(-50, 50)
    time_now = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    if 'gold' not in request.session:
        request.session['gold'] = 0
    request.session['gold'] += casino_random
    current_gold = casino_random
    if current_gold > 0:
        result = 'earn'
        message = f"Earned {current_gold} from the Casino! ({time_now})"
    else:
        result = 'lose'
        message = f"Entered a Casino and lost {current_gold} golds... Ouch... ({time_now})"
    request.session['activities'].append({"message": message, "result": result})
    return render(request, 'index.html')

def reset(request):
    request.session.flush()
    return redirect('/')