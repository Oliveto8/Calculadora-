from funciones_matematicas import *
from funciones import *

flag_operandoA = False
flag_operandoB = False
flag_calculado = False

seguir = "si"

while seguir == "si":
  match menu():
    case "1":
      operando1 = ingresar_operando("primer operando")
      flag_operandoA = True
      print(f"\nEl primer operando es {operando1}")
    case "2":
      if flag_operandoA:
        print(f"\nEl primer operador es {operando1}")
        operando2 = ingresar_operando("segundo operando")
        flag_operandoB = True
        print(f"\nEl primer operando es {operando1}")
        print(f"\nEl segundo operando es {operando2}")
      else:
        print("\nAntes de ingresar el segundo operando primero deberiamos ingresar el primero...")
    case "3":
      if flag_operandoA and flag_operandoB:
        print(f"\nEl primer operando es {operando1}")
        print(f"\nEl segundo operando es {operando2}")
        flag_calculado = True
        calculos(operando1,operando2)
        print(f"\nCalculos realizados")
      else:
        print("\nAntes de calcular primero debemos ingresar ambos operandos")
    case "4":
      if flag_calculado:
        informar_resultados(operando1,operando2)
        flag_calculado = False
        flag_operandoA = False
        flag_operandoB = False
      elif flag_operandoA == False and flag_operandoB == False:
        print("\nAntes de calcular primero debemos ingresar ambos operandos")
      else:
        print("\nAntes de mostrar los resultados primero debemos calcularlos")
    case "5":
      if pedir_confirmacion("\n¿Confirmar salida? "):
        seguir = "no"
        continue
    case _:
      print("\nIngrese uno de los numneros indicados")
  pausar()

print("\nFin del programa")
