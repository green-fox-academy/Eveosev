import sys
import todo
key = sys.argv[1]

if key == 'l':
    result = todo.call_todo_list()
    for row in result:
        print(row)
elif key == 'a':
    result = todo.add_todo_event(sys.argv[2])
    for row in result:
        print(row)
elif key == 'c':
    result = todo.check_event(sys.argv[2])
    for row in result:
        print(row)
elif key == 'r':
    result = todo.remove_event(sys.argv[2])
    for row in result:
        print(row)

