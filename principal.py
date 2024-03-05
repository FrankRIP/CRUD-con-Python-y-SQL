from BD.conexion import DAO
import funciones

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("========== Menù Principal ==========")
            print("1.- Listar Cursos ")
            print("2.- Registrar Cursos")
            print("3.- Actualizar Cursos")
            print("4.- Eliminar Cursos")
            print("5.- Salir")
            print("====================================")
            opcion = int(input("Seleccione una opcion por favor: "))
            
            if opcion < 1 or opcion >5:
                print("Opcion incorrecta, ingrese nuevamente por favor...")
            elif opcion == 5:
                continuar = False
                print ("Gracias por usar este sistema")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = DAO()
    
    if opcion == 1:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                funciones.listarCursos()
            else:
                print("No se encontraron cursos")
        except: 
            print("Ocurrio un error(Listado)")
    elif opcion == 2:
        curso = funciones.pedirDatosCurso()
        try:
            dao.registrarCurso(curso)
        except:
            print ("Ocurso un error(Registro)")
    elif opcion == 3:
        try:
            cursos = dao.listarCursos()
            if len (cursos) > 0:
                curso = funciones.pedirDatosActualizacion(cursos)
                if curso:
                    dao.actualizarCurso
                else:
                    print("Codigo de curso a actualizar no encontrado \n")
            else:
                print("No se econtraron cursos")
        except:  
            print ("Ocurrio un error(Actualizacion)")  
    elif opcion == 4:
        try:
            cursos = dao.conexion()
            if len(cursos) > 0:
                codigoEliminar = funciones.pedirDatosEliminacion(cursos)
                if not(codigoEliminar == ""):
                    dao.eliminarCurso(codigoEliminar)
                else:
                    print("Codigo de curso no encontrado.. \n")
        except:
            print ("Ocurso un error(Eliminar)")
    else:print("Opcion no valida...")
        

    
menuPrincipal()