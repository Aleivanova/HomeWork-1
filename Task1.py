import datetime

age = int(input("Привет! Сколько тебе лет? "))
in_year = int(input("Введи год: "))
cur_year = datetime.date.today().year
born_year = cur_year - age
if born_year > in_year: print("Ты еще не родился ;)")
else: print("В ", in_year, " тебе будет ", in_year - born_year, " лет")

