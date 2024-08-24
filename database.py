import sqlite3

def connect():
    conn = sqlite3.connect('church.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Membro (
            ID INTEGER PRIMARY KEY,
            NomeCompleto TEXT,
            Endereco TEXT,
            Telefone TEXT,
            Email TEXT,
            DataNascimento TEXT,
            DataBatismo TEXT,
            DataCasamento TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert(nome, endereco, telefone, email, data_nascimento, data_batismo, data_casamento):
    conn = sqlite3.connect('church.db')
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Membro (NomeCompleto, Endereco, Telefone, Email, DataNascimento, DataBatismo, DataCasamento)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (nome, endereco, telefone, email, data_nascimento, data_batismo, data_casamento))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('church.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Membro')
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('church.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM Membro WHERE ID=?', (id,))
    conn.commit()
    conn.close()

def update(id, nome, endereco, telefone, email, data_nascimento, data_batismo, data_casamento):
    conn = sqlite3.connect('church.db')
    cur = conn.cursor()
    cur.execute('''
        UPDATE Membro SET NomeCompleto=?, Endereco=?, Telefone=?, Email=?, DataNascimento=?, DataBatismo=?, DataCasamento=?
        WHERE ID=?
    ''', (nome, endereco, telefone, email, data_nascimento, data_batismo, data_casamento, id))
    conn.commit()
    conn.close()
    