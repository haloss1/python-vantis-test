import sqlite3


def get_header_id(uuid):
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        data = cur.execute(
            "SELECT id FROM Header WHERE identificador=(?)", (str(uuid),)
        ).fetchone()[0]
        return data


def insert_detail_into_db(idHeader, idCatalogo):
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO Detail (idHeader, idCatalogo) VALUES (?, ?)",
            (idHeader, idCatalogo),
        )
        con.commit()
        return cur.lastrowid
