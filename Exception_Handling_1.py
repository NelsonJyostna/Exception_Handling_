
########################################################################
# Child EXCEPT class first then its parent EXCEPT class

'''
try :
     print(10/0)
except ZeroDivisionError:         # Child Except Class
      print("Zero Error block")
except ArithmeticError:           # Parent Except Class
     print("Arithmetic Error")
'''


###################################################################################################################



# Dont try to take first Parent EXCEPT class

'''
try :
     print(10/0)
except ArithmeticError:                # Parent Class
     print("Arithmetic Error")
except ZeroDivisionError:              # Child Class
      print("Zero Error block")
'''

#######################################################################################################3


# try finally block

'''
try:
    print("try_first_Block")
    print(10/0)
    print("try_end_block")
finally:
   print("finally_block")

print("A_File_ENd")
'''
###############################################################################
'''
try:
   print(10/0)
else:
    print("sdbmdbkdj")
'''
#################################################################################################



# try except finally block
'''
try:
    print("try_Block")
    print(10/0)
    print("try_block")

except ZeroDivisionError:
      print("Except_Block")

finally:
   print("finally_block")

print("A_File_ENd")
'''
##############################################################

# If try block having return statement
'''
def m1():
    x=10
    try:
        print("try_Block")
        print(10 / 0)
        return x

    finally:
        print("Finally__Block")
    # except:
    #     print("Shivaji")
y=m1()
print(y)

'''
#############################################################


# If try block having return statement with finally value
'''
def m1():
    x=10
    try:
        print("try_Block")
        return x
    finally:
        x=40
        print("Finally__Block", x)
y=m1()
print(y)

'''
###############################################################


# IF Both try & finally block having return statement
'''
def m1():
    x=10
    try:
        print("try_Block")
        return x
    finally:
        x=40
        print("Finally__Block", x)
        return x
y=m1()
print(y)

'''
#######################################################33

#print(10/"")
# print(""/10)
# print((20/int(" ")))
#a=int(input(" ENter a no: "))
#b=input("ENter a String : ")

#print(' ' and 2)
##################################################################################################3

'''
print("Program Starts")
l=[10,20,30,40,50]

try:
     print("try Starts")
     print(l[6])
     print("try ends")

except LookupError:
   print("Some look exception occured")

except IndexError:
   print("Yor r trying to access the index out of bound")

print("Program Ends")

'''
########################################################################################

'''

print("Program Starts")
l=[10,20.30,40,50]
d={1:1, 2:4, 3:9, 4:16, 5:25}
try:
     print("try Starts")
     #print(l[10])
     print(d[6])
     print("try ends")

except KeyError:
      print("The key u r trying to access dosen't exist")

except IndexError:
      print("Yor r trying to access the index out of bound")

except LookupError:
      print("Some lookup exception occured")

except Exception:
      print("Some Exception Occured")

print("Program Ends")

'''
#######################################################################################

'''
def a():
    return 20

t=a()
print(t)

'''
#######################################################################################
'''
def m1():
    x=3
    try:
        print("try Block")
        print(10/0)
    except ZeroDivisionError:
            print("Zero Division Error")
    finally:
          print("Finally")
t=m1()
print(t)
'''
############################################################################################3
###########################################################################

# Mutliple Errors in single Except block
'''
try:
    print(10/0)
except (ArithmeticError, ZeroDivisionError) as e:
    print("Except block", e)
# except Exception as e
   # print("Second Exception ", e)
'''
######################################################################