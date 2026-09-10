from  abc import ABC,abstractmethod
import json

from sympy.codegen.ast import continue_


class Book:
    def __init__(self,book_id,title,author,total_num):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_num = total_num
        self.__available_num = total_num

    def borrow_books(self):
        if self.__available_num > 0:
            self.__available_num -=1
            return True
        return False

    def return_book(self):
        self.__available_num +=1

    def get_available_num(self):
        return self.__available_num


class Member(ABC):
    def __init__(self,member_id,name,password):
        self.member_id = member_id
        self.name = name
        self.__password = password
        self.__borrow_books = []

    def borrow_books(self,books:Book):
        if len(self.__borrow_books) >= self.get_max_books():
            print("You have borrowed the maximum number of books.")
            return False

        if books.borrow_books():
            self.__borrow_books.append(books)
            print(f"{self.name} has borrowed {books.title}")
            return True
        else:
            print(f"borrowing failed,the books {books.title}has been borrowed.")
            return False

    def return_books(self,books:Book):
        if books in self.__borrow_books:
            books.return_book()
            self.__borrow_books.remove(books)
            print(f"{self.name} has returned {books.title}")
            return True
        else:
            print(f"returning failed,{books.title} is not borrowed by {self.name}")
            return False

    def get_password(self):
        return self.__password

    def get_borrow_books(self):
        return self.__borrow_books

    @abstractmethod
    def get_max_books(self)->int:
        pass



class NormaMember(Member):
    def get_max_books(self) ->int:
        return 3

class VIPMember(Member):
    def __init__(self,member_id,name,password,vip_level):
        super().__init__(member_id,name,password)
        self.vip_level = vip_level

    def get_max_books(self) ->int:
        return 6 + self.vip_level



class LibrarySystem:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.current_number:Member|None = None

        self.load_books_data()
        self.load_member_data()

    def load_books_data(self):
        with open('data/books.json', 'r', encoding='utf-8') as f:
            books_data = json.load(f)
            for books in books_data:
                self.books[books['编号']] = Book(books['编号'], books['标题'], books['作者'], books['数量'])
            print("successfully loaded the books data")

    def load_member_data(self):
        with open('data/members.json', 'r', encoding='utf-8') as f:
            member_data = json.load(f)
            for member in member_data:
                if member['卡号'].startswith('N'):
                    self.members[member['卡号']] = NormaMember(member['卡号'], member['姓名'], member['密码'])
                elif member['卡号'].startswith('V'):
                    self.members[member['卡号']] = VIPMember(member['卡号'], member['姓名'], member['密码'], member['会员等级'])
            print("successfully loaded the member data")



    def login(self):
        while True:
            print("Logging in...")
            number_id = input("Enter your member ID: ")
            password = input("Enter your password: ")
            if number_id in self.members and self.members[number_id].get_password() == password:
                self.current_number = self.members[number_id]
                print(f"Welcome back, {self.current_number.name}!")
                return True
            else:
                print("Invalid member ID or password.")
                continue

    def borrow_books(self):
        for book in self.books.values():
            print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Available: {book.get_available_num()}")

        book_id = input("Enter the book ID you want to borrow: ")
        if book_id not in self.books:
            print("Invalid book ID.")
            return
        self.current_number.borrow_books(self.books[book_id])


    def return_books(self):
        borrow_books = self.current_number.get_borrow_books()
        print("You have borrowed the following books:")
        for book in borrow_books:
            print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")

        book_id = input("Enter the book ID you want to return: ")
        if book_id not in self.books:
            print("Invalid book ID.")
            return
        self.current_number.return_books(self.books[book_id])


    def show_and_borrow(self):
        borrow_books = self.current_number.get_borrow_books()
        if len(borrow_books) >0:
            print("You have borrowed the following books:")
            for book in borrow_books:
                print(f"Book ID: {book.book_id}, Title: {book.title}")
                return
        else:
            print("You have not borrowed any books.")

    def run(self):
        if self.login():
            while True:
                print("\n1.borrow books")
                print("\n2.return books")
                print("\n3.show and borrow")
                print("\n4.launch system")

                choice = input("enter your choice: ")
                match choice:
                    case "1":
                        self.borrow_books()
                    case "2":
                        self.return_books()
                    case "3":
                        self.show_and_borrow()
                    case "4":
                        print("bye bye")
                        break
                    case _:
                        print("Invalid choice. Please try again.")



if __name__ == "__main__":
    ls = LibrarySystem()
    ls.run()




