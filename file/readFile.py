try:
    file = open("text.txt", "r")
    # print(file.read())
    # Read each line one by one
    for line in file:
     print(line.strip()) 
    # Read the first line
    line = file.readline()

    # while line:
    #  print(line.strip())
    #  line = file.readline()  # Read the next line
except FileNotFoundError as e:
    print("Error",e)

finally:
    file.close()