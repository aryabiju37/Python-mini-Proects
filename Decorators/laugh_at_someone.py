from random import choice
def person(name):
    def get_laugh():
        laugh = choice(("LOL","HAHA","HEHE"))
        return "{} at {}".format(laugh,name)
    return get_laugh


laugh_at = person("Jake")
print(laugh_at())


