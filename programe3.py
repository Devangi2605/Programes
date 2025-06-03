'''
Build a contact book
'''

import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="12345", database="trainee")

cur=db.cursor()

cur.execute("CREATE TABLE Contact (S_No int primary key, FirstName varchar(30) not null, LastName varchar(40) not null, PhoneNumber int unique, Email_Id varchar(40) unique, Place_of_Birth varchar(30) not null)")

def insert_contact():
    S_No = int(input("Enter Number: "))
    F_Name = input("Enter First Name: ")
    L_Name = input("Enter Last Name: ")
    Phone_No = int(input("Enter Phone number: "))
    Email_ID = input("Enter Email ID: ")
    Place_of_Birth = input("Enter place of birth: ")
    sql = "INSERT INTO Contact(S_No, FirstName, LastName, PhoneNumber, Email_Id, Place_of_Birth) VALUES (%s, %s, %s, %s, %s, %s)"
    cur.execute(sql, (S_No, F_Name, L_Name, Phone_No, Email_ID, Place_of_Birth))
    db.commit()
    print("Contact Added Successfully")
    
def view_contact():
    cur.execute("Select * from Contact")
    rows=cur.fetchall()
    for row in rows:
        print(row)
        
def delete_contact():
    S_No=int(input("Enter S.No of contact to delete: "))
    cur.execute("Delete from Contact where S_No=%s", (S_No,))
    db.commit()
    print("Contact Deleted Successfully")
    
def search_contact():
    F_Name=input("Enter First Name to search: ")
    cur.execute("SELECT * FROM Contact WHERE FirstName=%s", (F_Name,))
    rows=cur.fetchall()
    for row in rows:
        print(row)

def update_contact():
    S_No=int(input("Enter S.No of contact to update: "))
    F_Name=input("Enter First Name to update: ")
    L_Name=input("Enter Last Name to update: ")
    Phone_No=int(input("Enter Phone number to update: "))
    Email_ID=input("Enter Email ID to update: ")
    Place_of_Birth=input("Enter place of birth to update: ")
    cur.execute("UPDATE Contact SET FirstName=%s, LastName=%s, PhoneNumber=%s, Email_Id=%s, Place_of_Birth=%s WHERE S_No=%s", (F_Name, L_Name, Phone_No, Email_ID, Place_of_Birth, S_No))
    db.commit()
    print("Contact Updated Successfully")
    
while True:
    print("1.Insert Contact")
    print("2.View Contact")
    print("3.Delete Contact")
    print("4.Search Contact")
    print("5.Update Contact")
    print("6.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        insert_contact()
    elif choice==2:
        view_contact()
    elif choice==3:
        delete_contact()
    elif choice==4:
        search_contact()
    elif choice==5:
        update_contact()
    elif choice==6:
        break
    else:
        print("Invalid choice. Please try again.")

        
                
    

            
