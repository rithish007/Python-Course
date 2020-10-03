# Writing

def Write_Details():
    filename = input("Enter file name with extension to write: ")
    try:
        #filename = open('Login.txt','w')
        fileObject = open(filename, "w")
        msg1 = input("Enter your Username: ")
        msg2 = input("Enter your Password: ")
        print(msg1, file=fileObject)
        print(msg2,file=fileObject)
        print("Data inserted to the file")

    except Exception as er:
        print(f'Warning: {er}')

# Reading

def Read_Details():
    filename = input("Enter file name with extension to read: ")
    try:
        #filename = open('Login.txt','r')
        fileObject = open(filename, "r")
        for line in fileObject.readlines():
            print(line)
    except Exception as er:
        print(f'Warning: {er}')




if __name__ == "__main__":
    Write_Details()
    Read_Details()