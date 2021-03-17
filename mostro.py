'''fa in modo che il mostro non possa uscire dalla griglia'''

class Entity: 
    def __init__(self, x, y, field): #inizializzando l'istanza con il costruttore init
        self.x = x
        self.y = y
        self.field = field
        self.field.entities.append(self) #aggiungo entity al field

    def move(self, direction):
        if direction == "up":
          self.y -= 1
        elif direction == "down":
          self.y += 1
        elif direction == "right":
          self.x += 1
        elif direction == "left":
          self.x -= 1

    def controllo(self):
        if self.x > self.field.w:
            print("l'entità non può muoversi più a destra")
            self.x -= 1
        elif self.x < 1:
            print("l'entità non può muoversi più a sinistra")
            self.x += 1
        elif self.y > self.field.h:
            print("l'entità non può muoversi più in basso")
            self.y -= 1
        elif self.y < 1:
            print("l'entità non può muoversi più in alto")
            self.y += 1
class Monster(Entity):
    def __init__(self, x, y, name, damage, field):
        super().__init__(x, y, field)
        self.name = name 
        self.hp = 20 # vita
        self.damage = damage

    def info(self):
        print("sono", self.name, "hp:", self.hp, "/20", "e mi trovo a (", self.x, ",", self.y, ")")
    def attack(self, enemy):
        if self.hp <= 0:
            print("non è possibile attaccare,", self.name, "è morto")
        else:
            print(self.name, "attacca", enemy.name)
        if enemy.hp <= 0:
            print(enemy.name, "è morto")
        else:cdf5
            enemy.hp -= self.damage
class Field:
    def __init__ vcx(self):
        self.w = 6
        self.h = 6
        self.entities = []
    def draw(self):
        for y in range(self.h):
          for x in range(self.w):
            for e in self.entities:
              if x + 1 == e.x and y + 1 == e.y:
                print("[+]", end = "")
                break
            else: # nel ciclo for di e
              print("[ ]", end = "")
          print()

field = Field() # creo il campo

m = Monster(2, 2, "Paolo", 10, field)
m1 = Monster(1, 1, "Giorgio", 10, field)
field.draw() # disegno il campo
m.info()
m1.info()
field.draw()

for n in range(5): # se faccio questo esce dalla griglia
    print()
    m.move("down")
    m.controllo()
    m.info()
    m1.info()
    field.draw()

print()
m1.move("down")
m1.controllo()
m.info()
m1.info()
field.draw()

for a in range(3):
    print()
    m.attack(m1)
    m.info()
    m1.info()
    field.draw()

print()
m1.attack(m)
m.info()
m1.info()
field.draw()