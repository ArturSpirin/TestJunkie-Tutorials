from test_junkie.decorators import test, Suite

from organization_tut.Labels import Feature, Component, Tag


@Suite(feature=Feature.HEADER)
class Header1:

    @test(component=Component.NAVIGATION, tags=[Tag.CONSUMER_FEATURE, Tag.LOGGED_OUT])
    def example_test(self):
        pass

    @test(component=Component.NAVIGATION, tags=[Tag.CONSUMER_FEATURE, Tag.LOGGED_OUT])
    def example_test(self):
        pass

    @test(component=Component.NAVIGATION, tags=[Tag.CONSUMER_FEATURE, Tag.LOGGED_OUT])
    def example_test(self):
        pass

    @test(component=Component.NAVIGATION, tags=[Tag.CONSUMER_FEATURE, Tag.LOGGED_OUT])
    def example_test(self):
        pass

    @test(component=Component.NAVIGATION, tags=[Tag.CONSUMER_FEATURE, Tag.LOGGED_OUT])
    def example_test(self):
        pass

    @test(component=Component.NAVIGATION, tags=[Tag.CREATOR_FEATURE, Tag.LOGGED_IN])
    def example_test(self):
        pass

    @test(component=Component.NAVIGATION, tags=[Tag.CREATOR_FEATURE, Tag.LOGGED_IN])
    def example_test(self):
        pass

    @test(component=Component.NAVIGATION, tags=[Tag.CREATOR_FEATURE, Tag.LOGGED_IN])
    def example_test(self):
        pass

    @test(component=Component.NAVIGATION, tags=[Tag.CREATOR_FEATURE, Tag.LOGGED_IN])
    def example_test(self):
        pass

    @test(component=Component.NAVIGATION, tags=[Tag.CREATOR_FEATURE, Tag.LOGGED_IN])
    def example_test(self):
        pass
