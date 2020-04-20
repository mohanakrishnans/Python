try:
	32/0
except:
	print('Divide by zero\n')

# Specific Exception Handling
try:
	car = ['ford','ferrari','bmw']
	print(car[3])
except IndexError:
	print("There is no such index!\n")


# else in exception
my_variable = 'My variable'
try:
  print(my_variable)
except NameError:
  print('NameError caught!\n')
else:
  print('No NameError\n')


# raising an Exception
# try:
#   raise IndexError('This index is not allowed\n')
# except:
#   print('Doing something with the exception!\n')
#   raise

# finally
try:
	print(my_var)
except NameError:
	print('Except block')
finally:
	print('Finally block')