import random

# Default constants
gene_pool = [] # Our 'genes' would be the binary number's digits.
# gene_pool would be a list of list.
GENE_SIZE = 10 # The length of our gene (0000000000~1111111111)
POPULATION = 10 # The size of our pool
MAX_GENERATION = 20 # The maximum number of times we will repeat the process

# 6) Loop MAX_GENERATION times
for _ in range(POPULATION):
    gene_pool.append([random.randint(0,1) for _ in range(GENE_SIZE)])
    # TODO
    pass
for generation in range(MAX_GENERATION):

    # 1) Initialize
    # Populate our gene_pool with 10 random genes
    # Please note that random.randint(a,b) includes b.

    # 2) Selection: 
    # We will choose top 4 fit genes, based on the number of 1s.
    # The number of 1s can be counted by sum,
    # and the following code sorts our pool in descending order,
    # using each gene's sum value.
    gene_pool = sorted(gene_pool, key=lambda x: sum(x), reverse=True)
    selected_pool = gene_pool[:4]

    #Uncomment this to see our pool
    # for gene in genetic_pool:
        # print(*gene)

    # 3) Crossover:
    # Our crossover strategy: slice 2 lists in half,
    # then add first half to other's second half and vice versa.
    # e.g. [1,1,1,1] and [0,0,0,0] -> [1,1,0,0], [0,0,1,1]
    # choose 2 genes from our selected_pool (POPULATION // 2) times
    # using random.choices() or random.sample()
    # and apply crossover to populate new_gene_pool
    new_gene_pool = []
    for _ in range(POPULATION//2):
        a, b = random.sample(selected_pool, 2)
        new_gene_pool.append(a[:len(a)//2]+b[len(b)//2:])
        new_gene_pool.append(b[:len(b)//2]+a[len(a)//2:])
        #TODO
        pass

    # 4) Mutation:
    # From the new_gene_pool, 
    # randomly choose one gene, and reverse one of its digit
    #TODO
    idx = random.randint(0,len(new_gene_pool)-1)
    new_gene_pool[idx][random.randint(0, GENE_SIZE-1)] = 1

    # 5) Replace:
    gene_pool = new_gene_pool


# When the loop finishes, check our result
print(sorted(gene_pool, key=lambda x: sum(x))[-1])
