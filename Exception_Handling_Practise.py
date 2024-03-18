

'''
try:
     print(10/0)
except ArithmeticError :
      print("Arithmetic Block")
except ZeroDivisionError:
    print("Zero Divison Error Block")
'''
###############################################################
'''
try:
    print(10/0)
except ZeroDivisionError:
     print("Zero Division Error block")
except ArithmeticError:
     print("Arithmetic Block")
     
'''
###############################################################3

'''
def m1():
  try:
       print("try Starts")
       x=40
       return x
       print(10/0)
  except :
      print("Except block")
  finally:
       x=88
       print("Finally block")
       return x

print("Program ENds")

m1()
print(m1())
'''
#################################################################################################################

######################################################################


'''
def m2():
    try:
       a=5
       #return a
       print(a)
       print(10/0)
    except:
        print("ZeroDivisionError")
    finally:
        print("Finally")


m2()
#print(m2())
'''
#########################################################################3
'''
def m3():
      #pass
      a=5
      return a


print(m3())
'''
#######################################################################################
'''
def m1():
    x=5
    try:
        print("try_Block")
        return x
    finally:
        print("finally")
y=m1()
print(y)'''
################################################################33




######################################################################################################
'''
def m1():
    x=3
    try:
        print("try block")
        print(10/0)
    except ZeroDivisionError:
         print("ZeroDivisionError")
    finally:
        print("Finally")

t=m1()
print(t)
'''

#################################################################################
''' 
# raise (m and m2 r outside the class)

class AgeInvalid(Exception):
    def __init__(self, msg):
        self.msg=msg


def m1(age):
      if age<0:
         raise AgeInvalid("Invalid")
      print("M1---end")

def m2():
     try:
       m1(-5)
     except AgeInvalid as e:
         print("Except Block", e)
     print("M2--end")

m2()
'''
#####################################################################
'''
# raise (m1 and m2 r inside the class)

class AgeInvalid(Exception):
    def __init__(self, msg):
        self.msg=msg


    def m1(self, age):
          if age<0:
            raise AgeInvalid("Invalid")
          print("M1---end")

    def m2(self):
           try:
             self.m1(-5)
           except AgeInvalid as e:
             print("Except Block", e)
           print("M2--end")

o=AgeInvalid(5)
o.m2()'''
#############################################################################################################################

'''
def m1():
        print("m1--block")
        print(10/0)

def m2():
    try:
        m1()
    except  Exception as e:
        print("Exception Occured", e)

m2()
'''
#################################################3##############################################################

'''
def m1():
    print(10/0)
    raise Exception("Error")

def m2():
    try:
      m1()
    except Exception as msg:
        print("Exception occured", msg)
    print("M2--end")

m2()

'''
##############################33########################################################################################
'''
try:
    print(10/0)
except:
    print("Exception")
print("M2 end")'''
#######################################################################################################################
'''
def m1(age):
    if age<0:
        raise Exception("Error")

def m2():
    try:
        m1(-5)
    except Exception as msg:
          print("Exception occured", msg)
    print("M2--End")


m2()
'''
######################################################################################################################################################
'''
class AgeInvalidError(Exception):
       def __init__(self, msg):
           self.msg=msg

def m1(age):
    if age<0:
        raise AgeInvalidError ("Age Problem")

def m2():
    try:
        m1(-5)
    except AgeInvalidError as e:
        print("Exception occured", e)
    print("M2--end")

m2()
'''
##################################################################################################################################
'''
class AgeInvalidError(Exception):
      def __init__(self, msg):
          self.msg=msg

      def m1(self, age):
          if age<=0:
              raise AgeInvalidError("Error")

      def m2(self):
          try:
              #self.m1(-5)
              self.m1(-5)
          except AgeInvalidError as msg:
              print("Exception Occured", msg)
          print("m2--end")

a=AgeInvalidError("123456")
a.m2()

'''

##########################################################################################3
'''
def m1(age):
    if age<0:
        raise Exception("Age Invalid")

def m2():
    try:
        m1(-15)
    except Exception as msg:
       print("Occur Exception", msg)
    # print("Nelson")
    else:
      print("Else Block")

m2()
'''
##################################################################################33
# Propgating Exception
'''
def m1():
    print("M1---Starts")
    print(10/0)
    print("M1---Ends")

def m2():
    try:
        m1()
    except:
        print("Zero Division Error")

m2()
'''
################################################################################
'''
def m1(age):
    if age>18:
        print("Valid ")
    else:
        raise Exception ("Invalid")

def m2():
    try:
       m1(17)
    except Exception as msg:
        print("except block", msg )

m2()
'''
########################################################################################################3


















