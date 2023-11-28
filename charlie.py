def get_user_age():
    return int(input("Enter your age: "))

def add_1_to(x):
    return x + 1

def age_up():
    age = get_user_age() # Running code in Script Mode only
    add_1_to(age)
    return "Next year you will be: "+ str(add_1_to(age))

def test_add_1_to_function():
    assert add_1_to(1) == 2

if __name__ == "__main__":
    print(age_up())