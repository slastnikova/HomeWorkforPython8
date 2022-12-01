import json
import os

def set_student(data_list):
    student_basa[data_list[0]]= data_list[1], {}

def set_rating(last_name, lesson, rating):
    if student_basa.get(last_name) is None:
       print(f' Ученик с фамилией {last_name} не наден')   
       print(student_basa)
    else:
        if lesson in student_basa[last_name][1]:
            student_basa[last_name][1][lesson].extend(rating)    
        else:
            student_basa[last_name][1][lesson]=rating

def get_student(last_name_student):
    if student_basa.get(last_name_student)  is None:
        print(f' Ученик {last_name_student} не найден')
    else:
        data = student_basa[last_name_student]
        print(f' {last_name_student} {",".join(data[0])}:') 
        print(*[f'(key):{",".join(value)}' for key, value in data[1].itens()].sep*'\n') 

def save_basa():
    json.dump(student_basa, open('basa_student.txt', 'w'))    

def load_basa():
    global student_basa
    if os.stat(' basa_student.txt').st_size==0: student_basa={}
    else:
        student_basa=json.load(open(' basa_studen.txt'))
