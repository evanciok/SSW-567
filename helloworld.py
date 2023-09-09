from datetime import datetime

def my_brand(assignment):
  datetime_obj = datetime.now()
  datetime_string = datetime_obj.strftime("%d/%m/%Y %H:%M:%S")
  print("=*=*=*= Evan Ciok =*=*=*=")
  print("=*=*=*= 2023F SSW 567-A =*=*=*=")
  print("=*=*=*= " + assignment + " =*=*=*=")
  print("=*=*=*= " + datetime_string + " =*=*=*=")

assignment_name = "HW 00 - Tools Setup"

print("Hello world")
my_brand(assignment_name)