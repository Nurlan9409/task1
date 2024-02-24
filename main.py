from classes import Country,City,Adress,User,Student,Mentor,Course,CourseMentor,CourseComments,Basket,Speciality,SpecialityCourse,CourseStudent,Modul,Lesson,LessonComments,PaymentStatus,PaymentType,Payment

def ServiceCountry():
    ty = input("""select for
    1.select information
    2.insert information
    3.delete information
    4.update information
    0.Back
    >>>>>>>>>>>>>>>
    """)
    if ty == "1":
        for i in Country.select(table="country"):
            print(i)
        return ServiceCountry()

    elif ty == '2':
        name = input("Enter name of country: ")
        create_date = input("Enter date of creation: ")
        country = Country(name, create_date)
        print(country.insert())
        return ServiceCountry()

    elif ty == '3':
        column = input("Enter column name")
        data = input("Enter data")
        if column != "country_id":
            print(Country.delete(column, data,))

        else:
            print(Country.delete_id(column, data))

        return ServiceCountry()

    elif ty == '4':
        country = input("Enter name of country:New ")
        name = int(input("Enter old name country"))
        query = f"""UPDATE country SET name='{country}' WHERE country_id='{id}';"""
        print(country.update(query))
        return ServiceCountry()

    elif ty == '0':
        return main()

def ServiceCity():
    ty = input("""select for
    1.select information
    2.insert information
    3.delete information
    4.update information
    0.back
    >>>>>>>>>""")

    if ty == "1":
        for i in City.select():
            print(i)
            return ServiceCity()

    elif ty == '2':
        name = input("Enter name of city: ")
        create_date = input("Enter date of creation: ")
        city = City(name, create_date)
        print(city.insert())
        return ServiceCity()

    elif ty == '3':
        column = input("Enter column name")
        data = input("Enter data")
        if column != "city_id":
            print(City.delete(column, data))

        else:
            print(City.delete_id(column, data, ))

        return ServiceCity()

    elif ty == '4':
        city = input("Enter name of city:New ")
        id = int(input("Enter old name city"))
        query = f"""UPDATE country SET name='{city}' WHERE city_id='{id}';"""
        print(city.update(query))
        return ServiceCity()

    elif ty == '0':
        return main()

def ServiceAdress():
    ty = input("""select for
    1.select information
    2.insert information
    3.delete information
    4.update information
    0.back
    >>>>>>>>>""")

    if ty == "1":
        for i in Adress.select():
            print(i)
            return ServiceAdress()

    elif ty == '2':
        name = input("Enter name of adress: ")
        create_date = input("Enter date of creation: ")
        adress = Adress(name, create_date)
        print(adress.insert())
        return ServiceAdress()

    elif ty == '3':
        column = input("Enter column name")
        data = input("Enter data")
        if column != "adress_id":
            print(Adress.delete(column, data))

        else:
            print(Adress.delete_id(column, data))

        return ServiceAdress()

    elif ty == '4':
        adress = input("Enter name of adress:New ")
        id = int(input("Enter old name adress"))
        query = f"""UPDATE adress SET name='{adress}' WHERE adress_id='{id}';"""
        print(adress.update(query))
        return ServiceCity()

    elif ty == '0':
        return main()

def ServiceUser():
    ty = input("""select for
     1.select information
     2.insert information
     3.delete information
     4.update information
     0.back
     >>>>>>>>>""")

    if ty == "1":
        for i in User.select():
            print(i)
            return ServiceUser()

    elif ty == '2':
        name = input("Enter name of user: ")
        create_date = input("Enter date of creation: ")
        user = User(name, create_date)
        print(user.insert())
        return ServiceUser()

    elif ty == '3':
        column = input("Enter column name")
        data = input("Enter data")
        if column != "user_id":
            print(User.delete(column, data, ))

        else:
            print(User.delete_id(column, data, ))

        return ServiceUser()

    elif ty == '4':
        user = input("Enter name of user:New ")
        name = int(input("Enter old name user"))
        query = f"""UPDATE user SET name='{user}' WHERE user_id='{id}';"""
        print(user.update(query))
        return ServiceUser()

    elif ty == '0':
        return main()


def Service_Student():
    ty = input("""select for
     1.select information
     2.insert information
     3.delete information
     4.update information
     0.back
     >>>>>>>>>""")

    if ty == "1":
        for i in Student.select():
            print(i)
            return Service_Student()

    elif ty == '2':
        name = input("Enter name of student: ")
        create_date = input("Enter date of creation: ")
        student = Student(name, create_date)
        print(student.insert())
        return Service_Student()

    elif ty == '3':
        column = input("Enter column name")
        data = input("Enter data")
        if column != "user_id":
            print(Student.delete(column, data, ))

        else:
            print(Student.delete_id(column, data, ))

        return Service_Student()

    elif ty == '4':
        student = input("Enter name of student:New ")
        name = int(input("Enter old name student"))
        query = f"""UPDATE user SET name='{student}' WHERE student_id='{id}';"""
        print(student.update(query))
        return Service_Student()

    elif ty == '0':
        return main()



def main():
    select = input("""
    Select service for:
    1.Country
    2.City
    3.Adress
    4.User
    5.Student
    6.Menthor
    7.Course
    8.Course_menthor
    9.Course_comments
    10.Basket
    11speciality
    12.specialiyu_course
    13.Course_student
    14.MODUL
    15.Lesson
    16.Lessom_comments
    17.Payment_status
    18.Payment_type
    19.Payment
    >>>>>>>
    """)
    if select == '1':
        return ServiceCountry()
    elif select == '2':
        return ServiceCity()
    elif select =='3':
        return ServiceAdress()
    elif select =='4':
        return ServiceUser()
    elif select =='5':
        return Service_Student()
    elif select =='6':
        pass
    elif select =='7':
        pass
    elif select =='8':
        pass
    elif select =='9':
        pass
    elif select =='10':
        pass
    elif select =='11':
        pass
    elif select =='12':
        pass
    elif select =='13':
        pass
    elif select =='14':
        pass
    elif select =='15':
        pass
    elif select =='16':
        pass
    elif select =='17':
        pass
    elif select =='18':
        pass
    elif select =='19':
        pass











if __name__ == '__main__':
    main()
