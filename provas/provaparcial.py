import mysql.connector

con = mysql.connector.connect(host='localhost', database='provaparcial', user='root', password='root')
print("Conectado!")

tabela_departamento = """CREATE TABLE IF NOT EXISTS Department (
  `DepartmentID` INT NOT NULL,
  `Name` NVARCHAR(45) NOT NULL,
  `Region` NVARCHAR(45) NOT NULL,
  PRIMARY KEY (`DepartmentID`));
"""

tabela_empregado = """CREATE TABLE IF NOT EXISTS Employee (
  `EmployeeID` INT NOT NULL,
  `Name` NVARCHAR(45) NOT NULL,
  `Birthday` DATETIME NOT NULL,
  `Salary` FLOAT(10,2) NOT NULL,
  `Job` NVARCHAR(45) NOT NULL,
  `DepartmentID` INT NOT NULL,
  PRIMARY KEY (`EmployeeID`),
  INDEX `DepartmentID_idx` (`DepartmentID` ASC) VISIBLE,
  CONSTRAINT `DepartmentID`
    FOREIGN KEY (`DepartmentID`)
    REFERENCES `Department` (`DepartmentID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
"""

cursor = con.cursor()
cursor.execute(tabela_departamento)
cursor.execute(tabela_empregado)

def menu():
    print("\nEscolha uma opção pelo número:")
    print("1. (C) Adicionar departamento")
    print("2. (R) Listar departamentos")
    print("3. (U) Atualizar departamento")
    print("4. (D) Deletar departamento")
    print("5. (C) Adicionar empregado")
    print("6. (R) Listar empregados")
    print("7. (U) Atualizar empregado")
    print("8. (D) Deletar empregado")
    print("9. Sair")


def create_department():
    department_id = int(input("ID do departamento: "))
    name = input("Nome do departamento: ")
    region = input("Região do departamento: ")

    query = "INSERT INTO Department (DepartmentID, Name, Region) VALUES (%s, %s, %s)"
    cursor.execute(query, (department_id, name, region))
    con.commit()
    print("Departamento adicionado com sucesso!")

def read_departments():
    cursor.execute("SELECT * FROM Department")
    departments = cursor.fetchall()

    print("\nDepartamentos:")
    for department in departments:
        print(f"ID: {department[0]}, Nome: {department[1]}, Região: {department[2]}")

def update_department():
    department_id = int(input("ID do departamento a ser atualizado: "))
    new_name = input("Novo nome do departamento: ")
    new_region = input("Nova região do departamento: ")

    query = "UPDATE Department SET Name = %s, Region = %s WHERE DepartmentID = %s"
    cursor.execute(query, (new_name, new_region, department_id))
    if cursor.rowcount == 0:
        print("Nenhum departamento com esse ID encontrado.")
    else:
        print("Departamento atualizado com sucesso!")

    con.commit()

def delete_department():
    department_id = int(input("ID do departamento a ser excluído: "))

    query = "DELETE FROM Department WHERE DepartmentID = %s"
    cursor.execute(query, (department_id,))
    if cursor.rowcount == 0:
        print("Nenhum departamento com esse ID encontrado.")
    else:
        print("Departamento excluído com sucesso!")

    con.commit()

def create_employee():
    employee_id = int(input("ID do empregado: "))
    name = input("Nome do empregado: ")
    birthday = input("Data de nascimento (YYYY-MM-DD): ")
    salary = float(input("Salário: "))
    job = input("Cargo: ")
    department_id = int(input("ID do departamento (DepartmentID): "))

    query = "INSERT INTO Employee (EmployeeID, Name, Birthday, Salary, Job, DepartmentID) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (employee_id, name, birthday, salary, job, department_id))
    print("Empregado adicionado com sucesso!")

    con.commit()

def read_employees():
    cursor.execute("SELECT * FROM Employee")
    employees = cursor.fetchall()

    print("\nEmpregados:")
    for employee in employees:
        print(f"ID: {employee[0]}, Nome: {employee[1]}, Data de Nascimento: {employee[2]}, Salário: {employee[3]}, Cargo: {employee[4]}, DepartmentID: {employee[5]}")

def update_employee():
    employee_id = int(input("ID do empregado a ser atualizado: "))
    name = input("Novo nome do empregado: ")
    birthday = input("Nova data de nascimento (YYYY-MM-DD): ")
    salary = float(input("Novo salário: "))
    job = input("Novo cargo: ")
    department_id = int(input("Novo ID do departamento (DepartmentID): "))

    query = """ UPDATE Employee SET Name = %s, Birthday = %s, Salary = %s, Job = %s, DepartmentID = %s WHERE EmployeeID = %s """
    cursor.execute(query, (name, birthday, salary, job, department_id, employee_id))
    if cursor.rowcount == 0:
        print("Nenhum empregado com esse ID encontrado.")
    else:
        print("Dados do empregado atualizados com sucesso!")

    con.commit()

def delete_employee():

    employee_id = int(input("ID do empregado a ser excluído: "))

    query = "DELETE FROM Employee WHERE EmployeeID = %s"
    cursor.execute(query, (employee_id,))
    if cursor.rowcount == 0:
        print("Nenhum empregado com esse ID encontrado.")
    else:
        print("Empregado excluído com sucesso!")

    con.commit()

while True:
    menu()
    opcao = input("Opção: ")

    if opcao == '1':
        create_department()
    elif opcao == '2':
        read_departments()
    elif opcao == '3':
        update_department()
    elif opcao == '4':
        delete_department()
    elif opcao == '5':
        create_employee()
    elif opcao == '6':
        read_employees()
    elif opcao == '7':
        update_employee()
    elif opcao == '8':
        delete_employee()
    elif opcao == '9':
        break
    else:
        print("Opção inválida!")

con.close()
