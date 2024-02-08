

#############################################################################################
'''
try:
    print(
except SyntaxError:
    print("Except")
'''

###############################################################################################


'''
try:
    print eval('six times seven')
except SyntaxError, err:
       print 'Syntax error %s (%s-%s): %s' % \
       (err.filename, err.lineno, err.offset, err.text)
      
'''

#######################################################
'''
try:
    print("Nelson"*"Nelson")
except ZeroDivisionError:
    print("Zero Division Error")
except ArithmeticError:
     print("Arithmetic Error")
#except:
    # pass
'''
##############################################
'''
class std:
     def __init__(self, name, rollno):
         self.name=name
         self.rollno=rollno

s1=std("xyz", 1)
s2=std("abc", 2)
s3=std("pqr", 3)
l=[s1, s2, s3]

try:
     stu=l[1]
except IndexError:
        print("Index Error")
print(stu.name)
print(stu.rollno)
'''

################################################

'''
# Propagating or Dedicating Exception or Deligating Exceptions

def m1():
    print("m1--starts")
    print(10/0)
    print("m1--end")

def m2():
    try:
        m1()
    except ZeroDivisionError:
         print("Except Block")
    print("m2--end")

m2()
'''

#####################################################################


'''
# Zero Division Error using raise

def m1():
    print("m1--starts")
    raise Exception(10/0)
    print("m1--end")

def m2():
    try:
        m1()
    except ZeroDivisionError:
         print("Except Block")
    print("m2--end")

m2()
'''

################################################################

#raise KeyError ("Key not found")

####################################################################

'''
# raise Exception  

def m1(age):
    if age <0:
        raise Exception("Age Problem")    # Child = Index Error

def m2():
    try:
       m1(-5)
    except Exception as msg:               # Parent = Exception
         print("Except--Block", msg)
    print("M2--block")

m2()
'''

########################################################################################3

'''
# raise Exception  (Error Milega)

def m1(age):
    if age <=0:
        raise Exception ("Age Problem")    # Parent = Exception

def m2():
    try:
       m1(-5)
    except IndexError as msg:         # Child = Index Error
         print("Except--Block", msg)
    print("M2--block")

m2()
'''

#######################################################################
'''
# raise Exception (m1 and m2 methods are outside the class)


class AgeInvalidError(Exception):
    def __init__(self, msg):
        self.msg=msg

def m1(age):
       print("m1--start")
       if age<0:
          raise  AgeInvalidError("Age Problem")      # Custom = AgeInvalidError
       print("m1--end")

def m2():
       try:
           m1(-5)
       except AgeInvalidError as msg:         # Custom = AgeInvalidError
          print("except--block", msg)
       print("m2--end")

m2()
'''
#############################################################3

'''
# raise Exception (All m1 and m2 Methods in class)

class AgeInvalidError(Exception):
    def __init__(self, msg):
        self.msg=msg

    def m1(self, age):
       print("m1--start")
       if age < 0:
          raise AgeInvalidError("Age Problem")        # Custom =AgeInvalidError
       print("m1--end")

    def m2(self):
       try:
           self.m1(-5)
           # m1(-5)
       except AgeInvalidError as msg:            # Custom = AgeInvalidError
          print("except--block", msg)
       print("m2--end")

A=AgeInvalidError(1)
A.m2()
'''

####################################################################################

'''
# meaning less Finally

try:
    print(10/0)
finally:
     print("s")

'''
##############################################################################################
'''     
try:
     print(10/0)
except (ZeroDivisionError,ArithmeticError) as e:
        print("Except block")
'''
#########################################################################################

'''

# raise Exception (All m1 and m2 Methods in class)

class AgeInvalidError(Exception):
    def __init__(self, msg):
        self.msg=msg

    def m1(self, age):
       print("m1--start")
       if age<0:
          raise AgeInvalidError("Age Problem")        # Custom =AgeInvalidError
       print("m1--end")

    def m2(self):
       try:
           self.m1(-5)
       except AgeInvalidError as e:            # Custom = AgeInvalidError  # small e use kiya
          print("except--block",e)
       print("m2--end")

A=AgeInvalidError(1)
A.m2()

'''
###################################################################################
'''
try:
    print("Try")
    print(10/0)
finally:
    print("jBSkdjh")
'''
################################################################################################
