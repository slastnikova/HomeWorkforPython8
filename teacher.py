from studentbasa import set_student, set_rating

def add_student():
    metric = input(' введите фамилию, имя, класс через пробел: ').split('')
    set_student(metric)

def put_rating():
    last_name = input(' введите фамилию ученика: ')    
    lesson = input(' введите предмет: ')
    rating = input(' введите оценку, больше одной, вводить через пробел: ').split()
    set_rating(last_name, lesson, rating )
