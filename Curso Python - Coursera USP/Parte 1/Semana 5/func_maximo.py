def maximo(x, y, z):
    if z > x and y:
        return z
    if y > x and z:
        return y
    else:
        return x
