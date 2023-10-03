
dule for working with lockboxes.
"""

def canUnlockAll(boxes):
        posn = 0
            unlocked = {}

                for index in range(len(boxes)):

                        if len(boxes[index]) == 0 or index == 0:
                                    unlocked[index] = "unlocked"

                                            for key in boxes[index]:
                                                        if key < len(boxes) and key != index:
                                                                        unlocked[key] = key

                                                                                if len(unlocked) == len(boxes):
                                                                                            return True
                                                                                                return False
