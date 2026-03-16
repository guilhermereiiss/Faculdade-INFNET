def knapsack(target, weights, index=0, atual=None):
    if atual is None:
        atual = []

    if target == 0:
        print(atual)
        return

    if target < 0 or index >= len(weights):
        return

    knapsack(target - weights[index], weights, index + 1, atual + [weights[index]])
    knapsack(target, weights, index + 1, atual)

weights = [2, 3, 4, 5]
knapsack(7, weights)