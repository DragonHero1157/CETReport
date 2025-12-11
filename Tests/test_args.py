from Objects import CommandLine
import pytest

@pytest.fixture
def new_Args():
    return CommandLine.Args()

def test_inFname(new_Args):
    assert new_Args.inFName
    assert "test" in new_Args.inFname

def test_outFname(new_Args):
    assert new_Args.outFName
    assert "out" in new_Args.outFName

def test_doDump(new_Args):
    assert new_Args.doDump == True

def test_noDump(new_Args):
    assert new_Args.doDump == False