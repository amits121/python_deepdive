filename = 'pythonclass.txt'
with open(filename, 'w') as file_content:
    file_content.write("This python class have four students. ")
    file_content.write("Their names are; Seema, Priyanka, Ajay and Gaurav.")
with open(filename, 'a') as file_content:	
    file_content.write("They arelearning fast") 