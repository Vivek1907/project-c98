file1 = input("Enter 1st filename:-")
file2 = input("Enter 2nd filename:-")

def swapFileData(a, b):
    f1 = open(a, "r")
    f2 = open(b, "r")
    text1 = f1.read()
    text2 = f2.read()
    print(text1)
    print(text2)
    f1.close()
    f2.close()
    f1write = open(a, "w")
    f2write = open(b, "w")
    f1write.write(text2)
    f2write.write(text1)
    f1write.close()
    f2write.close()


swapFileData(file1, file2)

