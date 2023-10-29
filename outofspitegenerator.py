from random import *
#floor_complexity = int(input("Floor Complexity"))
#floor_points = floor_complexity*12
roomnames = ['Armory', 'Medbay', 'Lobby', 'Hallway','Dining Room','Office','Gym','Recreation room','bathroom']
generatednames = []
d = {}

def innerdice(n,m):
    thedice = randint(n,m)
    return thedice

def run_complexity():
    room_complexity1 = randint(1,20)
    room_complexity2 = randint(1,20)
    room_complexity = min(room_complexity1,room_complexity2)
    return room_complexity
##    print("Room Complexity:",room_complexity)

def run_doors():
    amount_of_doors = randint(1,4)
    if amount_of_doors == 1:
        interpr = int(innerdice(1,100))
        if interpr < 70:
            amount_of_doors = 2
    return(amount_of_doors)
##    print("Doors in the Room:",amount_of_doors)

def run_room_name():
    roomname = roomnames[randint(0,len(roomnames)-1)]
    addition = 0
    roomnametest = str(roomname)+str(addition)
    while roomnametest in generatednames:
        addition += 1
        roomnametest = str(roomname)+str(addition)
    roomname = str(roomname)+str(addition)
    generatednames.append(roomname)
    return(roomname)


class Room:
    def __init__(self, name, doors, complexity):
        self.name = name
        self.doors = doors
        self.complexity = complexity

for i in range (1,100):
    x = Room(run_room_name(), run_doors(), run_complexity())
    d["var{0}".format(i)] = x.name, x.doors, x.complexity
    print("Room Name: ",x.name)
    print("Room Doors: ",x.doors)
    print("Room Complexity: ",x.complexity)
