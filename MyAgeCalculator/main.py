from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def main():
    name = input("Enter your name : ")
    birthdate = input("Enter your birthday (YYYY-MM-DD) : ")
    age = calculate_age(birthdate)
    print(f"Hello! My name is {name} and my age is {age} years old")

if __name__ == "__main__":
    main()
