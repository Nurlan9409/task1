from database import Database

class Country:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def insert(self, table):
        query = f"""INSERT INTO {table:country'}(name, date) VALUES('{self.name}', '{self.date}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table:country};"""
        return Database.connect(query, "select")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table:country} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table:"country} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class City(Country):
    def __init__(self,name,country_id,last_update):
        super().__init__(name,country_id)

        self.country_id = country_id
        self.last_update = last_update

    def insert(self, table="city"):
        query = f"""INSERT INTO {table}(name, date,country_id) VALUES('{self.name}', '{self.date}', '{self.country_id}')"""
        return Database.connect(query, "insert")




class Adress(Country):
    def __init__(self,name,city_id,last_update):
        super().__init__(name)

        self.city_id =city_id
        self.last_update = last_update

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,city_id) VALUES('{self.name}', '{self.city_id}')"""
        return Database.connect(query, "insert")




class User:
    def __init__(self,first_name, last_name,username,password,gmail,create_date,last_update):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.gmail = gmail
        self.create_date = create_date
        self.last_update =last_update


    def insert(self, table):
        query = f"""INSERT INTO {table}(first_name,last_name,username,password,gmail) VALUES('{self.first_name}', '{self.last_name}', '{self.user_name}','{self.password}','{self.gmail}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")




class Student(User):
    def __init__(self,first_name, last_name,username,password,gmail,create_date,last_update,balance,course_id):
        super().__init__(first_name,last_name,username,password,gmail,create_date,last_update)
        self.balance = balance
        self.course_id = course_id




    def insert(self, table):
        query = f"""INSERT INTO {table}(first_name,last_name,username,password,gmail,balance,course_id) VALUES('{self.first_name}', '{self.last_name}', '{self.user_name}','{self.password}','{self.gmail}','{self.balance}','{self.course_id}')"""
        return Database.connect(query, "insert")




class Mentor(User):
    class User:
        def __init__(self, first_name, last_name, username, password, gmail, status,create_date, last_update):
            super().__init__(first_name,last_name,username,password,gmail,create_date,last_update)
            self.status = status

        def insert(self, table):
            query = f"""INSERT INTO {table}(first_name,last_name,username,password,gmail,status) VALUES('{self.first_name}', '{self.last_name}', '{self.user_name}','{self.password}','{self.gmail}','{self.sattus}')"""
            return Database.connect(query, "insert")




class Course:
    def __init__(self,title,description,reyting,price,price_status,language,create_date,last_update):
        self.title = title
        self.description =description
        self.reyting = reyting
        self.price = price
        self.price_status = price_status
        self.language = language
        self.create_date = create_date
        self.last_update =last_update

    def insert(self, table):
        query = f"""INSERT INTO {table}(title,description,reyting,price,price_status,language) VALUES('{self.title}', '{self.description}', '{self.reyting}','{self.price}','{self.price_status}','{self.language}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table};"""

    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")





class CourseMentor:
    def __init__(self,course_id,menthor_id,last_update):
        self.course_id =course_id
        self.menthor_id =menthor_id
        self.last_update =last_update

    def insert(self, table):
        query = f"""INSERT INTO {table}(course_id,menthor_id) VALUES('{self.course_id}', '{self.menthor_id}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table};"""

    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")


class CourseComments:
    def __init__(self, course_id,stusent_id,menthor_id,text,last_update):
        self.course_id = course_id
        self.stusent_id =stusent_id
        self.menthor_id = menthor_id
        self.text =text
        self.last_update =last_update

    def insert(self, table):
        query = f"""INSERT INTO {table}(course_id,student_id,menthor_id,text) VALUES('{self.course_id}','{self.student_id}','{self.menthor_id}','{self.tetx}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")



class Basket:
    def __init__(self,course_id,student_id):
        self.course_id = course_id
        self.student_id =student_id

    def insert(self, table="basket"):
        query = f"""INSERT INTO {table}(course_id,student_id) VALUES('{self.course_id}','{self.student_id}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")


class Speciality:
    def __init__(self,title,description,course_count,last_update,create_date):
        self.title = title
        self.description = description
        self.course_count = course_count
        self.last_update= last_update
        self.create_date =create_date

    def insert(self, table):
        query = f"""INSERT INTO {table}(title,description,cuorse_count,crate_date) VALUES('{self.title}','{self.description}','{self.course_count}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")


    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")




class SpecialityCourse:
    def __init__(self,speciality_id,course_id,last_update):
        self.specciality_id =speciality_id
        self.course_id = course_id
        self.last_update = last_update

    def insert(self, table="specialitycourse"):
        query = f"""INSERT INTO {table}(speciality_id,course_id) VALUES('{self.speciality_id}','{self.cuorse_id}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")



    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")


class CourseStudent:
    def __init__(self, course_student_id,course_id,student_id,last_update):
        self.course_student_id = course_student_id
        self.course_id = course_id
        self.student_id = student_id
        self.last_update =last_update

    def insert(self, table="coursestudent"):
        query = f"""INSERT INTO {table}(cuorse_id,student_id) VALUES('{self.course_id}','{self.student_id}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")


    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class Modul:
    def __init__(self,lesson_count,course_id,last_update,create_date):
        self.lesson_count = lesson_count
        self.course_id = course_id
        self.last_update = last_update
        self.create_date = create_date


    def insert(self, table="modul"):
        query = f"""INSERT INTO {table}(lesson_count,course_id,create_date) VALUES('{self.lesson_count}','{self.lesson_count}','{self.create_date}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")


    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")


class Lesson:
    def __init__(self,name,modul_id,last_update):
        self.name = name
        self.modul_id = modul_id
        self.last_update = last_update

    def insert(self, table):
        query = f"""INSERT INTO {table}(name,modul_id) VALUES('{self.name}','{self.modul_id}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")


    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")



class LessonComments:
    def __init__(self,lesson_id,student_id,text,create_date,):
        self.lesson_id = lesson_id
        self.student_id = student_id
        self.text = text
        self.create_date = create_date

    def insert(self, table="lessoncomments"):
        query = f"""INSERT INTO {table}(lesson_id,student_id,text,create_date) VALUES('{self.lesson_id}','{self.student_id}','{self.text}','{self.create_date}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")


    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")

class PaymentStatus:
    def __init__(self,name,last_update):
        self.name = name
        self.last_update =last_update

    def insert(self, table):
        query = f"""INSERT INTO {table}(name) VALUES('{self.name}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table};"""

    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")



class PaymentType(PaymentStatus):
    def __init__(self, name, last_update):
        super().__init__(name, last_update)


    def insert(self, table):
        query = f"""INSERT INTO {table}(name) VALUES('{self.name}')"""
        return Database.connect(query, "insert")






class Payment:
    def __init__(self,student_id,course_id,amount,payment_status_id,payment_type_id,last_update,create_date):
        self.student_id = student_id
        self.course_id =course_id
        self.amount = amount
        self.payment_status_id = payment_status_id
        self.payment_type_id = payment_type_id
        self.last_update = last_update
        self.create_date =create_date


    def insert(self, table):
        query = f"""INSERT INTO {table}(student_id,course_id,amount,payment_status_id,payment_type_id) VALUES('{self.student_id}','{self.course_id}','{self.amount}','{self.payment_status_id}','{self.payment_type_id}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")


    @staticmethod
    def update(query):
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = '{search_data}'"""

        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, search_data, table):
        query = f"""DELETE FROM {table} WHERE {column} = {search_data}"""

        return Database.connect(query, "delete")


