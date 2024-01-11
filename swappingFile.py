def swapFileData(file1, file2):
    try:
        with open(file1, 'r') as file1_object:
            data_a = file1_object.read()

        with open(file2, 'r') as file2_object:
            data_b = file2_object.read()

        with open(file1, 'w') as file1_object:
            file1_object.write(data_b)

        with open(file2, 'w') as file2_object:
            file2_object.write(data_a)

        print("Swapping of data between", file1, "and", file2, "is successful.")
    except Exception as e:
        print("An error occurred:", str(e))

file1_name = input("Enter the name of the first file (e.g., sample1.txt): ")
file2_name = input("Enter the name of the second file (e.g., sample2.txt): ")

swapFileData(file1_name, file2_name)
