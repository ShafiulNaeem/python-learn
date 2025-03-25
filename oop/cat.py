from animal import Animal
class Cat(Animal):
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, value):
        self._color = value

    def sound(self):
        return "Meow"

cat = Cat()
cat.color = "Brown"

print(cat.color)
print(cat.sound())
print(cat.eat())
