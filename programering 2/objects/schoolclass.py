class student:
    def __init__(self, f_name : str, l_name : str, age : int, gender : str):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender

class teacher:
    def __init__(self, f_name : str, l_name : str, age : int, gender : str):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender

class group:
    def __init__(self, subject : str, teacher : teacher, students : list):
        self.subject = subject
        self.teacher = teacher
        self.students = students
        
