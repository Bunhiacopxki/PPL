
class Utils:
    def lookup(self, name, lst, func):
        for x in lst:
            if name.name == func(x):
                return x
        return None
