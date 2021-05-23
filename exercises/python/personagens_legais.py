characters_file = open("meus-personagens-favoritos.txt", mode="w")

characters_file.write("Tio Patinhas\n")
characters_file.write("papa é pop\n")
characters_file.write("myster boy\n")

print("batman", file=characters_file)

more_characters = ["alphoce\n", "eduard\n"]

characters_file.writelines(more_characters)

characters_file.close()
