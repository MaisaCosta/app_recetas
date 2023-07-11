from app_recetas.config.mysqlconnection import connectToMySQL
from app_recetas import BASE_DATOS
from flask import flash 


class Receta:
    def __init__( self, data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.descripcion = data['descripcion']
        self.instrucciones = data['instrucciones']
        self.fecha_elaboracion = data['fecha_elaboracion']
        self.menos_trienta = data['menos_trienta']
        self.id_usuario = data['id_usuario']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion']

@classmethod
def crear_uno( cls, data):
    query = """
            INSERT INTO recetas ( nombre, descripcion, instrucciones, fecha_elaboracion, menos_trienta, id_usuario)
            VALUES ( %(nombre)s, %(descripcion)s, %(instrucciones)s, %(fecha_elaboracion)s, %(menos_trienta)s, %(id_usuario')s,);
            """
    id_receta = connectToMySQL( BASE_DATOS).query_db( query, data)
    return id_receta