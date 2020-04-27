from test_junkie.decorators import test, Suite

from organization_tut.Labels import Feature, Component, Tag


@Suite(feature=Feature.HEADER)
class Header2:

    @test(component=Component.SEARCH, tags=[Tag.CONSUMER_FEATURE, Tag.LOGGED_OUT, Tag.LOGGED_IN])
    def example_test(self):
        pass

    @test(component=Component.SEARCH, tags=[Tag.CONSUMER_FEATURE, Tag.LOGGED_OUT, Tag.LOGGED_IN])
    def example_test(self):
        pass

    @test(component=Component.SEARCH, tags=[Tag.CONSUMER_FEATURE, Tag.LOGGED_OUT, Tag.LOGGED_IN])
    def example_test(self):
        pass

    @test(component=Component.SEARCH, tags=[Tag.CONSUMER_FEATURE, Tag.LOGGED_OUT, Tag.LOGGED_IN])
    def example_test(self):
        pass

    @test(component=Component.SEARCH, tags=[Tag.CONSUMER_FEATURE, Tag.LOGGED_OUT, Tag.LOGGED_IN])
    def example_test(self):
        pass

    @test(component=Component.SEARCH, tags=[Tag.CREATOR_FEATURE, Tag.LOGGED_IN])
    def example_test(self):
        pass

    @test(component=Component.SEARCH, tags=[Tag.CREATOR_FEATURE, Tag.LOGGED_IN])
    def example_test(self):
        pass

    @test(component=Component.SEARCH, tags=[Tag.CREATOR_FEATURE, Tag.LOGGED_IN])
    def example_test(self):
        pass

    @test(component=Component.SEARCH, tags=[Tag.CREATOR_FEATURE, Tag.LOGGED_IN])
    def example_test(self):
        pass

    @test(component=Component.SEARCH, tags=[Tag.CREATOR_FEATURE, Tag.LOGGED_IN])
    def example_test(self):
        pass
