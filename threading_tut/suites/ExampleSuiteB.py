from time import sleep

from test_junkie.decorators import test, Suite


@Suite()
class ExampleSuiteB:

    @test(parameters=[1, 2, 3, 4, 5], parallelized_parameters=True)
    def example_test_1(self, parameter):
        sleep(1)

    @test()
    def example_test_2(self):
        sleep(1)

    @test()
    def example_test_3(self):
        sleep(1)

    @test()
    def example_test_4(self):
        sleep(1)

    @test()
    def example_test_5(self):
        sleep(1)
