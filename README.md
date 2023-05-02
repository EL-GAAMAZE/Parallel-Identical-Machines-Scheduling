# Parallel Identical Machines Scheduling Problem with Genetic Algorithm
This code provides a Python implementation of the genetic algorithm to solve the Parallel Identical Machines Scheduling Problem. The problem involves scheduling a set of jobs on parallel identical machines with the goal of minimizing the makespan, which is the time it takes to complete all jobs.
# Getting Started
To run the code, you'll need to have Python 3.x installed on your system. You can clone this repository or download the code as a ZIP file and extract it to a local directory.

# Prerequisites
Python 3.x
# Running the code
To run the code, open your terminal or command prompt and navigate to the directory where the code is saved. Then, type:


```python genetic_algorithm.py```
# Code Structure
The genetic_algorithm.py file contains the following functions:


**initialize_population(num_individuals, num_jobs,num_machines)**: Initializes a population of random individuals.


**calculate_makespan(individual, processing_times,num_machines)**: Calculates the makespan of an individual.


**crossover(parent1, parent2)**: Performs single point crossover on two parents.


**mutation(individual,num_machines)**: Mutates an individual.


**genetic_algorithm(num_individuals, num_generations, processing_times,num_jobs,num_machines)**: Implements the genetic algorithm.


*main()*: The main function that runs the genetic algorithm.

# Parameters
You can modify the following parameters in the code:


**MUTAUTION_RATE**: The probability of mutation.


**CROSSOVER_RATE**: The probability of crossover.


**GENERATIONS**: The number of generations.


**POP_SIZE**: The population size.


**NUM_MACHINES**: The number of machines.


**NUM_JOBS**: The number of jobs.


**PROCESSING_TIME**: A list of processing times for each job.
# Outputs


The code outputs the best individual and its corresponding makespan.
# License
This project is licensed under the MIT License - see the LICENSE.md file for details.
