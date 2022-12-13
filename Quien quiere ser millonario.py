# 1.1-PANTALLA PRINCIPAL
from Preguntas import preguntas
import random


def saludo(nombre):
    print("Hola, {}, bienvenido a quien quiere ser millonario!!!".format(nombre))
    print("Muchas gracias por participar!!!")

    return None


def comodin(respuestas,tipo):
    if tipo == 'publico':
        pub=random.sample(respuestas,2)
        return pub
    


continuar = True
while continuar:
    nombre_usuario = input("Cual es su nombre?")
    saludo(nombre_usuario)
    print("¿Empezamos el juego?")

# 3-PREGUNTAS
    comodines= ['publico','50']
    opciones = ['a', 'b', 'c', 'd']
    random.shuffle(preguntas)
    puntaje = 0
    respuesta = input().lower()
    print(len(preguntas[:15]))
    if respuesta == "si":
        print("Empecemos!")
        for p in preguntas[:15]:
            print(p['title'])
            random.shuffle(p['answers'])
            for index in range(len(p["answers"])):
                print(f"{opciones[index]}: {p['answers'][index]}")
            print("Desea usar algun comodin?")
            respuestaC = input("Ingrese la respuesta correcta.")
            dd = opciones.index(respuestaC)
            if opciones == 'publico' or '50':
                comodin1=comodin(p["answers"],opciones)
            if p['correct_answer'] != p['answers'][dd]:
                print("Respuesta incorrecta, la respuesta correcta es:", p['correct_answer'])
                print("Fin del juego")
                break
            else:
                puntaje = puntaje+100
        print("Su puntaje final fue de: ", puntaje)

        otraVez = input("Desea empezar otra vez el juego?")
        if otraVez == "si":
            continuar = True

        else:
            continuar = False
            print("Gracias por participar.")

    if respuesta == "no":
        print("Bueno pues...")
        quit()

