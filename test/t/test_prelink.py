import pytest


class Test(object):

    @pytest.mark.complete("prelink ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("prelink -")
    def test_dash(self, completion):
        assert completion.list