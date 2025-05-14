z=300
x=300
def setup():
    size(600,600)
def draw():
    global z,x
    fill(255,176,3)
    rect(120,100,70,70)
    rect(300,100,70,70)
    rect(210,100,70,70)
    rect(210,10,70,70)
    ellipse(z,x,30,30)
def mouseClicked():
    global z,x
    if mouseX >210 and mouseX < 360 and mouseY > 10 and mouseY < 80 :
        x=x-2
    if mouseX >210 and mouseX < 360 and mouseY > 100 and mouseY < 170 :
        x=x+2
    if mouseX >300 and mouseX < 450 and mouseY > 100 and mouseY < 170 :
        z=z+2
    if mouseX >120 and mouseX < 270 and mouseY > 100 and mouseY < 170 :
        z=z-2
        
