from unittest import TestSuite
from unittest import TestLoader
from unittest import TextTestRunner
from test_12_1 import RunnerTest
from test_12_2 import TournamentTest


if __name__ == '__main__':
    test_suite = TestSuite()
    test_suite.addTest(TestLoader().loadTestsFromTestCase(RunnerTest))
    test_suite.addTest(TestLoader().loadTestsFromTestCase(TournamentTest))
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)