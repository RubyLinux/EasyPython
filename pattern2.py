import turtle

Lucifer=turtle.Turtle()
colors = ["green", "black"]
turtle.fill

for i in range(1000):
	Lucifer.pencolor(colors[i%2])
	Lucifer.fillcolor(colors[i%2])
	Lucifer.begin_fill()
	while True:
		Lucifer.forward(300)
		Lucifer.left(170)
		if abs(Lucifer.pos())<1:
			break
	Lucifer.end_fill()


turtle.done()
