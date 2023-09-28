import mysql.connector

con = mysql.connector.connect(host='localhost', database='pf_atividade2', user='root', password='root')
print("Conectado!")

tabela_author = """
    CREATE TABLE IF NOT EXISTS Author (
  `AuthorID` INT NOT NULL,
  `Name` NVARCHAR(45) NOT NULL,
  PRIMARY KEY (`AuthorID`))
"""

tabela_post = """
    CREATE TABLE IF NOT EXISTS Post (
  `PostID` INT NOT NULL,
  `Title` VARCHAR(45) NOT NULL,
  `Created` DATETIME NOT NULL,
  `Author_AuthorID` INT NOT NULL,
  PRIMARY KEY (`PostID`),
  INDEX `fk_Post_Author_idx` (`Author_AuthorID` ASC) VISIBLE,
  CONSTRAINT `fk_Post_Author`
    FOREIGN KEY (`Author_AuthorID`)
    REFERENCES `Author` (`AuthorID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
"""

cursor = con.cursor()
cursor.execute(tabela_author)
cursor.execute(tabela_post)

# funções

def create_author(author_id, nome):
    sql = "INSERT INTO Author (AuthorID, Name) VALUES (%s, %s)"
    val = (author_id, nome)
    cursor.execute(sql, val)
    con.commit()

def create_post(post_id, title, created, author_id):
    sql = "INSERT INTO Post (PostID, Title, Created, Author_AuthorID) VALUES (%s, %s, %s, %s)"
    val = (post_id, title, created, author_id)
    cursor.execute(sql, val)
    con.commit()

def read_authors():
    sql = "SELECT * FROM Author"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)

def read_posts():
    sql = "SELECT * FROM Post"
    cursor.execute(sql)
    result = cursor.fetchall() 
    for row in result:
        print(row)

def update_author(author_id, novo_nome):
    sql = "UPDATE Author SET Name = %s WHERE AuthorID = %s"
    val = (novo_nome, author_id)
    cursor.execute(sql, val)
    con.commit()

def update_post(post_id, novo_titulo):
    sql = "UPDATE Post SET Title = %s WHERE PostID = %s"
    val = (novo_titulo, post_id)
    cursor.execute(sql, val)
    con.commit()

def delete_author(author_id):
    sql = "DELETE FROM Author WHERE AuthorID = %s"
    val = (author_id,)
    cursor.execute(sql, val)
    con.commit()

def delete_post(post_id):
    sql = "DELETE FROM Post WHERE PostID = %s"
    val = (post_id,)
    cursor.execute(sql, val)
    con.commit()


cursor.close()
con.close()

options = ["c", "r", "u", "d"]
mensagem = """"
Siga os comandos abaixo para fazer o CRUD:

Digite C para criar um ator ou um post
Digite R para listar todos os atores ou posts
Digite U para atualizar o nome de um ator ou o título de um post
Digite D para deletar um ator ou um post

Ou digite E para sair do programa
"""

while True:

    user_choice = input(mensagem).lower()

    if user_choice == 'e':
        break

    if user_choice not in options:
        continue


    if user_choice == "c":
       
       authorid = input("Digite o nome do seu autor: ")
       nome = input("Digite o nome do autor: ")

       postid = input("Digite o ID do seu post: ")
       titulo = input("Digite título do seu post: ")

       create_author(authorid, nome)
       create_post(postid, titulo, "2023-09-11 10:00:00", authorid)

    elif  user_choice == "r":
        
        print("Autores:")
        read_authors()

        print("Posts:")
        read_posts()

    elif user_choice == "u":

        authorid = input("Digite o ID do autor que você deseja atualizar: ")
        nome = input("Digite o novo nome do autor: ")

        postid = input("Digite o ID do post que você deseja atualizar: ")
        titulo = input("Digite o novo título: ")

        update_author(authorid, nome)
        update_post(postid, titulo)

    elif user_choice == "d":
        
        authorid = input("Digite o ID do autor que você deseja deletar: ")
        postid = input("Digite o ID do post que você deseja atualizar: ")
        
        delete_author(postid)
        delete_post(authorid)
        
