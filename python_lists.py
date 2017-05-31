""" Given a specified number of commands, executes inputted
    english commands on one main list
"""
if __name__ == '__main__':
    N = int(input())
    c_list = list()
    for i in range(0, N):
        command = input().split()
        if command[0] == 'insert':
            c_list.insert(int(command[1]), int(command[2]))
        elif command[0] == 'append':
            c_list.append(int(command[1]))
        elif command[0] == 'sort':
            c_list.sort()
        elif command[0] == 'reverse':
            c_list.reverse()
        elif command[0] == 'remove':
            c_list.remove(int(command[1]))
        elif command[0] == 'pop':
            c_list.pop()
        else:
            print(c_list)
