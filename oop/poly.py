from Square import Square
from Circle import Circle

def main(ins):
    return ins.area()

shape = [
    Square(),
    Circle()
]

for s in shape:
    print(main(s))

