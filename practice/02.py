import sys

def remove_string():
    file_name=input("File name : ")
    remove_name=input("Remove string : ")
    f=open(file_name)
    S=f.read()
    newS=S.replace(remove_name,"")
    f.close()
    f=open(file_name,'w')
    f.write(newS)
    f.close()

