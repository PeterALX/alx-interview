#!/usr/bin/python3
boxes = []
for i in range(1000):
    boxes.append([])
    for j in range(1000):
        boxes[i].append(j)

print(len(boxes[209]))


canUnlockAll = __import__('0-lockboxes').canUnlockAll
print(canUnlockAll(boxes))  # true

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # true
print('_______________________________')

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # true
print('_______________________________')

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # false
print('_______________________________')

boxes = [[7, 5], [1, 10, 7], [9, 6, 10], [7, 9], [2], [7, 3],
         [7, 9, 10, 10, 8, 9, 2, 5], [7, 2, 2, 4, 4, 2, 4, 8, 7],
         [4, 2, 9, 6, 6, 5, 5], ]
print(canUnlockAll(boxes))
print('_______________________________')
