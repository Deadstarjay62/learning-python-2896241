#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    with open("textfile.txt","w+") as f:
        # Open the file for appending text to the end
        # f = open("textfile.txt","a+")

        # write some lines of data to the file
        for i in range(10):
            f.write("This is line %d\r\n" % (i+1))

    # Open the file back up and read the contents
    f = open("textfile.txt","r")
    if f.mode == 'r': # check to make sure that the file was opened
        # use the read() function to read the entire file
        # contents = f.read()
        # print (contents)

        fl = f.readlines() # readlines reads the individual lines into a list
        for x in fl:
            print (x)
    
if __name__ == "__main__":
    main()
