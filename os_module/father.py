class Father:
    def jump(self):
        return "Normal jump"
class Son(Father):
    def jump(self):
        return "Cool slow-mo jump"
print(Son().jump())