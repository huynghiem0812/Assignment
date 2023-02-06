def mutation(string, position, character):
    l, i = list(), 0
    while i < len(string):
        if i == position:
            l += [character]
        else:
            l += [string[i]]
        i += 1
    return ''.join(l)

def get_input():
    while True:
        raw = input("Position: ")
        try:
            try:
                num = int(raw)
            except:
                raise Exception("Must be a positive number! ")

            if num < 0:
                raise Exception("The number must be positive.")

            return num

        except Exception as e:
            print(e)
            continue

if __name__ == '__main__':
    s = input("String: ")
    i = get_input()
    c = input("Character: ")
    s_new = mutation(s, int(i), c)
    print(s_new)
