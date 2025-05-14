z=30
def setup():
    size(600,600)
def draw():
    global z
    fill(250,125,0)
    push()
    translate(300,230)
    rotate(radians(z))
    rect(0,0,100,100)
    pop()
    push()
    translate(300,230)
    rotate(radians(z))
    rect(0,0,30,30)
    pop()
    push()
    translate(280,240)
    rotate(radians(z))
    rect(0,0,40,40)
    pop()
    if keyPressed:
        if key =='d'or key == 'D':
            z=z+2
        if key == 'a' or key == 'A':
            z=z-2
    
        
    
    
