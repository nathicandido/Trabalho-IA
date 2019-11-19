
from random import sample, shuffle, randrange, choice
from operator import itemgetter



def get_by_tournment(populacao, populacao_com_fitness):
    competidores = sample(population, 3)
    return sorted(competidores, key=populacao_com_fitness.get)[:2]

def crossover(parents):
    crossover_point = randrange(len(parents[0]))
    first_piece = list(parents[0][:crossover_point])
    resultado_chromossomo = primeira_parte+[x for x in parents[1] if x not in primeira_parte]
    return tuple(resultado_chromossomo)

def mutatacao(chromossomo):
    i, j = sample(chromossomo, 2)
    cromo_list = list(chromossomo)
    cromo_list[i], cromo_list[j] = cromo_list[j], cromo_list[i]
    return tuple(cromo_list)


def criar_population(populacao_original,cromo_rate,populacao_com_fitness, mutacao_rate):
    nova_populacao = []
    add_populacao = nova_populacao.append
    populacao_len = len(populacao_original)
    while len(nova_populacao) < populacao_len:
        parents = get_by_tournment(populacao_original, populacao_com_fitness)

        if randrange(101) <= cromo_rate:
            novo_cromo = crossover(parents)
        else:
            novo_cromo = choice(parents)
        if randrange(101) <= mutacao_rate:
            novo_cromo = mutate(novo_cromo)
        add_populacao(novo_cromo)

    return nova_populacao


def generate_first_population(genes, population_size):
    population = []
    while len(population) < population_size:
        shuffle(genes)
        population.append(tuple(genes))
    return population


def get_best_fitted(population, cities):
    fitness = -1
    chromossome = ()
    population_with_fitness = {}
    for c in population:
        f = get_fitness(c, cities)
        if fitness == -1:
            fitness = f
            chromossome = c
        if f < fitness:
            fitness = f
            chromossome = c
        population_with_fitness[c] = f
    return fitness, chromossome, population_with_fitness


def get_fitness(chromossome, cities_matrix):
    start = -1
    fitness = 0
    for gene in chromossome:
        if start < 0:
            start = gene
            continue
        fitness += cities_matrix[start][gene]
        start = gene
    return fitness+cities_matrix[start][chromossome[0]]


def run(cities_matrix, population_size, generations, cross_rate, mutation_rate):
    genes = list(range(len(cities_matrix)))
    population = generate_first_population(genes, population_size)
    fitness = 0
    convergence_count = 0
    diversity = 1

    for i in range(generations):
        new_fitness, best_fitted, pop_with_fitness = get_best_fitted(population,
            cities_matrix)

        diversity = len(pop_with_fitness)/population_size

        if new_fitness < fitness or not fitness:
            fitness = new_fitness
            convergence_count = 0
        elif fitness == new_fitness:
            convergence_count += 1
        if convergence_count > 5:
            break

        population = create_new_population(population, pop_with_fitness, cross_rate, mutation_rate)

    return fitness, best_fitted, diversity


if __name__ == '__main__':


    matrix_file = 1/5
    generations_number = 300
    mutation_rate = 1

    f = open(filename, 'r')

    matrix = []
    for line in f.readlines():
        matrix.append([int(x) for x in line.split(' ')])

    pop_size = int(args.population_size)
    crossover_rate = int(args.crossover_rate)
    mutation_rate = int(args.mutation_rate)
    generations = int(args.generations_number)
    cProfile.run('print(run(matrix, pop_size, generations, crossover_rate, mutation_rate))')
