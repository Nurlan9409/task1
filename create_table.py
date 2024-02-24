from database import Database

def create_tables():
    country_table = f"""
        CREATE TABLE country(
            country_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            last_update TIMESTAMP DEFAULT now(),
            date DATE);"""

    city_table = f"""
        CREATE TABLE city(
                city_id SERIAL PRIMARY KEY,
                country_id int references country(country_id),
                name VARCHAR(20),
                last_update TIMESTAMP DEFAULT now(),
                date DATE);
                """

    adress_table = f"""
        CREATE TABLE adress(
            adress_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            city_id int references city(city_id),
            last_update TIMESTAMP DEFAULT now());
            """


    user_table = f"""
        CREATE TABLE user(
            user_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            username VARCHAR(20),
            password VARCHAR(20),
            gmail VARCHAR(20),
            create_date date,
            last_update TIMESTAMP DEFAULT now());
              """


    student_table = f"""
        CREATE TABLE student(
            student_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            username VARCHAR(20),
            password VARCHAR(20),
            gmail VARCHAR(20),
            create_date date,
            last_update TIMESTAMP DEFAULT NOW(),
            balance float,
            course_id varchar(20));
            """

    menthor_table = f"""\
        CREATE TABLE menthor(
            menthor_id serial primary key,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            user_name VARCHAR(20),
            password VARCHAR(20),
            gmail VARCHAR(20),
            status boolean,
            create_date date,
            last_update TIMESTAMP DEFAULT NOW());
              """

    course_table = f"""
        CREATE TABLE course(
            course_id serial primary key,
            title VARCHAR(50),
            description text,
            reyting float,
            price float,
            price_status boolean,
            language varchar(20),
            create_date date,
            last_update TIMESTAMP DEFAULT NOW());
            """
    course_menthor = f"""
        CREATE TABLE course_menthor(
            course_menthor_id serial primary key,
            course_id int references course(course_id),
            menthor_id int references menthor(menthor_id),
            last_update TIMESTAMP DEFAULT NOW());
            """

    course_comments_table= f"""
        CREATE TABLE course_comments(
            course_comments_id serial primary key,
            course_id int references course(course_id),
            student_id int references student(student_id),
            menthor_id int references menthor(menthor_id),
            text text,
            last_update TIMESTAMP DEFAULT NOW());
            """
    basket_table = f"""
        CREATE TABLE basket(
            basket_id serial primary key,
            course_id int references course(course_id),
            student_id int references student(student_id));
            """
    speciality_table = f"""
        CREATE TABLE speciality(
            speciality_id serial primary key,
            title varchar(20),
            deckription text,
            course_count smallint,
            last_update TIMESTAMP DEFAULT NOW(),
            create_date date);
            """
    speciality_course_table = f"""
        CREATE TABLE speciality_course(
            speciality_course_id serial primary key,
            speciality_id int references speciality(speciality_id),
            course_id int references course(course_id),
            last_update TIMESTAMP DEFAULT  NOW());
                """
    course_student_table = f"""
        CREATE TABLE course_student(
            course_student_id serial primary key,
            course_id int references course(course_id),
            student_id int references student(student_id),
            last_update TIMESTAMP DEFAULT  NOW());
            """
    modul_table = f"""
        CREATE TABLE modul(
            modul_id serial primary key,
            lesson_count smallint,
            course_id int references course(course_id),
            last_update timestamp default now(),
            create_date date);
            """
    lesson_table = f"""
        CREATE TABLE lesson(
            lesson_id serial primary key,
            name varchar(20),
            modul_id int references modul(modul_id),
            last_update timestamp default now());
            """
    lesson_comments_table = f"""
        CREATE TABLE lesson_comments(
            lesson_comments_id serial primary key,
            lesson_id int references lesson(lesson_id),
            student_id int references student(student_id),
            text text,
            create_date date);
            """

    payment_status_table = f"""
        CREATE TABLE payment_status(
            payment_status_id serial primary key,
            name varchar(20),
            last_update timestamp default now());
            """

    payment_type_table = f"""
        CREATE TABLE payment_type(
            payment_type_id serial primary key,
            name varchar(20),
            last_update timestamp default now());
            """
    payment_table = f"""
        CREATE TABLE payment(
            payment_id serial primary key,
            student_id int references student(student_id),
            course_id int references course(course_id),
            amount float,
            payment_status_id int references payment_status(payment_status_id),
            payment_type int references payment_type(payment_type_id),
            last_update timestamp default now(),
            create_date date);
             """

    data_table = {
        'country': country_table,
        'city': city_table,
        'adress':adress_table,
        'user':user_table,
        'student':student_table,
        'menthor':menthor_table,
        'course':course_table,
        'course_menthor':course_menthor,
        'course_comments':course_comments_table,
        'basket':basket_table,
        'speciality':speciality_table,
        'speciality_course':speciality_course_table,
        'course_student': course_student_table,
        'modul': modul_table,
        'lesson':lesson_table,
        'lesson_comments':lesson_comments_table,
        'payment_status':payment_status_table,
        'payment_type':payment_type_table,
        'payment':payment_table

    }

    for i in data_table:
        print(f"{i} {Database.connect(data_table[i],"create")}")


if __name__ == "__main__":
    create_tables()
