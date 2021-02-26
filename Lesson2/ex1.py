def f21(x):
    if x[1] == 1963:
        return 8
    elif x[1] == 2012:
        if x[3] == 'mupad':
            return 9
        elif x[3] == 'rust':
            return 10
    elif x[1] == 1991:
        if x[2] == 'csv':
            if x[3] == 'mupad':
                return 0
            elif x[3] == 'rust':
                return 1
        elif x[2] == 'mql5':
            if x[0] == 'flux':
                return 2
            elif x[0] == 'ruby':
                return 3
            elif x[0] == 'zimpl':
                return 4
        elif x[2] == 'terra':
            if x[0] == 'flux':
                return 5
            elif x[0] == 'ruby':
                return 6
            elif x[0] == 'zimpl':
                return 7


# print(f21(['ruby', 1991, 'mql5', 'mupad']))
# print(f21(['ruby', 1991, 'csv', 'mupad']))
