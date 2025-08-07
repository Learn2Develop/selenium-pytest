import pytest

@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_data(self, dataLoad):
        print(dataLoad[0])