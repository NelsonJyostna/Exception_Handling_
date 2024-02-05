
'''
print("file__A__start")
print(10/0)
print("File__A__End")
'''
#######################################################################
'''
print("File__A__Start")
try:
    print(10/0)
except:
    print("Except_Block")

print("File__A__End")
'''
###############################################################################
'''
print("File__A__Start")
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("Except_Block", e)

print("File__A__End")
'''
#################################################################################################
 # When try block have Wrong code
'''
print("File_A_Start")
try:
    print("Try__Start")
    print(10/0)
    print("Try__END")
except ZeroDivisionError:
    print("Except_Block")

print("File__A__End")
'''
###########################################################################################

 # When try block have Right code

'''
print("File_A_Start")
try:
    print("Try__Start")
    print(10/2)
    print("Try__END")
except ZeroDivisionError:
    print("Except_Block")
else:
    print('Else block')
print("File__A__End")
'''

#################################################################################################

#Try, Except else block
'''

print("File__A__Start")
try:
    print("Try_Start")
    print(10/2)
    print("Try_ENd")
except:
    #pass
    print("Except Block")
else:
    print("else Block")

print("File__A__End")

'''
############################################################################3

'''
try:
   r=int(input("ENter ur Roll no : "))
   print(r)
except BaseException:
    print("Please provide some int variable ")
'''
############################################################################################
'''
try:
   r=int(input("ENter ur Roll no : "))
   print(r)
except ValueError:
    print("Please provide some int variable ")
'''
#####################################################################################
'''
# Multply Except is possible
try:
    print(" "/' ')

except ZeroDivisionError:
      print("Zer0_Except_Block")

except ValueError:
    print("Value_Except_Block")

except:
   print("Third except block")
'''
######################################################################################################
'''a=str(5846)
print(type(a))'''
###########################################################################################################
# 2 try not possible
'''
try:
     print(" "/' ')
try:
     print( 0/0)
except:
      pass
except:
     pass
'''
#######################################################################################################################

'''
try :
    a = int(input("Enter a First No : "))
    b = int(input("Enter a Second no : "))
    print(a/b)
except ZeroDivisionError:
    print("Please provide positive no")
except ValueError:
     print("Please enter a value")
'''
#######################################################################################################################
# Try, except, else block

'''
try:
    a = int(input("Enter a First No : "))
    b = int(input("Enter a Second no : "))
    print(a / b)
except ZeroDivisionError:
    print("Please provide positive no")
except ValueError:
     print("Please enter a value")
else:
    print("Else__Block")
'''

###############################################################################################################################
# Two else can not possible

'''
try:
    print(10/2)
except:
    print("Except Block")
else:
   print("Else Block")
else:
    print("second Else block")

'''
################################################################################################################################
