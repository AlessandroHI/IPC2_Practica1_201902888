from Cola import Cola
from Orden import Orden
from Pizza import Pizza
from graphviz import Digraph
import emoji


def generarGrafica(ordenes):
    
  if ordenes.length() == 0:
    ni = Digraph('ni')  
    ni.attr(bgcolor='#215985')
    ni.edge_attr.update(dir = 'none' , color = '#81FFE5')
    ni.attr('node', shape='box')
    ni.node_attr.update(style='filled')
    ni.node('Q', "Cola de ordenes vacias",color='#EA8D18')
    ni.render('grafo.gv', view=True)
  
  else:
    ni = Digraph('ni')  
    ni.attr(bgcolor='#215985')
    ni.attr('node', shape='box')
    ni.node_attr.update(style='filled')
    ni.node('Q', "Cola de ordenes",color='#EA8D18')
    pizzas = """
    """
    for i in range(Ordenes[0].Pizzas.length()):
      pizzas += """ Pizza"""+str(Ordenes[0].Pizzas[i].noPizza)+""":  con ingredientes: """+str(Ordenes[0].Pizzas[i].ingredients)+"""
      """

    ni.node('0', "No. de orden: 1"+"\n Tiempo de elaboración: "+ str(ordenes[0].tiempo)+"min"  + "\n A nombre de: "+ str(ordenes[0].Nombre)+ " NIT: " +str(ordenes[0].NIT) + pizzas )
    for i in range(1,ordenes.length()):
      ni.node(str(i), "No. orden: "+str(i+1)+"\n A nombre de: "+ ordenes[i].Nombre + " NIT: " +str(ordenes[i].NIT))
    
    ni.attr(rankdir='TB')
    ni.edges(["Q0"])
    for i in range(ordenes.length()):
      if i < ordenes.length() - 1:
       ni.edges([str(i)+str(i+1)])
    ni.render('grafo.gv', view=True)
    
    
def addOrden():
  global Ordenes
  Pizzas = Cola()
  tiempoTotal = 0 #TIEMPO TOTAL PARA DICHA ORDEN
  cont = 1
  
  nombreCliente = input("\nIngresar nombre del cliente: ")
  Nit = input("\nIngresar NIT del cliente: ")
  noPizzas = int(input("\nIngrese No. pizzas a ordenar: "))
  for i in range(noPizzas):
      noIngrdientes = int(input("\nPara la pizza "+str(cont)+" cuantos ingredientes desea:"))
      ingre = ""
      tiempoo1 = 0
      for j in range(noIngrdientes):
          print("\n1- Pepperoni\n2- Salchicha\n3- Carne\n4- Queso\n5- Piña")
          ingredientes = input("Ingrese el ingrediente:")
          
          if ingredientes == "1":
              ingre += "Pepperoni, "
              tiempoTotal += 3
              tiempoo1 += 3
          if ingredientes == "2":
              ingre += "Salchicha, "
              tiempoTotal+=4
              tiempoo1 +=4
          if ingredientes == "3":
              ingre += "Carne, "
              tiempoTotal +=10
              tiempoo1 +=10
          if ingredientes == "4":
              ingre += "Queso, "
              tiempoTotal += 5
              tiempoo1 += 5
          if ingredientes == "5":
              ingre += "Piña, "
              tiempoTotal += 2
              tiempoo1 += 2
      Pizzas.agregar_orden(Pizza(cont,ingre,tiempoo1))
      cont +=1
  Ordenes.agregar_orden(Orden(nombreCliente,Nit,Pizzas,tiempoTotal))
  print("Orden agregada...")
  generarGrafica(Ordenes)
  
     
def mostrar_Ordenes():
    print("--------- ORDENES ---------")
    if Ordenes.length == 0:
      print("La cola de ordenes esta vacia...")
    else:
      for i in range(Ordenes.length()):
       print("\n---- ORDEN: ", i+1)
       print("Cliente: " +Ordenes[i].Nombre +" NIT: "+ Ordenes[i].NIT + " Timepo para la orden: " ,Ordenes[i].tiempo,"min")
       for j in range(Ordenes[i].Pizzas.length()):
        print("      Pizza" , Ordenes[i].Pizzas[j].noPizza , ": " +"Ingredientes: " + Ordenes[i].Pizzas[j].ingredients + " Tiempo de elavoracion : " , Ordenes[i].Pizzas[j].tiempo1,"min")


def entregar_orden():
  if Ordenes.length() == 0:
    generarGrafica(Ordenes)
  else:
    Ordenes.entregar_orden()
    print("Orden entrega...")
    generarGrafica(Ordenes)

def datosEstudent():# DATOS DE ESTUDIANTE 
    print("")
    print("---> Nombre: Ivan Alessandro Hilario Chacon")
    print("---> Carnet: 201902888")
    print("---> Curso: Introduccion a la Programación y Computación 2 Seccion \"C\"")
    print("---> Carrera: Ingenieria en Ciencias y Sistemas")
    print("")    

if __name__ == '__main__':
 global Ordenes
 Ordenes = Cola()

 print("--------- BIENVENIDO ---------")
 menuprincipal = input(
  "        Pizzeria "+emoji.emojize(":pizza:")+" \n------- MENU PRINCIPAL-------- \n 1- Agregar Orden  \n 2- Ver Ordenes \n 3- Entregar Orden  \n 4- Salir \n 5- Informacion del dessarrollador   \nPor favor elija una opcion: \n")
 while menuprincipal != "4":
 
  if menuprincipal == "1":
    addOrden()

  elif menuprincipal == "2":
    mostrar_Ordenes()

  elif menuprincipal == "3":
    entregar_orden()
  
  elif menuprincipal == "5":
    datosEstudent()

  else:
    print("Opcion ingresa invalida!")

  menuprincipal = input(
  "        Pizzeria "+emoji.emojize(":pizza:")+" \n------- MENU PRINCIPAL-------- \n 1- Agregar Orden  \n 2- Ver Ordenes \n 3- Entregar Orden  \n 4- Salir \n 5- Informacion del dessarrollador   \nPor favor elija una opcion: \n")


