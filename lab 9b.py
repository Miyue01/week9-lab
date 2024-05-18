#Mingxuan Yue
#Create your own github repo
#Add a .py file
#Create a simple version of an agent based simulation, based on the code in the last lecture, and the github repo linked at the end
#1. Create an Agent class
#2. Create a World class
#3. Initialize the world
#4. Create a loop
#Ask each agent in sequence to find an empty patch
#Move the agent to the empty patch
#5. End
#Keep it simple (small grid, small number of agents, small number of loops), and utilize the code from the more complex example given in lecture. 


import random

class Agent:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
    
    def move(self, world):
        empty_patch = world.find_empty_patch()
        if empty_patch:
            self.x, self.y = empty_patch
            world.update_agent_position(self)
    
    def __repr__(self):
        return f'Agent({self.id}, {self.x}, {self.y})'

class World:
    def __init__(self, width, height, num_agents):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.agents = []
        
        for i in range(num_agents):
            x, y = self.find_empty_patch()
            agent = Agent(i, x, y)
            self.agents.append(agent)
            self.grid[y][x] = agent

    def find_empty_patch(self):
        empty_patches = [(x, y) for y in range(self.height) for x in range(self.width) if self.grid[y][x] is None]
        return random.choice(empty_patches) if empty_patches else None

    def update_agent_position(self, agent):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == agent:
                    self.grid[y][x] = None
                    break
        self.grid[agent.y][agent.x] = agent

    def __repr__(self):
        return '\n'.join([' '.join(['.' if cell is None else 'A' for cell in row]) for row in self.grid])

def main():
    width, height, num_agents, num_iterations = 5, 5, 3, 10
    world = World(width, height, num_agents)
    
    print("Initial world:")
    print(world)
    
    for _ in range(num_iterations):
        for agent in world.agents:
            agent.move(world)
        print(f"\nWorld after iteration {_ + 1}:")
        print(world)

if __name__ == "__main__":
    main()

