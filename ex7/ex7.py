textlist = ["hello world","hello planet",""]

for i in textlist:
    if len (i) %2 == 0:
        print(f"{i}   -->   even")
    else:
        print(f"{i}   -->   odd")