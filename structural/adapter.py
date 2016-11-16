class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer.'.format(self.name)

    def execute(self):
        return 'executes a program'

class Synthesizer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electronic song'

class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} the human'.format(self.name)

    def speak(self):
        return 'says hello'

class Adapter:
    def __init__(self, obj, adapted_methods): #use inspect module 
        self.obj = obj #use in __str__ method
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)

def main():
    objects = [Computer('Acer')]
    synth = Synthesizer('mongo')
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Fenng')
    objects.append(Adapter(human, dict(execute=human.speak)))

    for item in objects:
        print('{} {}'.format(str(item), item.execute()))


if __name__ == '__main__':
    main()
