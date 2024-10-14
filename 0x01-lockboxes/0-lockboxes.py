#!/usr/bin/python3

'''solution for lockboxes puzzle'''


def open_box(key, unlocked, boxes):
    for key in boxes[key]:
        if (key not in unlocked
                and len(unlocked) < len(boxes)
                and 0 <= key < len(boxes)):
            unlocked.add(key)
            open_box(key, unlocked, boxes)
        else:
            pass


def canUnlockAll(boxes):
    unlocked = {0}
    open_box(0, unlocked, boxes)
    if (len(unlocked) < len(boxes)):
        return False
    return True
