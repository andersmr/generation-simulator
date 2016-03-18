import random
BLUE = 0
RED = 1

def main():
    """
    Calls functions in the program to run them at the end of the file
    """
    # Generation 0
    a = 50
    b = 50
    c = 40
    d = 60

    for k in range(13):
        print('Generation', k + 1, '\n')
        population1 = establish_population(a, b)
        population2 = establish_population(c, d)
        allelepool1 = draw_ten(population1)
        allelepool2 = draw_ten(population2)
        population1.extend(allelepool2)
        population2.extend(allelepool1)
        print('Population 1')
        a, b = draw_fifty(population1)
        print('Population 2')
        c, d = draw_fifty(population2)
        print('\n')

def establish_population(num_blue, num_red):
    population = [BLUE, ] * num_blue + [RED, ] * num_red
    return population

def draw_ten(population):
    """
    Constructs a test to draw ten individuals from a popualtion of
     50 individuals.
    """
    temppool = []
    for _ in range(20):
        temppool.append(population.pop())
    return temppool

def draw_fifty(population):
    sample = random.sample(population, 100)
    sample1 = sample[0::2]
    sample2 = sample[1::2]
    pairs = list(zip(sample1, sample2))

    print('The number of homozygous dominant individuals is',
          pairs.count((0, 0)))
    print('The number of heterozygous individuals is',
          pairs.count((0, 1)) + pairs.count((1, 0)))
    print('The number of homozygous recessive individuals is',
          pairs.count((1, 1)))

    return sample.count(BLUE), sample.count(RED)

main()
