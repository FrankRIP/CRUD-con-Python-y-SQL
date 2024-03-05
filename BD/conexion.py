import mysql.connector #importo la libreria para poder conectarme a la base de datos
from mysql.connector import Error


class DAO():
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='universidad'
            )
        except Error as ex:
            print ("Error al intentar la conexion: {0}".format(ex))
            
    def listarCursos(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM curso ORDER BY nombre ASC")
            except Error as ex:
                print ("Error al intentar la conexion: {0}".format(ex))
            
    def registarCurso (self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursos()
                sql = "INSERT INTO curso (codigo, nombre, creditos) VALUES ('{0}', '{1}', {2})"
                cursor.execute(sql.format(cursor[0], curso[1], curso[2]))
                self.conexion.commit()
                print("¡Curso Registrado!")
            except Error as ex:
                print ("Error al intentar la conexion: {0}".format(ex))