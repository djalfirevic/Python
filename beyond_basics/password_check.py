correct_password = "python123"
name = input("Enter name: ")
password = input("Enter password: ")

while correct_password != password:
  password = input("Wrong password! Enter again: ")

message = "Hi %s, you are logged in" % (name)
print(message)