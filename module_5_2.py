class House:
    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors

    # def go_to(self, new_floor):
    #     self.new_floor = new_floor
    #     for i in range(1, self.new_floor+1):
    #         if 1 <= self.new_floor <= self.num_of_floors:
    #             print (i)
    #     if 1 < self.new_floor > self.num_of_floors:
    #         print('Такого этажа не существует')

    def __len__(self):
        return self.num_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.num_of_floors}'


h1 = House("ЖК Эльбрус", 10)
h2 = House("ЖК Акация", 20)

print(h1)
print(h2)

print(len(h1))
print(len(h2))
