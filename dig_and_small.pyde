z=100
def setup():
   size(600,600)    
def draw():
    global z
    ellipse(300,300,z,z)
    if keyPressed:
       if key == 'i' or key == 'I':
           z=z+2
       if key == 'o' or key == 'O':
           z=z-2  
       
       
