# Copyright (c) 2010-2022 openpyxl

from openpyxl.tests.helper import compare_xml

from openpyxl.xml.functions import tostring


def test_related():
    from openpyxl.worksheet.related import Related
    rel = Related(id="rId1")
    expected = """
    <drawing xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:id="rId1"/>
    """
    xml = tostring(rel.to_tree("drawing"))
    diff = compare_xml(xml, expected)
    assert diff is None, diff
