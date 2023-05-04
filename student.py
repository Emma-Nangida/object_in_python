# class student:
#     firstName="Wina"
#     lastName="Nangida"
#     country="Kenya"
#     name="Emma"
#     age=23
#     school="akiraChix"
#     Nationality="Kenyan"

#     print(student.name)
# from msilib.schema import SelfReg
# from typing import Self


class Student:
    school="Akirachix" #class attribute
    def __init__(self,name,age,school,Nationality,first_name,last_name,country):
        self.first_name=first_name
        self.last_name =last_name
        self.country=country
        self.name=name
        self.age=age
        self.school=school
        self.Nationality=Nationality
    
    def greet_student(self):
        return f"Hello{Self. name},welcome to{Self.school},proudly {Self.Nationality}"

  # 1) Update the Student Class to include these attributes - first_name, last_name, age, country
     #- Add these methods to the Student class
           #  - show_full_name
            # - year_of_birth
            # - show_initials  
    def show_student_info(self):
        return f"Hello{self.first_name}{self.last_name}"
    def year_of_birth(self):
        return f"{1999-self.age}"
    def show_initials(self):
        return f"{self.first_name[0],{self.last_name[0]}}"






