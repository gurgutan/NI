from random import choice, random

letters = (
    "абвгдеёжзийкламнопрстуфхцчшщэьъюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЭЮЯ -0123456789 "
)

target = list("моя цель - успешно сдать экзамен")
charset = letters + " "
parent = [choice(charset) for _ in range(len(target))]
minmutaterate = 0.09
C = range(100)
copies = []

perfectfitness = float(len(target))


def fitness(trial):
    "Сумма соответствующих позиции символов"
    return sum(t == h for t, h in zip(trial, target))


def mutaterate():
    "Чем меньше мутаций, тем ближе соответствие родителю"
    return 1 - (
        (perfectfitness - fitness(parent)) / perfectfitness * (1 - minmutaterate)
    )


def mutate(parent, rate):
    return [(ch if random() <= rate else choice(charset)) for ch in parent]


def que():
    print(
        "#%-4i, fitness: %4.1f%%, '%s'"
        % (iterations, fitness(parent) * 100.0 / perfectfitness, "".join(parent))
    )
    print("Варианты: ", end=" ")
    [print("'" + "".join(copies[i]), end="' ") for i in range(4)]
    print()


def mate(a, b):
    place = 0
    if choice(range(10)) < 7:
        place = choice(range(len(target)))
    else:
        return a, b

    return a, b, a[:place] + b[place:], b[:place] + a[place:]


iterations = 0
center = len(C) // 2
while parent != target:
    rate = mutaterate()
    iterations += 1
    if iterations % 10 == 0:
        que()
    copies = [mutate(parent, rate) for _ in C] + [parent]
    parent1 = max(copies[:center], key=fitness)
    parent2 = max(copies[center:], key=fitness)
    parent = max(mate(parent1, parent2), key=fitness)
que()
