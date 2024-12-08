from runner_and_tournament import Runner
from runner_and_tournament import Tournament
from unittest import main
from unittest import TestCase
from unittest import skipIf


class TournamentTest(TestCase):
    is_frozen = True
  
    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()
        cls.count = 0
  
    def setUp(self):
        self.runner1 = Runner(name='Усэйн', speed=10)
        self.runner2 = Runner(name='Андрей', speed=9)
        self.runner3 = Runner(name='Ник', speed=3)
        self.distance = 90
        TournamentTest.count += 1

  
    def _last_runner(self, *runners):
        self.last_runner = runners[0]
        time_runner = self.distance / runners[0].speed
        for runner in runners:
            if (self.distance / runner.speed) > time_runner:
              self.last_runner = str(runner)
  
    def _first_runner(self, *runners):
        self.first_runner = runners[0]
        time_runner = self.distance / runners[0].speed
        for runner in runners:
            if (self.distance / runner.speed) < time_runner:
                self.first_runner = str(runner)
  
    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament1(self):
        self.list_runners = [self.runner1, self.runner3]

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        self.list_runners = [self.runner2, self.runner3]

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament3(self):
        self.list_runners = [self.runner1, self.runner2, self.runner3]
  
    def tearDown(self):
        self.tournament = Tournament(self.distance, *self.list_runners)
        self.result_tournament = self.tournament.start()
        TournamentTest.all_results[TournamentTest.count] = self.result_tournament
        self._last_runner(*self.list_runners)
        self._first_runner(*self.list_runners)
        self.assertTrue(self.result_tournament[max(self.result_tournament)] == self.last_runner)
        self.assertTrue(self.result_tournament[min(self.result_tournament)] == self.first_runner)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)


if __name__ == '__main__':
    main()