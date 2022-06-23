# Copyright (c) 2010-2022 openpyxl

import pytest

def test_interface():
    from openpyxl.packaging.interface import ISerialisableFile

    class DummyFile(ISerialisableFile):

        pass

    with pytest.raises(TypeError):

        df = DummyFile()
