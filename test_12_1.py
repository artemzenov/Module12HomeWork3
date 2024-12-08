import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_runner = runner.Runner(name='TestName')
        for _ in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_runner = runner.Runner(name='TestName')
        for _ in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_runner1 = runner.Runner(name='TestName1')
        test_runner2 = runner.Runner(name='TestName2')
        for _ in range(10):
            test_runner1.run()
            test_runner2.walk()
        self.assertNotEqual(test_runner1.distance, test_runner2.distance)


if __name__ == '__main__':
    unittest.main()