import sqlite3

conn = sqlite3.connect("livros_progresso.db")

cur = conn.cursor()

cur.execute("""
CREATE TABLE Livros(
  Id INTEGER NOT NULL PRIMARY KEY,
  Nome TEXT NOT NULL,
  Autor TEXT NOT NULL,
  Quantidade_de_Paginas TEXT NOT NULL,
  Quantidade_de_Capitulos TEXT NOT NULL,
  Genero TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE Pessoas(
  Id INTEGER NOT NULL PRIMARY KEY,
  Nome TEXT NOT NULL,
  Sobrenome TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE Progresso_Livro_Pessoa(
  Id INTEGER NOT NULL PRIMARY KEY,
  Livro_Id INTEGER NOT NULL,
  Pessoa_Id INTEGER NOT NULL,
  Paginas_Lidas INTEGER NOT NULL,
  Capitulos_Lidos INTEGER NOT NULL,
  Percentual_Lido INTEGER NOT NULL
  FOREIGN KEY (Livro_Id)
    REFERENCES Livros (Id)
      ON DELETE CASCADE
      ON UPDATE NO ACTION,
  FOREIGN KEY (Pessoa_Id)
    REFERENCES Pessoas (Id)
      ON DELETE CASCADE
      ON UPDATE NO ACTION,
)
""")

cur.execute("""
INSERT INTO Livros VALUES
  ('Sherlock - 1','Árthur Conan Doyle', 250, 10,'Romance'),
  ('Sherlock - 2','Árthur Conan Doyle', 250, 10,'Romance'),
  ('Sherlock - 3','Árthur Conan Doyle', 250, 10,'Romance'),
  ('Sherock - 4','Árthur Conan Doyle', 250, 10,'Romance')
""")

cur.execute("""
INSERT INTO Pessoas VALUES
  ('Maria', 'Janovicci'),
  ('Rafael', 'Gomes')
""")

cur.execute("""
INSERT INTO Progresso_Livro_Pessoa VALUES
  (1,1,50,2,20),
  (2,1,100,4,40),
  (1,2,25,1,10)
""")

conn.commit()

cur.execute("""
UPDATE Livros
SET Nome = 'Sherock - 4' WHERE Id = 4
""")

res = cur.execute("SELECT * FROM Progresso_Livro_Pessoa WHERE Pessoa_Id = 1 AND Livro_Id = 1")
res.fetchall()

conn.close()
