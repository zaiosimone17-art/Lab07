from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_libri_filtrati(self, id_biblioteca=None, genere=None):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)

            query = """
                SELECT * FROM libro 
                WHERE (%s IS NULL OR id_biblioteca = %s)
                  AND (%s IS NULL OR genere = %s)
            """

            cursor.execute(query, (id_biblioteca, id_biblioteca, genere, genere))
            for row in cursor:
                l = Libro(
                    row["id"],
                    row["titolo"],
                    row["autore"],
                    row["genere"],
                    row["anno_pubblicazione"],
                    row["id_biblioteca"]
                )
                result.append(l)

            cursor.close()
            cnx.close()
        return result
