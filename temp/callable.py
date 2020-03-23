class Student():

    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print(f"My name is {self.name}")


st = Student('Samo')

print(st.name)

st()