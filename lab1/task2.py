def overlap(u, v):
    return [x for x in u if x in v]

print(overlap([1.0, 2.0, 4.5], [2.0, 4.5, 5.0]))
def join(u, v):
    bucket = [x for x in u]
    bucket += [x for x in v if x not in u]
    return bucket

print(join([1.0, 2.0, 4.5], [2.0, 4.5, 5.0]))
