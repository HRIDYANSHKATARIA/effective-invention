class book:
    def _init_(self,name,age,dob,id_no):
        self.book_name = name
        self.book_age = age
        self.book_dob = dob
        self.book_id_no = id_no
       
        
    def add_book(self):
        print("Name : "+self.book_name)
        print("Author : "+self.book_age)
        print("Price : "+self.book_dob)
        print("Published : "+self.book_id_no)
       
        
book1 = book("Harry Potter and Philosopher's Stone","J.K.Rowling,"1928","1997")
book1.add_book("Harry Potter and Philosopher's Stone","J.K.Rowling,"1928","1997")

book2 = book("The Diary Of A Wimpy Kid","Jeff Kinney","700","2017")
book2.add_book("Abc","10","2011","102")