
#################################################################################################33
'''
# raise Exception  (All m1, m2 and m3 Methods are outside class)  (Tricky)

class AgeInvalidError(Exception):
    def __init__(self, msg):
        self.msg=msg

def m1(age):
       print("m1--start")
       if age<0:
          raise AgeInvalidError(855)
       print("m1--end")

def m2():
       try:
           m1(-5)
       except AgeInvalidError as msg:
          print("except--block", msg)
       print("m2--end")


def m3():
    try:
        m2()
    except AgeInvalidError as msg:
        print("except--block", msg)
    print("m3--end")

m2()
m3()
'''


##############################################################################################################
'''

# Try, Except and raise Exception Handling with init and str method (Very Important)

class AgeInvalidException(Exception):
      def __init__(self, age, message):
          self.age=age
          self.message=message

      def __str__(self):
         return f"The age{self.age} is not valid, Since - {self.message}"

try:
  a=int(input("Enter a Age : "))
  if a<18:
      raise AgeInvalidException(a, "age must be greater than 18 for this job")
  elif a>35:
      raise AgeInvalidException(a, "age must be lesser than 35 for this job")
  else:
      print("Congo! You can apply")

except AgeInvalidException as obj:
       print(obj)

'''
###########################################################################################
