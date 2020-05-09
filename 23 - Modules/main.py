# link to download python ----> https://www.python.org/downloads/

# 1)Loading whole module
# syntax ---> import module_name

import Addition

sum1 = Addition.add_two_numbers(20,30)
print('Sum1 ==== ',sum1)

sum2 = Addition.add_three_numbers(20,30,40)
print('Sum2 ==== ',sum2)

print('List1 ==== ',Addition.num_list)

# print('dict1 ===== ',Addition.dict11) #<----- error




# 2)Loading module and giving different name/ alias
# syntax ---> import module_name as alias_name

import Addition as ad

sum1 = ad.add_two_numbers(20,30)
print('Sum1 ==== ',sum1)

sum2 = ad.add_three_numbers(20,30,40)
print('Sum2 ==== ',sum2)

print('List1 ==== ',ad.num_list)



# 3) Importing only selected functions or variables
# from module_name import function_name
# from module_name import variable_name

# a) loading a perticular function
from Addition import add_two_numbers

sum1 = add_two_numbers(20,30)
print('New sum1 ====== ',sum1)

# sum1 = Addition.add_two_numbers(20,30) <------- error
# print('New sum1 ====== ',sum1)

# b) loading a perticular variable
from Addition import dict1

print('dict1 === ',dict1)
print('Brand === ',dict1['Brand'])

