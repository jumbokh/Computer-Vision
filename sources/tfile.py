import os

os.getcwd()

path = "E1/Eason/"
file_type = "jpg"

for i, filename in enumerate(os.listdir(path)):

    i = str(i)

    if len(i)==1:
        i = "000"+i
    elif len(i)==2:
        i = "00"+i
    elif len(i)==3:
        i = "0"+i
    else:
        i = str(i)

    os.rename(path + filename, path + str(i) + "." + file_type)
