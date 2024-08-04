import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()



def push(date, name, lesson, course, typo):
    connection = mysql.connector.connect(
    user = os.getenv('USER'),
    password = os.getenv('PASSWORD'),
    host = os.getenv('HOST'),
    database = os.getenv('DATABASE')
    )
    with connection as conn:
        if lesson == "Русский язык":
            cursor = conn.cursor()
            query = (f"INSERT INTO russian (datatime, autor, lesson, course, typo) VALUES ('{date}', '{name}', '{lesson}', '{course}', '{typo}')")
            cursor.execute(query)
        elif lesson == "Математика":
            cursor = conn.cursor()
            query = (f"INSERT INTO math (datatime, autor, lesson, course, typo) VALUES ('{date}', '{name}', '{lesson}', '{course}', '{typo}')")
            cursor.execute(query)
        elif lesson == "Информатика":
            cursor = conn.cursor()
            query = (f"INSERT INTO informath (datatime, autor, lesson, course, typo) VALUES ('{date}', '{name}', '{lesson}', '{course}', '{typo}')")
            cursor.execute(query)
        elif lesson == "Физика":
            cursor = conn.cursor()
            query = (f"INSERT INTO physics (datatime, autor, lesson, course, typo) VALUES ('{date}', '{name}', '{lesson}', '{course}', '{typo}')")
            cursor.execute(query)
        elif lesson == "История":
            cursor = conn.cursor()
            query = (f"INSERT INTO history_ (datatime, autor, lesson, course, typo) VALUES ('{date}', '{name}', '{lesson}', '{course}', '{typo}')")
            cursor.execute(query)
        elif lesson == "Обществознание":
            cursor = conn.cursor()
            query = (f"INSERT INTO social (datatime, autor, lesson, course, typo) VALUES ('{date}', '{name}', '{lesson}', '{course}', '{typo}')")
            cursor.execute(query)
        elif lesson == "Английский язык":
            cursor = conn.cursor()
            query = (f"INSERT INTO english (datatime, autor, lesson, course, typo) VALUES ('{date}', '{name}', '{lesson}', '{course}', '{typo}')")
            cursor.execute(query)
        elif lesson == "Биология":
            cursor = conn.cursor()
            query = (f"INSERT INTO bio (datatime, autor, lesson, course, typo) VALUES ('{date}', '{name}', '{lesson}', '{course}', '{typo}')")
            cursor.execute(query)
        elif lesson == "Химия":
            cursor = conn.cursor()
            query = (f"INSERT INTO chemistry (datatime, autor, lesson, course, typo) VALUES ('{date}', '{name}', '{lesson}', '{course}', '{typo}')")
            cursor.execute(query)
        elif lesson == "Digital Skills":
            cursor = conn.cursor()
            query = (f"INSERT INTO digital_skills (datatime, autor, lesson, course, typo) VALUES ('{date}', '{name}', '{lesson}', '{course}', '{typo}')")
            cursor.execute(query)
        connection.commit()
        cursor.close()

# async def create_table():
#     with connection as conn:
#         query = """CREATE TABLE IF NOT EXISTS chemistry ( datatime text, autor text, lesson text, course text, typo text ); 
# CREATE TABLE IF NOT EXISTS bio ( datatime text, autor text, lesson text, course text, typo text ); 
# CREATE TABLE IF NOT EXISTS english ( datatime text, autor text, lesson text, course text, typo text ); 
# CREATE TABLE IF NOT EXISTS social( datatime text, autor text, lesson text, course text, typo text );
# CREATE TABLE IF NOT EXISTS history_( datatime text, autor text, lesson text, course text, typo text );
# CREATE TABLE IF NOT EXISTS russian( datatime text, autor text, lesson text, course text, typo text );
# CREATE TABLE IF NOT EXISTS math( datatime text, autor text, lesson text, course text, typo text );
# CREATE TABLE IF NOT EXISTS informath( datatime text, autor text, lesson text, course text, typo text );
# CREATE TABLE IF NOT EXISTS physics( datatime text, autor text, lesson text, course text, typo text );
# CREATE TABLE IF NOT EXISTS digital_skills( datatime text, autor text, lesson text, course text, typo text );"""
#         cursor = conn.cursor()
#         cursor.execute(query)
#         cursor.close()
#         return