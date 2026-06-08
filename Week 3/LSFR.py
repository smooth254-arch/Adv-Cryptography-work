def lfsr(seed, taps, length):
    register = seed
    output = []

    for _ in range(length):
        new_bit = 0
        for t in taps:
            new_bit ^= register[t]

        output.append(register[-1])
        register = [new_bit] + register[:-1]

    return output


seed = [1, 0, 0, 1]
taps = [0, 3]
result = lfsr(seed, taps, 10)

print("LFSR Output:", result)