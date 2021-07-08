from django.shortcuts import render
from .models import Articulo

def index(request):
	try:
		a = Articulo.objects.all() 
		name=[]
		for i in range(len(a)):
			name.append(a[i])

		data = (sql_c.nombre, sql_c.exp) 
	except:
		pass
	return render(request,"index.html",{"datos":name})

def cart(request, dato):
	try:
		e = Articulo.objects.get(nombre=dato) 
		e_l = [e.nombre, e.descripcion, e.precio, e.ruta]
	except:
		pass
	return render(request,"cart.html",{"dato":e_l})
