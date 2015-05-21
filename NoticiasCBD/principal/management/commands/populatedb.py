# 'manage.py populatedb'
#
from datetime import date, datetime
from django.contrib.auth.models import Permission
from django.core.management.base import BaseCommand
from django.contrib import auth
from principal.models import *


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _migrate(self):
        # Drop all tables
        print('Borrando datos actuales...')

        Noticia.objects.all().delete()
        Editorial.objects.all().delete()
        Persona.objects.all().delete()


        print('Creando personas')
        p1 = Persona(nombre='Carlos', apellidos='Borja Garcia-Baquero')
        p2 = Persona(nombre='Ruben', apellidos='Gomez Barrera')
        p3 = Persona(nombre='Julio', apellidos='Maldonado Maldini')
        p4 = Persona(nombre='Josep', apellidos='Pedrerol')
        p1.save()
        p2.save()
        p3.save()
        p4.save()
        print('Personas creadas')

        print('Creando editoriales')
        e1 = Editorial(nombre='Marca')

        e2 = Editorial(nombre='US')

        e3 = Editorial(nombre='AS')

        e4 = Editorial(nombre='El pais')

        e1.save()
        e2.save()
        e3.save()
        e4.save()
        print('Editoriales creadas')
        print('Uniendo empleados con editorial')
        e1.empleados.add(p1)
        e2.empleados.add(p2)
        e3.empleados.add(p3)
        e4.empleados.add(p4)
        e1.save()
        e2.save()
        e3.save()
        e4.save()
        print('Union creada')
        print('Creando noticias')
        n1 = Noticia(titulo = 'Xavi Hernandez se marcha del Barcelona',
                     cuerpo= 'El capitan del FC Barcelona, Xavi Hernandez, abandonara al final de temporada el club catalan tras llegar a la conclusion de que es "el momento" de irse, despues de 17 temporadas, y firmara con el Al-Sadd catari, aunque ha asegurado que volver al Barcelona es su "objetivo". "Confirmo mi salida del Barcelona. Es una decision definitiva y dificil. No ha sido una decision sencilla ni facil. Lo he consensuado con mi mujer, con mi familia, con los mios. Pero es el momento de marcharme", ha anunciado en rueda de prensa el jugador, que ha reconocido que le cuesta digerir no estar ya en el equipo ni sentirse importante.',
                     publicador = p1)
        n1.editoral = e1
        n1.save()
        n2 = Noticia(titulo = 'El Real Betis sube a primera division',
                     cuerpo= 'El equipo de la palmera consigue volver a la maxima categoria despues de una temporada dificil.',
                     publicador = p2)
        n2.editoral = e2
        n2.save()
        print('Noticias creadas')


    def handle(self, *args, **options):
        self._migrate()
