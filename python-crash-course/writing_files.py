employee_file = open("employees_1.txt", "w") # Can create a new file or overwrite an existing file

# employee_file.write("Toby - Human Resources")  


employee_file_2 = open("employees_1.txt", "a") # 'a' is for append, which adds to the end of the file

employee_file_2.write("\nKelly - Customer Servicesss")


html_write = open("index.html", "w")

html_write.write("<p>This is a paragraph</p>")

