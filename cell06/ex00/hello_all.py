import inspect

class MyClass:
    def method1(self):
        pass
    def method2(self):
        pass

obj = MyClass()


methods = [name for , member in inspect.getmembers(obj, predicate=inspect.ismethod)
           if member.__self__.__class__== MyClass]

print("Hollo, everyone!")
