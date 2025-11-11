import random
def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)

def print_gen():
    list_random = []
    for i in gen_random(5,1,3):
        list_random.append(i)
    print(*list_random)
