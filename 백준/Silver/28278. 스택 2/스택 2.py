import sys

input = sys.stdin.readline

N = int(input())
stack = []
output = []

for _ in range(N):
    cmd = input().split()

    if cmd[0] == '1':          # push
        stack.append(int(cmd[1]))

    elif cmd[0] == '2':        # pop
        if stack:
            output.append(str(stack.pop()))
        else:
            output.append('-1')

    elif cmd[0] == '3':        # size
        output.append(str(len(stack)))

    elif cmd[0] == '4':        # empty
        output.append('1' if not stack else '0')

    elif cmd[0] == '5':        # top
        if stack:
            output.append(str(stack[-1]))
        else:
            output.append('-1')

print('\n'.join(output))