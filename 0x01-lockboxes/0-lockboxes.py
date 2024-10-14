#!/usr/bin/python3
'''solution for lockboxes puzzle'''


def open_box(key, unlocked, boxes):
    '''
    checks if keys in a box have been opened
    if a key hasn't been opened,
        adds the key to the set of unlocked boxes and opens it
    it is called recursively until
        either all boxes are open or no other boxes can be opened
    no return value,
        it modifies a set:unlocked to keep track of unlocked boxes
    '''
    toUnlock = set()
    for key in boxes[key]:
        if (len(unlocked) >= len(boxes)):
            break
        if (key in unlocked):
            continue
        if key < 0 or key >= len(boxes):
            continue
        unlocked.add(key)
        toUnlock.add(key)
    for key in toUnlock:
        open_box(key, unlocked, boxes)


def canUnlockAll(boxes):
    '''
    returns true if all boxes can be opened from only the 0th box being opened
    otherwise returns false
    '''
    unlocked = {0}
    open_box(0, unlocked, boxes)
    if (len(unlocked) < len(boxes)):
        return False
    return True
