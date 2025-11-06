from turtle import Turtle, Screen

from prettytable import PrettyTable
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

print("| Pokemon Name | Type | ")
print("_ _ _ _ _ _ _ _ _ _ ")
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)


