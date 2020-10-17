import psycopg2

connection = psycopg2.connect(user = "postgres", password = "ams253526370", host = "127.0.0.1", port = "5432", database = "airport")
cursor = connection.cursor()

def conectar():
    try:
        cursor.execute("SELECT * FROM flights;")
        record = cursor.fetchall()
        print(record)
        print ("Conexion exitosa")

    except (Exception, psycopg2.Error) as error :
        print ("Error de conexión", error)

def desconectar():
    if connection:
        cursor.close()
        connection.close()
        print("Conexión terminada")


if __name__=="__main__":
    conectar()

    a = "n"
    while a != "y":
        a = input("Desea terminar la conexión (y/n): ")

    desconectar()
