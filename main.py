from iu.menu_principal import menu_principal


def main():
    verdadero = True
    while verdadero:
        print()
        menu_principal()
        print()
        opcion = input("Seleccione su opción [0-3]: ")
        if opcion == '1':
            pass
        elif opcion == '2':
            pass
        elif opcion == '3':
            pass
        elif opcion == '0':
            print("Saliendo del sistema...")
            print("Hasta pronto.")
            verdadero = False
        else:
            print("Opción no corresponde, ingrese nuevamente.")

main()


