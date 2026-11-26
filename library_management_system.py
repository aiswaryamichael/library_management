from idlelib import query

import mysql.connector
class Books:

    # CONNECTION
    def __init__(self):
        try:
            self.connection=mysql.connector.connect(user="root",password="root",host="localhost",database="library_management")
            self.cursor=self.connection.cursor()
            print("Connected")
        except:
            print("Connection Failed")


    def create(self,book_id,title,author,category,total_copies,available_copies):
        try:
            if total_copies< 0 or available_copies<0:
                print(" copies cannot be negative")
                return
            if available_copies>total_copies:
                print("available copies cannot exeed total copies")
                return

            query="insert into books(book_id,title,author,category,total_copies,available_copies)values(%s,%s,%s,%s,%s,%s)"
            data=(book_id,title,author,category,total_copies,available_copies)
            self.cursor.execute(query,data)
            self.connection.commit()
            print("Record Created")
        except:
            print("Creation Failed")

    def view(self):
        try:
            query="select * from books where available_copies>=1 order by title limit 20"
            self.cursor.execute(query)
            record=self.cursor.fetchall()

            if record:
                for row in record:
                    print(row)
            else:
                print("No Record Found")
        except:
            print("Viewing Failed")

    def search(self):
        try:
            print("1. search by Book ID\n2.Search by Title\n3. Search by Author ")
            ch=int(input("enter the search choice(1-3):"))

            if ch==1:
                try:
                    book_id=int(input("enter the book id :"))
                    query="select * from books where book_id=%s"
                    data=(book_id,)
                    self.cursor.execute(query,data)
                    record=self.cursor.fetchone()
                    if record:
                        print(record)
                    else:
                        print("No Record Found")
                except:
                    print("search by book id failed")

            elif ch==2:
                try:
                    title=input("enter the title :")
                    query="select * from books where title=%s"
                    data=(title,)
                    self.cursor.execute(query,data)
                    record=self.cursor.fetchone()
                    if record:
                        print(record)
                    else:
                        print("No Record Found")
                except:
                    print("search by title failed")

            elif ch==3:
                try:
                    author=input("enter the author :")
                    query="select * from books where author=%s"
                    data=(author,)
                    self.cursor.execute(query,data)
                    record=self.cursor.fetchone()
                    if record:
                        print(record)
                    else:
                        print("No Record Found")
                except:
                    print("search by title failed")
            else:
                print("Invalid search Choice")
        except:
            print("Searching Failed")

    def update(self,available_copies,book_id):
        try:
            if total_copies< 0 or available_copies<0:
                print("copies cannot be negative")
                return
            if available_copies>total_copies:
                print("available copies cannot exeed total copies")
                return
            query="update books set available_copies=%s where book_id=%s"
            data=(available_copies,book_id)
            self.cursor.execute(query,data)
            self.connection.commit()

            if self.cursor.rowcount>0:
                print("updated")
            else:
                print("no record found")
        except:
            print("update failed")

    def delete(self,book_id):
        try:
            query="delete from books where book_id=%s"
            data=(book_id,)
            self.cursor.execute(query,data)
            self.connection.commit()
            if self.cursor.rowcount>0:
                print("deleted")
            else:
                print("no record found")
        except:
            print("deletion failed")

    def summary(self):
        try:
            query="select count(*),sum(available_copies),avg(total_copies) from books"
            self.cursor.execute(query)
            record=self.cursor.fetchone()
            if record:
                print(record)
            else:
                print("no record found")
        except:
            print("Summary Failed")

B=Books()
while(True):
    print("1. Add Book\n2. View Available Books\n3. Search Book\n4.Update Available Copies\n5. Delete Book\n6. Library Summary\n7. Exit")
    ch=int(input("Enter your choice(1-7) :"))

    if ch==1:
        book_id=int(input("Book ID :"))
        title=input("Title :")
        author=input("Author :")
        category=input("Category :")
        total_copies=int(input("Total no of Copies :"))
        available_copies=int(input("Available no of Copies :"))
        B.create(book_id,title,author,category,total_copies,available_copies)

    elif ch==2:
        B.view()

    elif ch==3:
        B.search()

    elif ch==4:
        book_id=int(input("Enter Book ID :"))
        available_copies=int(input("Available no of Copies :"))
        B.update(available_copies,book_id)

    elif ch==5:
        book_id=int(input("Book ID :"))
        B.delete(book_id)

    elif ch==6:
        B.summary()

    elif ch==7:
        exit()
    else:
        print("Invalid Choice")






