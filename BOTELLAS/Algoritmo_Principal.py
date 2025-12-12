from Botellas_plastico import Botella_Plastico
from Botellas_vidrio import Botella_Vidrio
from Botella import Botella
from Base_Datos import Base_datos

def menu():
    print("--- MENÚ BOTELLAS ---")
    print("1. agregar botella de plástico")
    print("2. agregar botella de vidrio")
    print("3. agregar botella normal")
    print("4. ver todas las botellas registradas")
    print("5. eliminar una botella")
    print("6. Salir")
    opcion = input("Elige una opción: ")
    return opcion

def main():
    while True:
        opcion = menu()

        if opcion == "1":
            botella_plastico = Botella_Plastico("1L", "Cilíndrica", "Lisa", "normal")
            print("Botella Plastico:")
            botella_plastico.mostrar_atributos()
            print("-----------------------------------")
            botella_plastico.contener_liquidos()
            botella_plastico.transparencia()
            botella_plastico.reutilizar()

        elif opcion == "2":
            botella_vidrio = Botella_Vidrio("750ml", "Recta", "elegante", "Corcho")
            print("Botella Vidrio:")
            botella_vidrio.mostrar_atributos()
            print("-----------------------------------")
            botella_vidrio.contener_liquidos()
            botella_vidrio.bebidas_calientes()
            botella_vidrio.fragilidez()

        elif opcion == "3":
            obj_botella = Botella("normal","2 L","circular","deportivo", "normal", )
            print("Botella Normal:")
            obj_botella.mostrar_atributos()
            print("------------------------------------")
            obj_botella.contener_liquidos()
            obj_botella.cierre_hermetico()
            obj_botella.facilitar_vertido()

        elif opcion == "4":
            Base_datos.imprimir_info()

        elif opcion == "5":
            if not Base_datos.lista_botellas:
                print("No hay botellas para eliminar.")
            else:
                Base_datos.imprimir_info()
                try:
                    indice = int(input("Ingresa el número de la botella que deseas eliminar: "))
                    if 1 <= indice <= len(Base_datos.lista_botellas):
                        eliminada = Base_datos.lista_botellas.pop(indice - 1)
                        print(f"Botella eliminada: {eliminada.material} - {eliminada.capacidad}")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Por favor ingresa un número válido.")

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


main()