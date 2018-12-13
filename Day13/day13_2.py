import sys

available_states = ['^','>','v','<']
data = [list(line) for line in open("d:\\AoC2018\\Day13\\day13.txt", "r").readlines()]
y_max = len(data)
x_max = len(data[0])

class Cart:
    def __init__(self, x,y,state, id):
        self.id = id
        self.x = x
        self.y = y
        self.state = state
        self.available_turns = ['l', 's','r']
        self.intersection = 0
        if state == '^' or state == 'v':
            self.previous_position = '|'
        else:
            self.previous_position = '-'
    def __str__(self):
        return "X: {0}, Y: {1}, state: {2}".format(self.x, self.y, self.state)
    def __repr__(self):
        return "X: {0}, Y: {1}, state: {2}".format(self.x, self.y, self.state)
    def cross_intersection(self):
        turn = self.available_turns[self.intersection % len(self.available_turns)]
        index = available_states.index(self.state)
        if turn == 'l':
            self.state = available_states[(index - 1) % 4]
        elif turn == 'r':
            self.state = available_states[(index + 1) % 4]
        self.intersection += 1

def fetchCarts(carts, data):
    i = 0
    for y in range(0, y_max):
        for x in range(0, x_max):
            if data[y][x] in available_states:
                carts.append(Cart(x,y, data[y][x], i))
                i += 1


def printPlane(data):
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            sys.stdout.write(data[y][x])
    print()

def move(carts, data):
    carts.sort(key=lambda k: k.y)
    toRemove = []
    for cart in carts:
        if cart in toRemove:
            continue
        data[cart.y][cart.x] = cart.previous_position
        #MOVE CART
        if cart.state == '>':
            cart.x += 1
        elif cart.state == '<':
            cart.x -= 1
        elif cart.state == '^':
            cart.y -= 1
        elif cart.state == 'v':
            cart.y += 1

        #UPDATE PLANE
        if data[cart.y][cart.x] == "\\":
            if cart.state == '^':
                cart.state = '<'
            elif cart.state == '>':
                cart.state = 'v'
            elif cart.state == 'v':
                cart.state = '>'
            else:
                cart.state = '^'
        elif data[cart.y][cart.x] == '/':
            if cart.state == '<':
                cart.state = 'v'
            elif cart.state == '^':
                cart.state = '>'
            elif cart.state == 'v':
                cart.state = '<'
            else:
                cart.state = '^'
        elif data[cart.y][cart.x] == '+':
            cart.cross_intersection()
        elif data[cart.y][cart.x] in available_states:
            colliding = [c for c in carts if c.y == cart.y and c.x == cart.x and c.id != cart.id]
            data[cart.y][cart.x] = colliding[0].previous_position
            toRemove.append(cart)
            toRemove.append(colliding[0])
            continue
        
        cart.previous_position = data[cart.y][cart.x]
        data[cart.y][cart.x] = cart.state
    
    if len(toRemove) > 0:
        return True, toRemove

    return False, []

carts = []
fetchCarts(carts, data)
collisionDetected = False

while len(carts) > 1:
    collisionDetected, toRemove = move(carts, data)
    if collisionDetected:
        for c in toRemove:
            carts.remove(c)

print("RESULT: ", carts[0].x, carts[0].y)
    
    

