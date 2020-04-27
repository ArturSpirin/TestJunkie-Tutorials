from test_junkie.runner import Runner

from organization_tut.Header1 import Header1
from organization_tut.Header2 import Header2
from organization_tut.Labels import Feature, Component, Tag

runner = Runner(suites=[Header1, Header2])
runner.run(features=[Feature.HEADER],
           components=[Component.SEARCH],
           tag_config={"run_on_match_any": [Tag.LOGGED_OUT, Tag.LOGGED_IN]})
