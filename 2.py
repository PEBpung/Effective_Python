class A:
    def __str__(self):
        return 'True'
    def __repr__(self):
        return 'False'

a = A()

print(a)
print(repr(a))

