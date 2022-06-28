class Zoo:
    __animals = 0

    def __init__(self,name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self,species,name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals +=1

    def get_info(self,species):
        if species == "mammal":
            print(f"Mammals in {self.name}: {', '.join(self.mammals)}")
        elif species == "fish":
            print(f"Fishes in {self.name}: {', '.join(self.fishes)}")
        elif species == "bird":
            print(f"Birds in {self.name}: {', '.join(self.birds)}")
        print(f"Total animals: {zoo.__animals}")


name = input()

zoo = Zoo(name)
n = int(input())

for i in range(n):
    line = input().split()

    species = line[0]
    animal = line[1]

    zoo.add_animal(species,animal)

specie = input()

zoo.get_info(specie)


