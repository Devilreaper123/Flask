class ClassTest:
    def instance_method(self):
        print(f'Called instance method of {self}')
    @classmethod
    def class_method(cls):
        print(f"called {cls}")

# test = ClassTest()
# test.instance_method()
ClassTest.class_method()