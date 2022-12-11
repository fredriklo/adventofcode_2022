visible_trees = 0
scenic_scores = []
all_rows = [[line.rstrip()] for line in open("8des.txt").readlines()]
for row in range(0, len(all_rows)):
    current_row = all_rows[row][0]
    for item in range(0, len(current_row)):
        current_item = current_row[item]
        if row == 0 or row == len(all_rows) - 1 or item == 0 or item == len(current_row) - 1:
            visible_trees += 1
        else:
            check_column_below = [int(all_rows[check_row][0][item]) for check_row in range(len(all_rows) - 1, row, -1)]
            check_column_above = [int(all_rows[check_row][0][item]) for check_row in range(row - 1, -1, -1)]
            check_row_left = [int(item) for item in current_row[0:int(item)]]
            check_row_right = [int(item) for item in current_row[int(item)+1::]]
            if all(i < int(current_item) for i in check_column_below) or all(i < int(current_item) for i in check_column_above) \
                or all(i < int(current_item) for i in check_row_left) or all(i < int(current_item) for i in check_row_right):
                visible_trees += 1

            scores = {"down": 0, "up": 0, "left": 0, "right": 0}
            for tree in reversed(check_column_below):
                if int(tree) < int(current_item):
                    scores["down"] += 1
                else:
                    scores["down"] += 1
                    break

            for tree in check_column_above:
                if int(tree) < int(current_item) or int(tree) == 0:
                    scores["up"] += 1
                else:
                    scores["up"] += 1
                    break
            for tree in reversed(check_row_left):
                if int(tree) < int(current_item):
                    scores["left"] += 1
                else:
                    scores["left"] += 1
                    break

            for tree in check_row_right:
                if int(tree) < int(current_item):
                    scores["right"] += 1
                else:
                    scores["right"] += 1
                    break

            scenic_scores.append(scores["down"] * scores["up"] * scores["left"] * scores["right"])

print("Part 1: ", visible_trees)
print("Part 2: ", max(scenic_scores))


