import turtle

ventana = turtle.Screen()
ventana.bgcolor("black")
tortuga = turtle.Turtle()
tortuga.speed(0.3)
tortuga.color('red')


while True:
   for i in range(5):
       tortuga.forward(140)
       tortuga.right(145)
