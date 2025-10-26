#CSC3600 lab10
#Name:He yuke
#No:217885
#Goal:“Genetic Algorithm: Nature-inspired Optimization Technique”

import random
import string

# Target string
TARGET = "Genetic Algorithm: Nature-inspired Optimization Technique"

# Gene pool: uppercase, lowercase, digits, space, and common punctuation
GENE_POOL = string.ascii_letters + string.digits + " :.-"

# Genetic algorithm parameters
POPULATION_SIZE = 100
MUTATION_RATE = 0.01

# Generate a random individual (chromosome)
def generate_individual(length):
    return ''.join(random.choice(GENE_POOL) for _ in range(length))

# Fitness function: count mismatched characters (lower is better)
def calculate_fitness(individual):
    return sum(1 for a, b in zip(individual, TARGET) if a != b)

# Crossover: mix genes from two parents
def crossover(parent1, parent2):
    return ''.join(parent1[i] if random.random() < 0.5 else parent2[i] for i in range(len(TARGET)))

# Mutation: randomly change some genes
def mutate(individual):
    return ''.join(
        gene if random.random() > MUTATION_RATE else random.choice(GENE_POOL)
        for gene in individual
    )

# Initialize the population
population = [generate_individual(len(TARGET)) for _ in range(POPULATION_SIZE)]

generation = 0
while True:
    # Sort population based on fitness (ascending)
    population = sorted(population, key=calculate_fitness)

    # Check if the best individual matches the target
    if calculate_fitness(population[0]) == 0:
        print(f"\n✅ Target matched in generation {generation}")
        print("Result:", population[0])
        break

    # Select top 20% of population as parents
    parents = population[:POPULATION_SIZE // 5]

    # Create new generation through crossover and mutation
    next_generation = []
    while len(next_generation) < POPULATION_SIZE:
        parent1, parent2 = random.sample(parents, 2)
        child = crossover(parent1, parent2)
        child = mutate(child)
        next_generation.append(child)

    population = next_generation
    generation += 1

    # Optional: log progress every 100 generations
    if generation % 100 == 0:
        best = population[0]
        print(f"Generation {generation} | Best: {best} | Fitness: {calculate_fitness(best)}")
