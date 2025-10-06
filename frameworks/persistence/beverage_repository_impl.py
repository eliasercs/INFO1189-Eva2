from entities.beverage import Bebida
from adapters.gateways.beverage_repository import BebidaRepository
from adapters.presenters.beverage_presenter import BebidaPresenter
import mysql.connector
from typing import List, Optional

class BebidaRepositoryImpl(BebidaRepository):  # ← Implementa CON MySQL
    def __init__(self, db_connection):
        self.db = db_connection  # ← Conexión real a MySQL
    
    def guardar(self, bebida: Bebida) -> Bebida:
        # ✅ Aquí SÍ hay código de base de datos
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO bebidas (codigo, nombre, precio, stock) VALUES (%s, %s, %s, %s)",
            (bebida.codigo, bebida.nombre, bebida.precio, bebida.stock)
        )
        self.db.commit()
        
        # Obtener el ID generado
        bebida.id = cursor.lastrowid
        return bebida
    
    def obtener_bebida_por_id(self, id: int) -> Bebida:
        query = """SELECT 
            b.*,
            c.id as categoria_id,
            c.nombre as categoria_nombre,
            c.tipo_grado as categoria_tipo_grado,
            c.restriction_edad as categoria_restriction_edad,
            g.id as grado_alcohol_id,
            g.nombre as grado_alcohol_nombre,
            g.description as grado_alcohol_description,
            g.horario_limite_venta as grado_alcohol_horario_limite
        FROM bebidas b
        LEFT JOIN categorias c ON b.categoria_id = c.id
        LEFT JOIN grados_alcohol g ON c.tipo_grado = g.id WHERE b.id = %s;"""
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(query, (id,))
        fila = cursor.fetchone()
        
        return BebidaPresenter.present_bebida_completa(fila)
    
    def obtener_bebidas(self):
        query = """SELECT 
            b.*,
            c.id as categoria_id,
            c.nombre as categoria_nombre,
            c.tipo_grado as categoria_tipo_grado,
            c.restriction_edad as categoria_restriction_edad,
            g.id as grado_alcohol_id,
            g.nombre as grado_alcohol_nombre,
            g.description as grado_alcohol_description,
            g.horario_limite_venta as grado_alcohol_horario_limite
        FROM bebidas b
        LEFT JOIN categorias c ON b.categoria_id = c.id
        LEFT JOIN grados_alcohol g ON c.tipo_grado = g.id;"""
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(query)
        data = cursor.fetchall()
        
        bebidas = [BebidaPresenter.present_bebida_completa(bebida) for bebida in data]
        
        return bebidas
    
    def actualizar(self, bebida: Bebida) -> Optional[Bebida]:
        """
        PUT - Actualiza TODOS los campos de una bebida
        """
        cursor = self.db.cursor()
        try:
            cursor.execute(
                """UPDATE bebidas SET 
                   codigo=%s, nombre=%s, marca=%s, precio=%s, stock=%s, 
                   categoria_id=%s, updated_at=NOW() 
                   WHERE id=%s""",
                (bebida.codigo, bebida.nombre, bebida.marca, bebida.precio,
                 bebida.stock, bebida.categoria_id, bebida.id)
            )
            self.db.commit()
            
            if cursor.rowcount == 0:
                return None  # No se actualizó ninguna fila
                
            return self.obtener_bebida_por_id(bebida.id)
            
        except mysql.connector.Error as e:
            self.db.rollback()
            raise Exception(f"Error al actualizar bebida: {str(e)}")
        finally:
            cursor.close()
            
    def actualizar_stock(self, bebida_id: int, nuevo_stock: int) -> Optional[Bebida]:
        """
        Actualiza solo el stock de una bebida
        """
        cursor = self.db.cursor()
        try:
            cursor.execute(
                "UPDATE bebidas SET stock = %s, updated_at = NOW() WHERE id = %s",
                (nuevo_stock, bebida_id)
            )
            self.db.commit()
        
            if cursor.rowcount == 0:
                return None  # No se encontró la bebida
            
            # Devolver la bebida actualizada
            return self.obtener_bebida_por_id(bebida_id)
        
        except mysql.connector.Error as e:
            self.db.rollback()
            raise Exception(f"Error al actualizar stock: {str(e)}")
        finally:
            cursor.close()
            
    def eliminar(self, bebida_id: int) -> bool:
        """
        DELETE - Elimina una bebida por ID
        """
        cursor = self.db.cursor()
        try:
            cursor.execute("DELETE FROM bebidas WHERE id = %s", (bebida_id,))
            self.db.commit()
            return cursor.rowcount > 0  # True si eliminó, False si no existía
            
        except mysql.connector.Error as e:
            self.db.rollback()
            raise Exception(f"Error al eliminar bebida: {str(e)}")
        finally:
            cursor.close()