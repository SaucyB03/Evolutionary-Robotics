from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.nextAvailableID = 0

        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1



        
    def Evolve(self):
        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for key in self.parents.keys():
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for item in self.children.values():
            item.Mutate()

    def Evaluate(self, solutions):
        for p in solutions.values():
            p.Start_Simulation("DIRECT")

        for p in solutions.values():
            p.Wait_For_Simulation_To_End()

    def Select(self):
        for key in self.parents.keys():
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]

    def Show_Best(self):
        lowest_fit = 999999
        best = None
        for p in self.parents.values():
            if p.fitness < lowest_fit:
                lowest_fit = p.fitness
                best = p
        best.Start_Simulation("GUI")

    def Print(self):
        print("\n/////////////////////////////")
        print("Parents:")
        for key in self.parents.keys():
            print(self.parents[key].fitness)
        print("Children:")
        for key in self.children.keys():
            print(self.children[key].fitness)
        print("/////////////////////////////")