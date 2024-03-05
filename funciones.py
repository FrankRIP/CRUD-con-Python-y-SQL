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
        if(int(creditos) > 0):
            creditosCorrectos = True
            creditos = int(creditos)
        else:
            print ("Los creditos debe ser mayor a 0.")
    else:
        print ("Creditos Incorrectos: Debe ingresar un numero")
    curso = (codigo, nombre, creditos)
    return curso



def pedirDatosActualizacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEditar = input ("Ingrese el codigo del curso a editar: ")
    for cur in cursos:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break
    if existeCodigo:
        nombre = input("Ingrese Nombre: ")
        
        creditosCorrectos = False
        while (not creditosCorrectos):
            creditos = input("Ingrese creditos a modificar: ")
            if creditos.isnumeric():
                if(int(creditos) > 0):
                    creditosCorrectos = True
                    creditos = int(creditos)
                else:
                    print ("Los creditos debe ser mayor a 0.")
            else:
                print ("Creditos Incorrectos: Debe ingresar un numero")
        curso = (codigoEditar, nombre, creditos)
    else:
        curso = None
    return curso
    
def pedirDatosEliminacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEliminar = input("Ingrese el codigo del curso a eliminar")
    for cur in cursos:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break
    if not existeCodigo:
        codigoEliminar = ""
    return codigoEliminar