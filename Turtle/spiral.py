import turtle
wn = turtle.Screen()
wn.bgcolor('Dark Slate Gray')
wn.title('Kokoro saves your heart')
kokoro = turtle.Turtle()
kokoro.color('Medium Turquoise')
radius = 1
for i in range(180):
    kokoro.fd(10)
    kokoro.lt(radius)
    radius += 1 + (-10 * i)
        
