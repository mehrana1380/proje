import sqlite3

query= 'insert into phonebook values ("{}", "{}")'
full_name=""
while full_name != "exit" :
    full_name=input("enter a name:\n")

    phone=int(input("enter a phone number:\n"))

    cursor.execute(query.format(full_name, phone))

connection.commit()
connection.close()

commend=1
while commend != 0:
    commend=iput("what do you want?\n")
    if commend== "add":
        query= 'insert into phonebook values ("{}", "{}")'
        full_name=input("enter a name:\n")
        phone=int(input("enter a phone number:\n))
        print(append.full_name())
        print(append.phone())

    if commend== "remove":
        query= 'insert into phonebook values ("{}", "{}")'
        full_name=input("enter a name:\n")
        phone=int(input("enter a phone number:\n))
        print(remove.full_name())
        print(remove.phone())

    if commend== "show_all":
        query_2= 'select * from phonebook'



connection= sqlite3.connection("proje.db")
connection.close()
