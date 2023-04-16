import random
import math

class Valve:
    def __init__(self, pressure_rate, destinations):
        self.state = False # off
        self.pressure_rate = pressure_rate
        self.released_pressure = 0
        self.destinations = destinations

    def tick(self):
        if self.state:
            self.released_pressure += self.pressure_rate

    def open(self):
        self.state = True

    def close(self):
        self.state = True


def construct_graph(file):
    lines = file.readlines()
    graph = {}
    graph_lookup = []
    max_routes = 0
    for line in lines:
        first_half, second_half = line.split(';')
        valve_name = first_half[6:8]
        pressure_rate = int(first_half[first_half.find('rate=')+5:])
        destinations_str = second_half[second_half.find("to valves ")+10:-1]
        destinations = destinations_str.split(', ')
        if len(destinations) > max_routes:
            max_routes = len(destinations)
        graph_lookup.append(valve_name)
        graph[valve_name] = Valve(pressure_rate, destinations)

    return graph, graph_lookup, max_routes


class Env:
    def __init__(self, graph, graph_lookup):
        self.cumulated_pressure = 0
        self.time_remaining = 30
        self.graph = graph
        self.graph_lookup = graph_lookup
        self.state = [0] * len(self.graph)

    def update_pressures(self):
        for node in self.graph:
            if self.graph[node].state:
                self.graph[node].tick()
                self.cumulated_pressure += self.graph[node].pressure_rate

    def reset(self):
        self.cumulated_pressure = 0
        self.time_remaining = 30

        self.state = [0] * len(self.graph)

        for valve in self.graph:
            self.graph[valve].close()

    def step(self, action):
        if action == 0:
            self.graph[self.state[-1]].open()
        elif action < len(self.graph[self.graph_lookup[self.state[-1]]].destinations):
            pass
        else:
            new_state_name = self.graph[self.graph_lookup[self.state[-1]]].destinations[action - 1]
            self.state[-1] = self.graph_lookup.index(new_state_name)

        self.time_remaining -= 1
        self.update_pressures()

        if self.time_remaining == 0:
            done = True
        else:
            done = False

        return self.state, self.cumulated_pressure, done

class Agent:
    def __init__(self, max_valves, max_actions):
        self.num_actions = max_actions
        self.num_states = math.pow(2, max_valves - 1) +
        self.Q_table = [[0 for col in range(max_actions)] for row in range(max_valves)]
        self.epsilon_min = 0.05
        self.decay = 0.995
        self.epsilon = 1

    def take_action(self, state):
        self.epsilon = max(self.epsilon_min, self.epsilon * self.decay)

        if random.random() < self.epsilon:
            action = random.choice(self.num_actions)
        else:
            action = self.Q_table[state[-1]].index(self.Q_table[state[-1]])
        return action

    def update_q_table(self, state, action):

        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])

        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)


file = open("input_day16.txt", 'r')

graph, graph_lookup, max_dest = construct_graph(file)
print('asd')
