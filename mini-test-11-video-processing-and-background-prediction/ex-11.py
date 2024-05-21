import matplotlib.pyplot as plt

# Existing code to compute results
It = [0, 1, 2, 1, 2, 1, 0, 2, 1, 8, 1, 3, 0]
D = {0: 3, 1: 5, 2: 3, 3: 1, 8: 1}
p = 0.5

results = []

for i in It:
    Di = D[i] / 13
    numerator = Di * p
    denominator = (Di * p) + ((1 - p) * (1 / 10))
    p = numerator / denominator
    results.append(str(100*(1-p))[:6])

print(results)