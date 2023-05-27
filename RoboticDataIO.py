import os
import pickle

class RoboticDataIO:
    def __init__(self, suffix):
        self.baseDir = "Populations/"
        self.numGenerations = 0
        self.suffix = suffix
        pass

    def setNumGenerations(self, numGenerations):
        self.numGenerations = numGenerations

    def savePopulation(self,robots):
        for robotIndex in range(len(robots)):
            path = self.baseDir + str(self.numGenerations) + self.suffix
            self.__createIfNotExists(path)
            file_name = path + '/robot' + str(robotIndex) + '.pkl'
            with open(file_name, 'wb') as file:
                pickle.dump(robots[robotIndex], file)
                print(f'Object successfully saved to "{file_name}"')

    def __createIfNotExists(self,path):
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)

    def saveData(self, data, name):
        dir = self.baseDir + str(self.numGenerations) + self.suffix
        path = dir + '/' + name + '.pkl'
        self.__createIfNotExists(dir)
        with open(path, 'wb') as fp:
            pickle.dump(data, fp)

    def loadPopulation(self, populationIndex):
        robots = []
        for i in range(25):
            with (open(f"{self.baseDir}{str(populationIndex)}{self.suffix}/robot"+str(i)+".pkl", "rb")) as openfile:
                while True:
                    try:
                        robots.append(pickle.load(openfile))
                    except EOFError:
                        break
        return robots

    def load_file(self,populationIndex, fileName):
        data = None
        with (open(f"{self.baseDir}{populationIndex}{self.suffix}/{fileName}.pkl", "rb")) as openfile:
            while True:
                try:
                    data = pickle.load(openfile)
                except EOFError:
                    break
        return data