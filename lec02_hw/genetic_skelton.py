import random

"""Default constants"""
gene_pool = [] # Our 'genes' would be the binary number's digits.
# gene_pool would be a list of list.

GENE_SIZE = 10 # The length of our gene (0000000000~1111111111)

POPULATION = 10 # The length of our pool

MAX_GENERATION = 20 # The maximum number of times we will repeat the process

k = 4 # Number of genes selected by fitness

"""1) Initialize"""
# Fill our gene_pool with POPULATION random genes
# TODO

#Uncomment this to see our pool
# for gene in gene_pool:
    # print(*gene)

"""6) Loop MAX_GENERATION times"""
for generation in range(MAX_GENERATION):

    """2) Selection"""
    # Sort genes by fitness(the number of 1s)
    # It can be counted by sum. 
    # This code sorts gene_pool in descending order, using each gene's sum.
    # From gene pool choose top k fit genes, based on the number of 1s.
    gene_pool = sorted(gene_pool, key=lambda x: sum(x), reverse=True)
    selected_pool = gene_pool[:k]

    """3) Crossover"""
    # Our crossover strategy: slice 2 lists in half,
    # then add first half to other's second half and vice versa.
    # e.g. [1,1,1,1] and [0,0,0,0] -> [1,1,0,0], [0,0,1,1]
    # choose 2 genes from our selected_pool (POPULATION // 2) times
    # using random.choices() or random.sample()
    # and apply crossover to populate new_gene_pool
    new_gene_pool = []
    for _ in range(POPULATION//2):
        #TODO
        pass

    """"4) Mutation"""
    # From the new_gene_pool, 
    # randomly choose one gene, and reverse one of its digit
    #TODO

    """5) Replace:"""
    gene_pool = new_gene_pool


# Check our result
print(sorted(gene_pool, key=lambda x: sum(x))[-1])
