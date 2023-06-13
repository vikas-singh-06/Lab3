def write_text_file():
    name = input("Enter your name: ")
    file_name = "output.txt"

    with open(file_name, "w") as file:
        file.write(name)

    print(f"A text file '{file_name}' has been created with your name.")

write_text_file()
