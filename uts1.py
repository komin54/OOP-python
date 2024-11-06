class Hero: # template
    pass


herol = Hero() # object / instance (instansiate)
hero2 = Hero() 
hero3 = Hero();


herol.name = "sniper"
herol.health = 100

herol.name = "sven"
herol.health = 200

herol.name = "ucup"
herol.health = 1000

print (herol)
print (herol.__dict__)
print (herol.name)