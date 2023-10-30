from random import *
#floor_complexity = int(input("Floor Complexity"))
#floor_points = floor_complexity*12
roomnames = ['Armory', 'Medbay', 'Lobby', 'Hallway','Dining Room','Office','Gym','Recreation room','bathroom']
adjectives = ["Smelly", "Comfy", "Narrow", "", "", "Average-Looking", "Fancy"]
generatednames = []
#occupied_coordinates = []
d = []
connections = []
def change_cords(coordinates, generated_directions):
    result = randint(1,4)
    while result in generated_directions:
        result = randint(1,4)
    new_coordinates = coordinates.copy()
    if result == 1: #north
        new_coordinates[1] +=1
    if result == 2: #east
        new_coordinates[0] +=1
    if result == 3: #south
        new_coordinates[1] -=1
    if result == 4: #west
        new_coordinates[0] -=1
    generated_directions.append(result)
    return new_coordinates

def run_complexity():
    room_complexity1 = randint(1,20)
    room_complexity2 = randint(1,20)
    room_complexity = min(room_complexity1,room_complexity2)
    return room_complexity
##    print("Room Complexity:",room_complexity)

def run_doors():
    amount_of_doors = randint(1,3)
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

def run_room_adjective():
    roomad = adjectives[randint(0,len(adjectives)-1)]
    return(roomad)


class Room:
    def __init__(self, name, doors, complexity, adject, coordinate, num):
        self.name = name
        self.doors = doors
        self.complexity = complexity
        self.adjective = adject
        self.coordinate = coordinate
        self.num = num

i = 0
def roomgenerator(n, current_cords): #n is the number of rooms in the floor
    global i
    if i>=n:
        return 0
    for r in d:
        if r.coordinate == current_cords:
            print("Connecting "+ str(i) + " and " +str(r.num) + "because it ecountered "+str(r.num))
            connections[i].append(r.num)
            connections[r.num].append(i)
            return 0
    x = Room(name=run_room_name(), doors=run_doors(), complexity=run_complexity(), adject=run_room_adjective(), coordinate= current_cords, num= i)
    d.append(x)
    i+=1
    generated_directions = []
    for y in range(x.doors):
        res = roomgenerator(n, change_cords(current_cords, generated_directions))
        if(type(res) == Room): #if it succesfully creates a room
            print("Connecting "+ str(res.num) + " and " +str(x.num))
            connections[res.num].append(x.num)
            connections[x.num].append(res.num)
    return x
    
    
    

number = int(input("Select a number of rooms "))
for n in range(number):
    connections.append([])

roomgenerator(number, [0, 0])

print("Successfully generated " + str(len(d)) + " rooms.")
print("Here is the array of connections: ")
print(connections)


