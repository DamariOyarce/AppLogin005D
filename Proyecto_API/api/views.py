import json
from typing import List
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario

# Create your views here.

class UsuarioView(View):
 
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
 
    def get(self, request,id=0):
        if (id>0):
            usuarios=list(Usuario.objects.filter(id=id).values())
            if len(usuarios) > 0:
                usuario=usuarios[0]
                datos = {'message': "Success",'usuarios':usuario}
            else:
                datos = {'message': " not found ..."}
            return JsonResponse(datos)      
        else:
            usuarios = list(Usuario.objects.values())
            if len(usuarios) > 0:
                datos = {'message': "Success",'usuarios':usuarios}
            else:
                datos = {'message': "Companies not found ..."}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd =json.loads(request.body)
        #print(jd)
        Usuario.objects.create(nombreusuario=jd['nombreusuario'],email=jd['email'],contraseña=jd['contraseña'])
        datos={'message' : "Success" }
        return JsonResponse (datos)

    def put(self, request,id):
        jd =json.loads(request.body)
        usuarios=list(Usuario.objects.filter(id=id).values())
        if len(usuarios) > 0:
            usuario=Usuario.objects.get(id=id)
            usuario.nombreusuario = jd['nombreusuario']
            usuario.email = jd['email']
            usuario.contraseña = jd['contraseña']
            usuario.save()
            datos = {'message': "Success"}   
        else:
            datos={'message': "Usuario not found..." }
        return JsonResponse(datos)
            

    def delete(self, request,id):
        usuarios=list( Usuario.objects.filter(id=id).values())
        if len(usuarios) > 0:
            Usuario.objects.filter(id=id).delete()
            datos = {'message': "Success"}   
            
        else:
            datos={'message': "Companies not found..." }
        return JsonResponse(datos)
