"""
Tital  : mysql connectio nprogram
Autor  : Akshay unde
Date   : 7/1/2020
"""


import mysql.connector

con = mysql.connector.connect(host="localhost" , user="root", password = "root", database = "don")

mycursor = con.cursor()

for i in mycursor:
	print(i)