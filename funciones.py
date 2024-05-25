from funciones_matematicas import *

def menu()->str:
  #limpiar_pantalla()
  print(f"{'\n--Menu de opciones--\n'}")
  print("1- Ingresar 1er operando")
  print("2- Ingresar 2do operando")
  print("3- Calcular todas las operaciones:")
  print("4- Informar resultados")
  print("5- Salir")
  return input(f"\ningrese una opcion: ")

def pausar():
  import os
  print("")
  os.system("pause")
  

def limpiar_pantalla():
  import os
  os.system("cls")

def pedir_confirmacion(mensaje:str)->bool:
  rta = input(mensaje).lower()
  return rta == 'si'

