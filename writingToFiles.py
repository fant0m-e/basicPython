employee_file = open("C:\\Users\\trist\Documents\\python\\employees.txt", "a")
employee_file.write("\nToby - Human Resources") # new line
employee_file.close()

# employee_file = open("C:\\Users\\trist\Documents\\python\\employees.txt", "w")
# employee_file.write()                               would overwrite entire file
# employee_file.close()                               if we changed employees.txt in target
#                                                     then new file would be created