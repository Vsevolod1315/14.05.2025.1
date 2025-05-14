z='z'
def setup():
    size(600,600)
def draw():
    global z
    background(0)
    text(z,300,300)
def keyPressed():
    global z
    z = key + z
    
    
