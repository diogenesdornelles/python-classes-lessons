from dataclasses import dataclass, field


@dataclass
class CheckName:
    name: str
    result: bool = field(default=False)

    def __post_init__(self):
        if self.name != '' and isinstance(self.name, str):
            self.result = True
            return self.name
        else:
            if self.name == '':
                print('Name must be given.')
                #  raise ValueError('Name must be given.')
            elif isinstance(self.name, str) is False:
                print('Name must be type str.')
                #  raise TypeError('Name must be type str.')


@dataclass
class CheckAge:
    age: int
    result: bool = field(default=False)

    def __post_init__(self):
        if self.age >= 0 and isinstance(self.age, int):
            self.result = True
            return self.age
        else:
            print('Age integer positive must be given.')
            #  raise [(ValueError, TypeError), 'Age integer positive must be given.']
