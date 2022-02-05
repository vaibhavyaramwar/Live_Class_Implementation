from pkg1 import pkg1test1
import pkg2test2
import MyModule

def test2():
    print("This is my function inside package2 test1 module")

test2()
pkg1test1.test1()
pkg2test2.test2()
print(MyModule.get_course())
print(MyModule.get_greetings())