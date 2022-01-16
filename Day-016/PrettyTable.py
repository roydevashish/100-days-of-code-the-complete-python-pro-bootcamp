from prettytable import PrettyTable

app = PrettyTable()

app.field_names = ["Pokemon Name", "Type"]
app.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"]
    ]
)

app.align["Pokemon Name"] = "l"
app.align["Type"] = "r"
print(app)