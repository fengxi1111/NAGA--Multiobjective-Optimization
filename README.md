# NAGA--Multiobjective-Optimization

Briefly introduce the NSGA-II algorithm. First, there is a batch of individuals with multiple targets as parents. In each iteration, the parents and children are merged after the GA operation. Through non-dominated sorting (discussed in detail later), we classify all individuals into different Pareto-frontier frontier levels. Individuals are selected from the Pareto front as the next population in the order of different levels. To preserve diversity, a “crowding distance” was also calculated. Distance comparison leads the selection process at each stage of the algorithm to the consistently unfolded Pareto-most pattern front.


Let's look at the previous example. The consumption of each row shows np and Sp. np means "How many people dominate you?" Sp means "Who are you controlling? Because" A and B are not dominated by any solution, nor are they dominated by everyone, so their np = 0, Sp contains C and d. C is dominated by A and B and its np = 1. C also dominates D, so Sp contains D.


Non-dominated Sorting
Let the set of all solutions be S. Now estimate the set of non-dominated solutions, denoted as F1
Let S=S-F1, and then determine the non-dominated solution set from S, denoted as F2
Repeat the second step until S is an empty set
The non-dominated solutions for each sorting are sorted as follows:
{F1,F2,…,Fn}

Crowding Distance
To estimate the density of solutions around a particular solution in the population, the authors calculated the average distance to each target along both edges of the point. As shown in the figure below, the crowding distance of the i-th coriander at its front end (marked by a solid circle) is the average side length of the cuboid (marked by a dotted box).


Algorithm:

Initialize the crowding distance to zero for all individuals.
Review all personal and goal values. Select binding solutions by assigning them with Inf values.
Calculate the m-th maximum and minimum values ​​of each target to obtain the normalized denominator.
Sum the crowding distances of m targets for the i-th individual
The purpose of calculating the degree of crowding is to preserve solutions with low similarity and maintain the diversity of the solution space.
in conclusion
NSGA-II is an elitist MOEA based on a non-dominated ranking method. In practice, NSGA-II remains a classic method that finds a better extension of the solution and converges better near the true Pareto optimal front. This is also a good example of designing a simple yet efficient algorithm. In terms of implementation, DEAP provides a good python toolkit to perform NSGA-II.
