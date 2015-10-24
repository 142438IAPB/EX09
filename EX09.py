"""EX09."""
from MockService import MockService
import random


class MonteCarloSimulation(object):

    """This is a a template for a Monte Carlo simulation."""

    def __init__(self, service):
        """
        Constructor for the simulation.

        Arguments:
            Input service
        Returns:
            Output service
        """
        self.service = service
        pass

    def get_area(self):
        """
        Monte Carlo simulation.

        Return:
        Dictionary where first part is number of the shape
        and second  number is the area.
        """
        width = self.service.get_width()
        height = self.service.get_height()
        dict_answer = {}

        h = [0, 0, 0]
        n = [0, 0, 0]

        area = width * height

        for one_two_or_three in range(1, 4):
            for i in range(10000):

                rand_width = random.randint(0, width - 1)
                rand_height = random. randint(0, height - 1)
                if int(self.service.info(rand_width, rand_height)
                       ) == one_two_or_three:
                    h[one_two_or_three - 1] += 1
                n[one_two_or_three - 1] += 1

        for i in range(0, 3):
            if h[i] != 0:
                dict_answer[len(dict_answer)] = ((h[i] * area) / n[i])

        return dict_answer
  
  if __name__ == "__main__":
    
    service1 = MockService('circle_10.txt')
    service2 = MockService('circle_100.txt')
    service3 = MockService('circle_20.txt')
    service4 = MockService('circle_200.txt')
    service5 = MockService('squares.txt')

    sim1 = MonteCarloSimulation(service1)
    sim2 = MonteCarloSimulation(service2)
    sim3 = MonteCarloSimulation(service3)
    sim4 = MonteCarloSimulation(service4)
    sim5 = MonteCarloSimulation(service5)

    print(sim1.get_area())
    print(sim2.get_area())
    print(sim3.get_area())
    print(sim4.get_area())
    print(sim5.get_area())
