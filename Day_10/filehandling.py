def Write_details():
    filename = input("Enter file name with extension:")
    try:
        fileObject = open(filename, "a")
        msg = input("Enter your message: ")
        print(msg, file = fileObject)
        print("Data inserted to the file")

    except Exception as er:
        print(f'Warning: {er}')


def Read_details():
    filename = input("Enter file name with extension: ")
    try:
        fileobject = open(filename, "r")
        for line in fileObject.readlines():
            print(line)

    except Exception as er:
        print(f'Warning {er}')



if __name__ == "__main__":
    Read_details()

