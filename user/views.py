from django.shortcuts import render
from product.models import Favorite

def dashboard(request):
  user = request.user 

  # favorite_items = Favorite.objects.filter(user=user)
  print(request.user)


  

  return render(request, 'user/account-infoprofile.html', )

