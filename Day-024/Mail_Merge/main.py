PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    for name in names:
        name = name.strip()
        with open("./Input/Letters/starting_letter.txt") as starting_file:
            content = starting_file.read()
            invitation_message = content.replace(PLACEHOLDER, name)
        
        with open(f"./Output/ReadyToSend/invitation_{name}.txt", mode="w") as output_file:
            output_file.write(invitation_message)