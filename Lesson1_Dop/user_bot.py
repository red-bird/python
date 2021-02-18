import random
import random_bot


def script(check, x, y):
    if check("level") == 1:
        if not check('wall', x+2, y):
            if check('gold', x, y):
                return 'take'
            return 'right'
        if check('gold', x, y):
            return 'take'
        return 'down'

    if check('level') == 2:
        # follow gold
        if check('gold', x, y):
            return 'take'
        if check('gold', x+1, y) or check('gold', x+2, y):
            return 'right'
        if check('gold', x-1, y) or check('gold', x-2, y):
            return 'left'
        if check('gold', x, y+1):
            return 'down'
        if check('gold', x, y-1):
            return 'up'
        # start move
        if x == 0:
            return 'right'

        # chase gold 'tale'
        return 'up'

    if check('level') == 3:
        if check('gold', x, y):
            return 'take'
        # wall left & not up
        if check('wall', x-1, y) and not check('wall', x, y-1):
            return 'up'
        # wall up & not right
        if check('wall', x, y-1) and not check('wall', x+1, y):
            return 'right'
        # wall down
        if check('wall', x, y+1):
            return 'left'
        # wall right
        if check('wall', x+1, y):
            return 'down'
        # left-up
        if check('wall', x-1, y-1):
            return 'up'
        # right-up
        if check('wall', x+1, y-1):
            return 'right'
        # left-down
        if check('wall', x-1, y+1):
            return 'left'
        # right-down
        if check('wall', x+1, y+1):
            return 'down'

    if check('level') == 4:
        if check('gold', x, y):
            return 'take'

        # get to center through left-down tunnel
        if check('wall', x-1, y) and check('wall', x+2, y) and check('wall', x-1, y-3):
            return 'right'

        #
        if check('wall', x, y+2) and check('wall', x, y-3) and (check('gold', x+4, y-6) or check('gold', x+4, y-5)):
            return 'up'
        # if check('wall', x, y+1) and check('wall', x, y-2) and check('empty', x, y-1) and check('empty', x, y-2):
        #     return 'up'

        # wall up & not right
        if check('wall', x, y - 1) and not check('wall', x + 1, y):
            return 'right'
        # wall right & not down
        if check('wall', x + 1, y) and not check('wall', x, y+1):
            return 'down'
        # wall left & not up
        if check('wall', x - 1, y) and not check('wall', x, y - 1):
            return 'up'
        # wall down
        if check('wall', x, y + 1):
            return 'left'
        # right-up
        if check('wall', x + 1, y - 1):
            return 'right'
        # left-up
        if check('wall', x - 1, y - 1):
            return 'up'
        # left-down
        if check('wall', x - 1, y + 1):
            return 'left'
        # right-down
        if check('wall', x + 1, y + 1):
            return 'down'

    return "pass"
