# -*- coding: utf-8 -*-
primer_string = "Hola mundo\n 'Duvan'";
curso = "python 3";
nombre = "Duvan";
mensajefinal = "El" + curso + " practicado por" + nombre; # concatenación 1
mensajefinal = "El curso de  %s  practicado por %s" %(curso,nombre); # concatenación 2
mensajefinal = "yo {} practico el curso de {} ".format(nombre,curso); # concatenación 2
print(mensajefinal)
K= input("stop")