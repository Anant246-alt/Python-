import os
def write_and_file_name(filename,content):
    
        with open(filename, 'w') as file:
            return file.write(content)
    
print(write_and_file_name("Example.txt","Virat Kohli is the best Batsmen"))
