import pytest


@pytest.fixture(scope='class')
def setup():
    print("This is executed first")
    yield
    print("This is executed at last")


@pytest.fixture()
def dataLoad():
    print("User profile is being created")
    return ["Aman", "Sinha", "aman.sinha@gmail.com"]

@pytest.fixture(params=[("chrome","aman", "sinha"), ("edge", "sinha"), ("firefox", "aks")])
def crossbrowser(request):
    return request.param