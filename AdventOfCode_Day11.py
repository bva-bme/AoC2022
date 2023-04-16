class Monke:
    def __init__(self, starting_items, operation, value, test_value, target_true, target_false):
        self.starting_items = starting_items.copy()
        self.items = starting_items.copy()
        if operation == 'mul' or operation == 'add' or operation == 'sqr':
            self.operation = operation
        else:
            print('Error')
        self.value = value
        self.test_value = test_value
        self.target_true = target_true
        self.target_false = target_false

        self.thrown = 0

    def inspect(self, item):
        if self.operation == 'add':
            item += self.value
        elif self.operation == 'mul':
            item *= self.value
        else:
            item *= item
        item = int(item / 3)
        return item

    def inspect_part2(self, item):
        if self.operation == 'add':
            item += self.value
        elif self.operation == 'mul':
            item *= self.value
        else:
            item *= item
        return item

    def test(self, item):
        if item % self.test_value == 0:
            return self.target_true
        else:
            return self.target_false

    def reset(self):
        self.thrown = 0
        self.items = self.starting_items.copy()

class KeepAway:
    def __init__(self, Monkeys):
        self.Monkeys = Monkeys

    def play_round(self, part2=False, global_mod=1):
        for monke in self.Monkeys:
            while len(monke.items) > 0:
                item = monke.items.pop(0)
                if part2:
                    item = monke.inspect_part2(item)
                    item = int(item % global_mod)
                else:
                    item = monke.inspect(item)
                target = monke.test(item)
                self.Monkeys[target].items.append(item)  # throw
                monke.thrown += 1

    def find_result(self):
        throws = []
        for monke in self.Monkeys:
            throws.append(monke.thrown)
        throws.sort()
        max_1 = throws.pop(-1)
        max_2 = throws.pop(-1)

        return max_1*max_2

# Define monkeys:
monke0 = Monke([97, 81, 57, 57, 91, 61], 'mul', 7, 11, 5, 6)
monke1 = Monke([88, 62, 68, 90], 'mul', 17, 19, 4, 2)
monke2 = Monke([74, 87], 'add', 2, 5, 7, 4)
monke3 = Monke([53, 81, 60, 87, 90, 99, 75], 'add', 1, 2, 2, 1)
monke4 = Monke([57], 'add', 6, 13, 7, 0)
monke5 = Monke([54, 84, 91, 55, 59, 72, 75, 70], 'sqr', 0, 7, 6, 3)
monke6 = Monke([95, 79, 79, 68, 78], 'add', 3, 3, 1, 3)
monke7 = Monke([61, 97, 67], 'add', 4, 17, 0, 5)

# Part I

game = KeepAway([monke0, monke1, monke2, monke3, monke4, monke5, monke6, monke7])

for i in range(20):
    game.play_round()

result = game.find_result()
print(result)

# Part II


global_mod = 1
for monke in game.Monkeys:
    monke.reset()
    global_mod *= monke.test_value

for i in range(10000):
    game.play_round(part2=True, global_mod=global_mod)

result = game.find_result()
print(result)