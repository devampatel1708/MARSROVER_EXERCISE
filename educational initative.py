# Define the Rover class
class Rover:
    def __init__(self, x, y, direction, grid_width, grid_height, obstacles):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.obstacles = obstacles

    def move(self):
        new_x, new_y = self.calculate_new_position()
        if self.is_valid_move(new_x, new_y):
            self.x, self.y = new_x, new_y

    def calculate_new_position(self):
        if self.direction == 'N':
            return self.x, self.y + 1
        elif self.direction == 'S':
            return self.x, self.y - 1
        elif self.direction == 'E':
            return self.x + 1, self.y
        elif self.direction == 'W':
            return self.x - 1, self.y

    def is_valid_move(self, x, y):
        if 0 <= x < self.grid_width and 0 <= y < self.grid_height and (x, y) not in self.obstacles:
            return True
        return False

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'N'

    def get_status_report(self):
        return f"Rover is at ({self.x}, {self.y}) facing {self.direction}. No Obstacles detected."

# Define the Grid class
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

# Define the Command pattern
class Command:
    def execute(self, rover):
        pass

class MoveCommand(Command):
    def execute(self, rover):
        rover.move()

class TurnLeftCommand(Command):
    def execute(self, rover):
        rover.turn_left()

class TurnRightCommand(Command):
    def execute(self, rover):
        rover.turn_right()

# ... (rest of the code remains the same)


# Main program
if __name__ == "__main__":
    grid = Grid(10, 10)
    obstacles = [(2, 2), (3, 5)]
    rover = Rover(0, 0, 'N', grid.width, grid.height, obstacles)

    commands = ['M', 'M', 'R', 'M', 'L', 'M']
    command_objects = []

    for cmd in commands:
        if cmd == 'M':
            command_objects.append(MoveCommand())
        elif cmd == 'L':
            command_objects.append(TurnLeftCommand())
        elif cmd == 'R':
            command_objects.append(TurnRightCommand())

    for command in command_objects:
        command.execute(rover)

    print(f"Final Position: ({rover.x}, {rover.y}, {rover.direction})")
    print(rover.get_status_report())
