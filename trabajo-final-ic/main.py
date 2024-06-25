"""
Trabajo Final - IC.
https://github.com/NicRiv/trabajo-final-ic

UNRN
Rivera, Nicolás.
"""

# Función principal
def main() -> None:
    # Inicializa variable de recuento de piezas
    total_de_piezas : int = 0
    
    while True: # primer ciclo
        ### Sección Pieza ###
        print('Ingrese el código de la pieza.')
        codigo_de_pieza : str = input('> ') # se asigna la entrada a la variable CP.
        if not codigo_valido(codigo_de_pieza):
            # Error: la entrada ingresada no es válida.
            print('Código no valido.\n')
    
        else:
            # La entrada es valida, se procesa el valor como tipo entero.
            codigo_de_pieza : int = int(codigo_de_pieza)
            
            if codigo_de_pieza != 0:
                # Inicializa variable del precio de la pieza
                precio_de_la_pieza : int = 0
                # Muestra por pantalla el valor del codigo de la pieza
                print(f'el codigo es: {codigo_de_pieza}')
                
                while True: # segundo ciclo
                    ### Sección Componente ###
                    print('Ingrese el código del componente.')
                    codigo_de_componente : str = input('> ') # Se asigna el valor de entrada a la variable CC.
                    
                    if not componente_valido(codigo_de_componente, codigo_de_pieza):
                        try:
                            # Prueba si corresponde al valor 0, sino error.
                            int(codigo_de_componente)
                            if int(codigo_de_componente) == 0:
                                # La entrada es 0, finaliza el recuento de componentes
                                if precio_de_la_pieza != 0:
                                    total_de_piezas += 1 # Agrega nueva pieza
                                print(f'El precio de la pieza es: {precio_de_la_pieza}.\n')
                                break
                            
                            else:
                                # la entrada no corresponde a un numero
                                # Error: la entrada ingresada no es válida.
                                print('Componente no valido.\n')    
                        except ValueError:
                            # la entrada no corresponde a un numero
                            # Error: la entrada ingresada no es válida.
                            print('Componente no valido.\n')
                        
                    else:
                        # La entrada es valida, se procesa como tipo entero
                        codigo_de_componente : int = int(codigo_de_componente)
                        
                        if codigo_de_componente != 0:
                            print(f'El código del componente es: {codigo_de_componente}')

                            while True: # tercer ciclo                            
                                # Sección precio del componente
                                print('Ingrese el precio del componente.')
                                precio_del_componente : str = input('> ')
                                
                                if not precio_valido(precio_del_componente):
                                    # Error: la entrada ingresada no es válida.
                                    print('Precio no valido.\n')
                                    
                                # se ingresa precio valido, pasa a un nuevo componente
                                else:
                                    precio_del_componente : float = float(precio_del_componente)
                                    precio_de_la_pieza += precio_del_componente
                                    break
                                                            
            # finaliza programa al ingresar 0 como valor de entrada
            else:
                print(f'El total de las piezas procesadas es de: {total_de_piezas}')
                break


# Subprocesos
def codigo_valido(codigo: str, componente: bool = False) -> bool:
    if codigo.isnumeric():
        # Se valida el código de pieza
        if not componente:
            if int(codigo) >= 0 and int(codigo) <= 99:
                return True
        
        # Se valida el código de componente
        else:
            if int(codigo) >= 101 and int(codigo) <= 9999:
                return True
    
    # No pasa los requisitos de validación.
    return False

def componente_valido(codigo: str, pieza: int) -> bool:
    if codigo_valido(codigo, True):
        if int(codigo) % pow(10, len(str(pieza))) == pieza:
            # El código del componente corresponde a la pieza
            return True
    
    # No pasa los requisitos de validación.
    return False
        

def precio_valido(precio: str) -> bool:
    try:
        float(precio)
        if float(precio) >= 10 and float(precio) <= 999.99:
            # La entrada es de tipo flotante y se encuentra entre el rango.
            return True
        
        # No pasa los requisitos de validación.
        else:
            return False
        
    # No pasa los requisitos de validación.    
    except ValueError:
        return False

if __name__ == '__main__':
    main()