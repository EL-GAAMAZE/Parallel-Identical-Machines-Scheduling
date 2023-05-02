import random

#global variables
MUTAUTION_RATE=0.1
CROSSOVER_RATE=0.9
GENERATIONS=100
POP_SIZE=50

#initialize population
def initialize_population(num_individuals, num_jobs,num_machines):
    population = []
    for _ in range(num_individuals):
        individual = [random.randint(1,num_machines) for _ in range(num_jobs)]
        population.append(individual)
    return population

#fitness function which is the maximum completion time
def calculate_makespan(individual, processing_times,num_machines):
    machine_time=[0 for _ in range(num_machines)]
    for machine in range(1,num_machines+1):
        for gene in range(len(individual)):
            if individual[gene]==machine:
                machine_time[individual[gene]-1]+=processing_times[gene]
    return max(machine_time)

#single ponit crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1)-1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2



def mutation(individual,num_machines):
    global MUTAUTION_RATE
    aleles=range(1,num_machines+1)
    mutated_individual = individual
    for i in range(len(individual)):
        if random.random() < MUTAUTION_RATE :
           mutated_individual[i]=random.choice(aleles)
    return mutated_individual

def genetic_algorithm(num_individuals, num_generations, processing_times,num_jobs,num_machines):
    global MUTAUTION_RATE,CROSSOVER_RATE
    population = initialize_population(num_individuals,num_jobs,num_machines)
    for i in range(num_generations):
        population=sorted(population,key=lambda individual:calculate_makespan(individual,processing_times,num_machines))
        #elitism
        offspring=population[:20]
        for _ in range(80):
            parent1=random.choice(population)
            parent2 = random.choice(population)
            if random.random()<CROSSOVER_RATE:
                chlid1,child2=crossover(parent1,parent2)
                offspring.extend([mutation(chlid1,num_machines),mutation(child2,num_machines)])
        population=offspring
    best_individual = min(population, key=lambda individual:calculate_makespan(individual,processing_times,num_machines))
    return best_individual, calculate_makespan(best_individual, processing_times,num_machines)


num_machines=3
num_jobs=5
processing_time=[1,1,1,1,1]


best_individual,makespan=genetic_algorithm(POP_SIZE,1000, processing_time,num_jobs,num_machines)
print(best_individual,makespan)