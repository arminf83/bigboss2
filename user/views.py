from django.shortcuts import render
from product.models import Favorite

def dashboard(request):
  user = request.user 

  favorite_items = Favorite.objects.filter(user=user)


  context = {
    'user_name': user.name, 
    'favorite_items': favorite_items,
    
  }

  return render(request, 'account-infoprofile.html', context)

