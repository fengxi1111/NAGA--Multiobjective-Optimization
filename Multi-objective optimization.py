#Importing required modules
import math
import random
import matplotlib.pyplot as plt
 
def function1(x):
    value = -x**2
    return value
 
def function2(x):
    value = -(x-2)**2
    return value
 
#Function to find index of list
def index_of(a,list):
    for i in range(0,len(list)):
        if list[i] == a:
            return i
    return -1
 
#Function to sort by values
'''list1=[1,2,3,4,5,6,7,8,9]
   value=[1,5,6,7]
   sort_list=[1,5,6,7]
'''
def sort_by_values(list1, values):
    sorted_list = []
    while(len(sorted_list)!=len(list1)):
        if index_of(min(values),values) in list1:
            sorted_list.append(index_of(min(values),values))
        values[index_of(min(values),values)] = math.inf
    return sorted_list
 
'''
SissiFeng
1. np=0, sp=infinite
2. Perform non-dominated sorting for all individuals. If individual p dominates individual q, then add q to sp and increase q's level by one.
   If q dominates p, add p to sq and increase p's level by one.
3. Initialize the current level number k for the population, set k=1.
4. Identify individuals in the population with np=0, remove them from the population, and add them to the level set fk. This set represents individuals with level 0.
5. Check if fk is not empty. If not, decrease the level of all individuals in sp corresponding to fk by 1, and set k=k+1, then proceed to step 2.
   If fk is empty, it means all non-dominated sets have been obtained, and the program terminates.

'''
def fast_non_dominated_sort(values1, values2):
    S=[[] for i in range(0,len(values1))]
    # Initialize the sp of all individuals in the population. Here,len(value1)=pop_size
    front = [[]]
    # Stratified collection, a two-dimensional list containing individuals in the nth layer and who are present in those individuals.
    n=[0 for i in range(0,len(values1))]
    rank = [0 for i in range(0, len(values1))]
    # ranking
 
    for p in range(0,len(values1)):
        S[p]=[]
        n[p]=0
        # Search for the dominance relationship between the p-th individual and the other individuals.
        # Initialize the sp and np of the p-th individual.
        for q in range(0, len(values1)):
             #step2:p > q if p dominaces q, then
            if (values1[p] > values1[q] and values2[p] > values2[q]) or (values1[p] >= values1[q] and values2[p] > values2[q]) or (values1[p] > values1[q] and values2[p] >= values2[q]):
            # Dominance determination criteria: A condition is met if and only if, for any i belonging to {1, 2}, it holds that fi(p) > fi(q), which indicates dominance.
            # Alternatively, it is met if and only if for any i belonging to {1, 2}, fi(p) >= fi(q), and there exists at least one j such that fj(p) > fj(q), which indicates weak dominance.
                if q not in S[p]:
                    # Also, if q does not belong to sp, add it to sp.
                    S[p].append(q)
            # if q dominates p
            elif (values1[q] > values1[p] and values2[q] > values2[p]) or (values1[q] >= values1[p] and values2[q] > values2[p]) or (values1[q] > values1[p] and values2[q] >= values2[p]):
                # so np+1
                n[p] = n[p] + 1
        if n[p]==0:
            # find the individulas which np=0
            rank[p] = 0
            # remove it from pt
            if p not in front[0]:
                # if p is not in the 0th layer, add it 
                front[0].append(p)
 
    i = 0
    while(front[i] != []):
        # if sublayer set is not empty，
        Q=[]
        for p in front[i]:
            for q in S[p]:
                n[q] =n[q] - 1
                if( n[q]==0):
                    # if nq==0
                    rank[q]=i+1
 
                    if q not in Q:
                        Q.append(q)
        i = i+1
        # and k+1
        front.append(Q)
 
    del front[len(front)-1]
 
    return front
 
#Function to calculate crowding distance
'''
SissiFeng
1.I[1]=I[l]=inf，I[i]=0 sets the crowding distance of the two boundary individuals to infinity.
2.I=sort(I,m)， sorts the population based on the objective function m.
3.I[i]=I[i]+(Im[i+1]-Im[i-1])/(fmax-fmin)
'''
def crowding_distance(values1, values2, front):
    distance = [0 for i in range(0,len(front))]
    # Initialize the crowding distance between individuals
    sorted1 = sort_by_values(front, values1[:])
    sorted2 = sort_by_values(front, values2[:])
    # Sort the hierarchical populations based on objective function 1 and objective function 2
    distance[0] = 4444444444444444
    distance[len(front) - 1] = 4444444444444444
    for k in range(1,len(front)-1):
        distance[k] = distance[k]+ (values1[sorted1[k+1]] - values2[sorted1[k-1]])/(max(values1)-min(values1))
    for k in range(1,len(front)-1):
        distance[k] = distance[k]+ (values1[sorted2[k+1]] - values2[sorted2[k-1]])/(max(values2)-min(values2))
    return distance
#Return the crowding distance
 
#Function to perform crossover
def crossover(a,b):
    r=random.random()
    if r>0.5:
        return mutation((a+b)/2)
    else:
        return mutation((a-b)/2)
 
#Function performs mutation operation
def mutation(solution):
    mutation_prob = random.random()
    if mutation_prob <1:
        solution = min_x+(max_x-min_x)*random.random()
    return solution
 
pop_size = 20
max_gen = 100
#Initialization
min_x=-55
max_x=55
solution=[min_x+(max_x-min_x)*random.random() for i in range(0,pop_size)]
# randomize varibles
gen_no=0
while(gen_no<max_gen):
    function1_values = [function1(solution[i])for i in range(0,pop_size)]
    function2_values = [function2(solution[i])for i in range(0,pop_size)]
    # Generate two function value lists to form a population
    non_dominated_sorted_solution = fast_non_dominated_sort(function1_values[:],function2_values[:])
    #  Perform fast non-dominated sorting among populations to obtain a non-dominated sorted set
    print("The best front for Generation number ",gen_no, " is")
    for valuez in non_dominated_sorted_solution[0]:
        print(round(solution[valuez],3),end=" ")
    print("\n")
    crowding_distance_values=[]
    # Calculate the crowding degree of each individual in the non-dominated set
    for i in range(0,len(non_dominated_sorted_solution)):
        crowding_distance_values.append(crowding_distance(function1_values[:],function2_values[:],non_dominated_sorted_solution[i][:]))
    solution2 = solution[:]
 
    # generated offspring
    while(len(solution2)!=2*pop_size):
        a1 = random.randint(0,pop_size-1)
        b1 = random.randint(0,pop_size-1)
        # selection
        solution2.append(crossover(solution[a1],solution[b1]))
        # Randomly select and mate the individuals in the population to obtain the offspring population 2*pop_size
        
    function1_values2 = [function1(solution2[i])for i in range(0,2*pop_size)]
    function2_values2 = [function2(solution2[i])for i in range(0,2*pop_size)]
    non_dominated_sorted_solution2 = fast_non_dominated_sort(function1_values2[:],function2_values2[:])
    # Sort the two population values ​​obtained by the two objective functions to obtain the 2*pop_size solution
    crowding_distance_values2=[]
    for i in range(0,len(non_dominated_sorted_solution2)):
        crowding_distance_values2.append(crowding_distance(function1_values2[:],function2_values2[:],non_dominated_sorted_solution2[i][:]))
    # Calculate the distance value between individuals of the offspring
    new_solution= []
    for i in range(0,len(non_dominated_sorted_solution2)):
        non_dominated_sorted_solution2_1 = [index_of(non_dominated_sorted_solution2[i][j],non_dominated_sorted_solution2[i] ) for j in range(0,len(non_dominated_sorted_solution2[i]))]
        # ranking
        front22 = sort_by_values(non_dominated_sorted_solution2_1[:], crowding_distance_values2[i][:])
        front = [non_dominated_sorted_solution2[i][front22[j]] for j in range(0,len(non_dominated_sorted_solution2[i]))]
        front.reverse()
        for value in front:
            new_solution.append(value)
            if(len(new_solution)==pop_size):
                break
        if (len(new_solution) == pop_size):
            break
    solution = [solution2[i] for i in new_solution]
    gen_no = gen_no + 1
 
#Lets plot the final front now
function1 = [i * -1 for i in function1_values]
function2 = [j * -1 for j in function2_values]
plt.xlabel('Function 1', fontsize=15)
plt.ylabel('Function 2', fontsize=15)
plt.scatter(function1, function2)
plt.show()
