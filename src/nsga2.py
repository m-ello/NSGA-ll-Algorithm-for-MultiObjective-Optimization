#################################
# PROBLEMA : CLADIRE INALTA     #
#################################
population_size = 100
generations = 200
mutation_prob = 0.1

BOUNDS = np.array([
    [20,60],        # w - latimea cladirii
    [60,300],       # h - inaltimea cladirii
    [0.2,1.0],      # t - grossimea peretilor
])

# din mai multe surse:
density = 2400      # kg/m3 densitatea betonului
cost = 135          # $/m3

def evaluate(indidivual):
    w,h,t = individual
    volume = w*h*t
    mass = volume * density
    cost_total = volume * cost
    
    return (cost,mass)

#####################
# NSGA-II funcs     #
#####################

def dominates(x,y):
    return all(a<=b for a,b in zip(x,y)) and any(a < b for a,b in zip(x,y))


def tournament_selection(population, fitness):
    i,j = random.sample(range(len(population)), 2)
    if dominates(fitness[i], fitness[j]):
        return population[i]
    if dominates(fitness[j], fitness[i]):
        return population[j]
    return population[i] if random.random()<0.5 else population[j]
    
    
def crossover(parent1, parent2):

def mutation():

#####################
# MAIN              #
#####################
for i in range(population_size)   
    population[i] = np.array([random.uniform(*BOUNDS[j])for j in range(3)])
    
for _ in range(GENERATIONS):
    fitness = [evaluate(individual) for individual in population]
    offspring = []
    
    while len(offspring)<population_size:
        parent1 = tournament_selection(population,fitness)
        parent2 = tournament_selection(population,fitness)
        child1, child2 = crossover(parent1, parent2)
        offspring.append(mutation(child1))
        offspring.append(mutation(child2))
        
    
