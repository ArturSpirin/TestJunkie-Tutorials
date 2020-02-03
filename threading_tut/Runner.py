from test_junkie.runner import Runner

from threading_tut.suites.ExampleSuiteA import ExampleSuiteA
from threading_tut.suites.ExampleSuiteB import ExampleSuiteB

runner = Runner(suites=[ExampleSuiteA, ExampleSuiteB])
runner.run(suite_multithreading_limit=2,
           test_multithreading_limit=10)
