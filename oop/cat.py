from animal import Animal
class Cat(Animal):
    __color = "Black"
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, value):
        self.__color = value

    def sound(self):
        return "Meow"
    
    # encapsulation : private
    __age = 0
    # encapsulation : getter
    @property
    def age(self):
        return self.__age
    # encapsulation : setter
    @age.setter
    def age(self, value):
        self.__age = value

    # month calculation from age using private method
    def __age_to_month(self):
        return self.__age * 12
    
    def show_month(self):
        return f"""
        Cat age is {self.__age} year(y) and 
        {self.__age_to_month()} month(m)
        """
    def _cat_info(self):
        return f"""
        Cat is a domestic animal.
        Cat is a small carnivorous mammal.
        Cat color is {self.color}.
        Cat sound is {self.sound()}.
        Cat age is {self.age} year(y).
        Cat age is {self.__age_to_month()} month(m).
        Cat eat {self.eat()}.
        """
    
cat = Cat()
print("=== private property ===")
cat.age = .5
print(cat.show_month())
print("=== protected property ===")
cat.color = "White"
print(cat._cat_info())

