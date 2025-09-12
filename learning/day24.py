#open the file
'''file=open("day24.txt")
contents=file.read()
print(contents)
file.close()    #remove resource allocation of file opened'''
with open("day24.txt") as file:
    contents=file.read()
    print(contents)
    #file.write("I am a coder. I practise")  #wouldn't function in r mode
    #default mode is r mode if nothing is mentioned it is considered as read mode
    
