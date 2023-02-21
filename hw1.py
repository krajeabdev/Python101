import turtle
t = turtle.Pen()
t.shape('turtle')
t.color("blue")
t.penup()
t.setpos(100,80)
t.pendown()
for j in range(5):
   for i in range(5):
    t.forward(100)
    t.left(144)
        
   t.penup()   
   t.setpos(-100*j,-80*j)
   t.pendown()

t.penup()
t.setpos(0,0)
t.pendow()
t.done()

    
