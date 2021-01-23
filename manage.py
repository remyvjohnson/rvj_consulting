print('manage.py running!')
import sys
import utils

print("This is argv:", sys.argv)
command = sys.argv[1]
# print(command)
if command == "build":
    print("Build was specified")
    from utils import build
    build()
    print('Build Complete!')
elif command == "new":
    print("New page was specified")
    from utils import new_page
    new_page()
    print('New Page Complete!')
else:
    print('MUST ENTER EITHER: "python manage.py build" to rebuild site OR "python manage.py new" to create new page')
