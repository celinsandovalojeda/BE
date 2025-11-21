from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def vehiculo_list(request):
    return render(request, "vehiculo_list.html")

def vehiculo_create(request):
    return render(request, "vehiculo_create.html")

def vehiculo_edit(request, id):
    return render(request, "vehiculo_edit.html")

def vehiculo_delete(request, id):
    return render(request, "vehiculo_delete.html")


