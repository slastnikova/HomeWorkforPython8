from studentbasa import save_basa, load_basa
from teacher import add_student, put_rating
from student import see_rating

def controller():
    load_basa() 
    match = input(' кто ты? 1 - учитель, 2 - ученик:  ')
    case='1'
    flag=1
    while flag ==1:
            print(' ваши действия?: ')
            act = input(' 1 - записать ученика, 2 - поставить оценку, 3 - выйти из журнала: ')
            if act == '1':
                add_student()
            elif act == '2':
                put_rating()
            elif act == '3':
                flag=0
            else:
                save_basa()
    case = '2'
    flag=1
    while flag==1:
            last_name = input(' ввести им ученика, 3 - чтобы выйти из журнала:')   
            if last_name=='3':
                flag=0
            else:

                see_rating(last_name)     
