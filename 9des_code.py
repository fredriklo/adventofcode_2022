def move(rope, idx, direction):
    head_moves = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
    if idx == 0:
        return [sum(i) for i in zip(rope[idx], head_moves[direction[0]])]
    distances = [rope[idx][0]-rope[idx-1][0], rope[idx][1]-rope[idx-1][1]]
    moves = [-1 if distances[i] > 0 else 0 if distances[i] == 0 else 1 for i in range(2)]
    chebyshev = max(abs(rope[idx][i]-rope[idx-1][i]) for i in range(2)) > 1
    return [sum(dist) for dist in zip(rope[idx], moves)] if chebyshev else rope[idx]


def full_path(knots):
    visited_positions = []
    rope = [[0,0]] * knots
    for command in [[line.rstrip()] for line in open("9des.txt").readlines()]:
        for repetition in range(int(command[0][2::])):
            for idx, knot in enumerate(rope):
                rope[idx] = move(rope, idx, command[0][0])
                if idx == len(rope)-1 and rope[idx] not in visited_positions:
                    visited_positions.append(rope[idx])
    return len(visited_positions)


print("Part 1: ", full_path(2))
print("Part 2: ", full_path(10))


