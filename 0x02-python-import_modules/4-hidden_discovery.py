#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for val in dir(hidden_4):
        if val[0] != '_' and val[1] != '_':
            print(val)