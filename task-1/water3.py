def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1]==4

def successors(s):
    x, y, z = s
    

    if x>0 : #8--->5
        if y<5:
            min_var = min(x,5-y)
            yield(((x-min_var,y+min_var,z),min_var))
        if z<3:
            min_var = min(x,3-z)
            yield(((x-min_var,y,z+min_var),min_var))
    if y>0:
        if x<8:
            min_var =min(y,8-x)
            yield(((x+min_var,y-min_var,z),min_var))
        if z<3:
            min_var =min(y,3-z)
            yield(((x,y-min_var,z+min_var),min_var))
    if z>0:
        if x<8:
            min_var = min(z,8-x)
            yield(((x+min_var,y,z-min_var),min_var))
        if y<5:
            min_var = min(z,5-y)
            yield(((x,y+min_var,z-min_var),min_var))

    