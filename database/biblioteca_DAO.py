from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_tutte_biblioteche(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT * FROM biblioteca"
            cursor.execute(query)
            for row in cursor:
                b = Biblioteca(row["id"], row["nome"], row["indirizzo"])
                result.append(b)
            cursor.close()
            cnx.close()
        return result

    def get_tutti_generi(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL AND genere != ''"
            cursor.execute(query)
            for row in cursor:
                result.append(row["genere"])
            cursor.close()
            cnx.close()
        return result
