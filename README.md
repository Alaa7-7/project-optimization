### Optimization Algorithms Comparison
```
This project compares three simple optimization algorithms:

- Greedy Algorithm
- Random Search
- Genetic Algorithm

I use these algorithms to solve a simple resource allocation problem.

The goal is to select items with high total value while keeping the total cost within a limited budget.
```
----------------------------------------------------------------------------------------------------

## Problem
```
I have a number of items. Each item has:

- A cost
- A value

I have a limited budget, so I cannot select all items.

The budget is the maximum amount of cost that I can use.

In mathematics:

Total Cost <= Budget

In my project:

Budget = 50

This means the total cost of the selected items cannot be greater than 50.
The goal is to maximize the total value without exceeding the budget.
```
---------------------------------------------------------------------------------------------------

## Mathematical Formulation
```
I use a binary decision for each item.

x[i] = 1  ? I select the item
x[i] = 0  ? I do not select the item
```

## Total Cost
```
I calculate the total cost of the selected items:

Total Cost = cost[1] * x[1] + cost[2] * x[2] + ... + cost[n] * x[n]

In simple words, I add the cost of every selected item.
```

## Total Value

```
I calculate the total value of the selected items:

Total Value = value[1] * x[1] + value[2] * x[2] + ... + value[n] * x[n]

In simple words, I add the value of every selected item.
```

## Budget Constraint
```
The total cost must not be greater than the budget:

Total Cost <= Budget
```

## Optimization Goal

The main goal is:

Maximize Total Value

This means I try to get the highest possible value while respecting the budget.

```
Simple Example

For example:

Cost  = [10, 8, 5, 12]
Value = [20, 24, 15, 18]
Budget = 20

If I use:

solution = [1, 1, 0, 0]

I select the first and second items.

The total cost is:

Total Cost = 10*1 + 8*1 + 5*0 + 12*0
           = 18

The total value is:

Total Value = 20*1 + 24*1 + 15*0 + 18*0
            = 44

Since:

18 <= 20

The solution is feasible because the total cost is within the budget.
This means the solution follows the budget constraint and can be accepted.
```
----------------------------------------------------------------------------------------------------------


## Algorithms

# 1. Greedy Algorithm

```
I calculate the value-to-cost ratio for each item:

Ratio = Value / Cost

Then I sort the items from the highest ratio to the lowest ratio.

I select an item if adding it does not exceed the budget.

The Greedy Algorithm is simple and fast, but it does not always find the best possible solution.
```

# 2. Random Search

```
I generate random solutions.

For each solution, I calculate:

- Total Cost
- Total Value
```

If the solution is within the budget and has a better value than the previous solution, I keep it.

I repeat this process many times and return the best solution found.

# 3. Genetic Algorithm

I start with a population of random solutions.

```
Then I repeat several steps:

1. Evaluate the solutions.
2. Keep the better solutions.
3. Select two parent solutions.
4. Create a new solution using crossover.
5. Sometimes change one item using mutation.
6. Keep solutions that satisfy the budget.

After several generations, I return the best solution found.
```

-----------------------------------------------------------------------------------------------------------


```
Project Structure

project-optimization/
¦
+-- main.py
+-- README.md
+-- requirements.txt
¦
+-- src/
¦   +-- problem.py
¦   +-- greedy.py
¦   +-- random_search.py
¦   +-- genetic_algorithm.py
¦   +-- comparison.py
¦   +-- multiple_runs.py
¦
+-- tests/
    +-- test_problem.py
    +-- test_greedy.py
    +-- test_random_search.py
    +-- test_genetic_algorithm.py
```

--------------------------------------------------------------------------------------------------------------

## Files

```
"problem.py"

This file defines the optimization problem.

It creates random costs and values for the items and calculates the total cost and total value of a solution.

"greedy.py"

This file contains the Greedy Algorithm.

It selects items according to their value-to-cost ratio.

"random_search.py"

This file contains the Random Search algorithm.

It generates random solutions and keeps the best feasible solution.

"genetic_algorithm.py"

This file contains the Genetic Algorithm.

It uses a population, selection, crossover, and mutation.

"comparison.py"

This file runs the three algorithms on the same problem and compares:

- Cost
- Value
- Time

"multiple_runs.py"

This file runs the algorithms multiple times.

I use 10 runs and calculate the average cost, average value, and average running time.

"tests/"

This folder contains simple tests for the problem and the three algorithms.
```

-------------------------------------------------------------------------------------------------------


## Results

I ran the algorithms multiple times using the same problem in each run.

```
One example of the results was:

=== Multiple Runs Results ===
Runs: 10

Greedy
Average Cost: 45.7
Average Value: 141.4
Average Time: 1.5e-05

Random Search
Average Cost: 46.9
Average Value: 130.6
Average Time: 0.002356

Genetic Algorithm
Average Cost: 46.2
Average Value: 130.9
Average Time: 0.005466

The results can change slightly between runs because the problem and the algorithms use random values.

In this example, Greedy achieved the highest average value and was also the fastest algorithm.

Random Search and Genetic Algorithm had similar average values, but Genetic Algorithm took more time.
```

--------------------------------------------------------------------------------------------------------------


## Testing

```
I created four simple tests:

test_problem.py
test_greedy.py
test_random_search.py
test_genetic_algorithm.py

All four tests passed successfully.
```
-------------------------------------------------------------------------------------------------------------------


## Conclusion

In this project, I compared three optimization algorithms on a simple resource allocation problem.

The results show that a simple algorithm such as Greedy can perform very well on a small problem.

Random Search can find good solutions by trying many random possibilities.

Genetic Algorithm uses a more advanced search process with selection, crossover, and mutation, but it also needs more time.

The main purpose of this project is to understand how different optimization algorithms work and compare their results on the same problem.