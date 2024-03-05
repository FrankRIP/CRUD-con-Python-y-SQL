def listarCursos(cursos):
    print("\nCursos: \n")
    contador = 1
    for cur in cursos:
        datos = "{0}. Codigo: {1} Nombre: {2} ({3} creditos)"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
    print (" ")
    
def pedirDatosCurso():
    codigoCorrecto = False
    while(not codigoCorrecto):
        codigo = input("Ingrese codigo: ")
        if len(codigo) == 6:
            codigoCorrecto = True
        else:
            print("Codigo Incorrecto: debe tener 6 digitos obligatoriamente")
    nombre = input("Ingrese Nombre: ")
    
    creditosCorrectos = False
    creditos = input("Ingrese creditos")
    if creditos.isnumeric():
        creditosCorrectos = True
        creditos = int(creditos)
    else:
        print ("Creditos Incorrectos: Debe ingresar un numero")
    curso = (codigo, nombre, creditos)
    return curso