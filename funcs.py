def say_hello_twice():
    print("hello")
    print("hello")
say_hello_twice()

def say_hello_you(name = 'unknown'):
    print("hello", name)
say_hello_you('dulee')
say_hello_you('nico')
say_hello_you()

def first_meeting(name, age):
    return f"Hello {name}, you are {age} years old"

print(first_meeting(age = 30, name = 'dulee'))