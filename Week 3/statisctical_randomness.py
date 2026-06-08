sequence = [1, 0, 1, 1, 0, 0, 1, 0, 1, 1]

zeros = sequence.count(0)
ones = sequence.count(1)

print("Zeros:", zeros)
print("Ones:", ones)

if abs(zeros - ones) <= 2:
    print("Sequence is reasonably random")
else:
    print("Sequence is biased")