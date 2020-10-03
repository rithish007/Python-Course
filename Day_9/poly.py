class CompileTime:
    def add(self, a, b, c=0):
        print(f'Answer = {a+b+c}')


class FirstClass:
    def run(self):
        print('Insidde the First class Run method')


class SecondClass:
    def run(self):
        print(f'Inside the second class run method')


if __name__ == "__main__":
    o = SecondClass
    o.run()
    o.run()
    
