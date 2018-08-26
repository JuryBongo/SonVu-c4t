from turtle import*

turtle_list = []
for i in range(5):
    t = Turtle()
    turtle_list.append(t)
j = int(input("Turtle position?"))
b = (input('Turtle color?'))
a = (input("Turtle shape?"))
cmd = (input("Turtle command?")).lower()
turtle_list[j].color(b)
turtle_list[j].shape(a)
if cmd == 'forward':
    turtle_list[j].forward(100)
elif cmd == 'backward':
    turtle_list[j].backward(100)
elif cmd == 'left':
    turtle_list[j].left(90)
elif cmd == 'right':
    turtle_list[j].right(90)
else:
    print("I don't understand your command")

mainloop()