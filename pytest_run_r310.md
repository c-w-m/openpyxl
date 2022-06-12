============================= test session starts ==============================
platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0
rootdir: /workspaces/openpyxl, configfile: pytest.ini
plugins: anyio-3.6.1
collected 2430 items

openpyxl/cell/tests/test_cell.py ..................................x.... [  1%]
....................                                                     [  2%]
openpyxl/cell/tests/test_read_only.py .........                          [  2%]
openpyxl/cell/tests/test_text.py ............                            [  3%]
openpyxl/cell/tests/test_writer.py ..................................... [  4%]
..............                                                           [  5%]
openpyxl/chart/tests/test_3d.py ....                                     [  5%]
openpyxl/chart/tests/test_area_chart.py .....                            [  5%]
openpyxl/chart/tests/test_axis.py .................                      [  6%]
openpyxl/chart/tests/test_bar_chart.py ......                            [  6%]
openpyxl/chart/tests/test_bubble_chart.py ..                             [  6%]
openpyxl/chart/tests/test_chart.py ...............                       [  7%]
openpyxl/chart/tests/test_chartspace.py ........                         [  7%]
openpyxl/chart/tests/test_data_source.py ..................              [  8%]
openpyxl/chart/tests/test_error_bar.py ..                                [  8%]
openpyxl/chart/tests/test_label.py ....                                  [  8%]
openpyxl/chart/tests/test_layout.py ...                                  [  8%]
openpyxl/chart/tests/test_legend.py ....                                 [  9%]
openpyxl/chart/tests/test_line_chart.py .....                            [  9%]
openpyxl/chart/tests/test_marker.py ....                                 [  9%]
openpyxl/chart/tests/test_picture.py ..                                  [  9%]
openpyxl/chart/tests/test_pie_chart.py .........                         [  9%]
openpyxl/chart/tests/test_pivot.py ....                                  [ 10%]
openpyxl/chart/tests/test_plotarea.py ............                       [ 10%]
openpyxl/chart/tests/test_print.py ....                                  [ 10%]
openpyxl/chart/tests/test_radar_chart.py ..                              [ 10%]
openpyxl/chart/tests/test_reader.py ..                                   [ 10%]
openpyxl/chart/tests/test_reference.py ..........                        [ 11%]
openpyxl/chart/tests/test_scatter_chart.py ..                            [ 11%]
openpyxl/chart/tests/test_series.py .........                            [ 11%]
openpyxl/chart/tests/test_series_factory.py .......                      [ 11%]
openpyxl/chart/tests/test_shapes.py ..                                   [ 12%]
openpyxl/chart/tests/test_stock_chart.py ..                              [ 12%]
openpyxl/chart/tests/test_surface_chart.py ........                      [ 12%]
openpyxl/chart/tests/test_text.py .....                                  [ 12%]
openpyxl/chart/tests/test_title.py ...                                   [ 12%]
openpyxl/chart/tests/test_trendline.py ....                              [ 12%]
openpyxl/chart/tests/test_updown_bars.py ..                              [ 13%]
openpyxl/chartsheet/tests/test_chartsheet.py ....                        [ 13%]
openpyxl/chartsheet/tests/test_custom.py ....                            [ 13%]
openpyxl/chartsheet/tests/test_properties.py ..                          [ 13%]
openpyxl/chartsheet/tests/test_protection.py ...                         [ 13%]
openpyxl/chartsheet/tests/test_publish.py ....                           [ 13%]
openpyxl/chartsheet/tests/test_relation.py ....                          [ 13%]
openpyxl/chartsheet/tests/test_views.py ....                             [ 14%]
openpyxl/comments/tests/test_author.py ..                                [ 14%]
openpyxl/comments/tests/test_comment.py ....                             [ 14%]
openpyxl/comments/tests/test_comment_reader.py ...                       [ 14%]
openpyxl/comments/tests/test_comment_sheet.py ......                     [ 14%]
openpyxl/comments/tests/test_shape_writer.py ....                        [ 14%]
openpyxl/compat/tests/test_compat.py ........s.....                      [ 15%]
openpyxl/descriptors/tests/test_base.py ................................ [ 16%]
................                                                         [ 17%]
openpyxl/descriptors/tests/test_excel.py ............................... [ 18%]
.                                                                        [ 18%]
openpyxl/descriptors/tests/test_namespace.py ...                         [ 18%]
openpyxl/descriptors/tests/test_nested.py .........................      [ 19%]
openpyxl/descriptors/tests/test_sequence.py ...................          [ 20%]
openpyxl/descriptors/tests/test_serialisable.py ...............          [ 21%]
openpyxl/drawing/tests/test_color.py ............                        [ 21%]
openpyxl/drawing/tests/test_connector.py x.                              [ 21%]
openpyxl/drawing/tests/test_descriptors.py .                             [ 21%]
openpyxl/drawing/tests/test_drawing.py .........                         [ 22%]
openpyxl/drawing/tests/test_effect.py ......                             [ 22%]
openpyxl/drawing/tests/test_fill.py .................                    [ 23%]
openpyxl/drawing/tests/test_geometry.py ................                 [ 23%]
openpyxl/drawing/tests/test_graphic.py ...........xx..                   [ 24%]
openpyxl/drawing/tests/test_image.py F.....                              [ 24%]
openpyxl/drawing/tests/test_line.py .......                              [ 24%]
openpyxl/drawing/tests/test_picture.py ........                          [ 25%]
openpyxl/drawing/tests/test_properties.py ..........                     [ 25%]
openpyxl/drawing/tests/test_relation.py ..                               [ 25%]
openpyxl/drawing/tests/test_spreadsheet_drawing.py ..................... [ 26%]
.....                                                                    [ 26%]
openpyxl/drawing/tests/test_text.py ..............                       [ 27%]
openpyxl/formatting/tests/test_formatting.py .......                     [ 27%]
openpyxl/formatting/tests/test_rule.py ................................  [ 29%]
openpyxl/formula/tests/test_tokenizer.py ............................... [ 30%]
........................................................................ [ 33%]
........................................................................ [ 36%]
...................                                                      [ 37%]
openpyxl/formula/tests/test_translate.py ............................... [ 38%]
........................................................................ [ 41%]
..................                                                       [ 42%]
openpyxl/packaging/tests/test_core.py .......                            [ 42%]
openpyxl/packaging/tests/test_extended.py ..                             [ 42%]
openpyxl/packaging/tests/test_interface.py .                             [ 42%]
openpyxl/packaging/tests/test_manifest.py ....................           [ 43%]
openpyxl/packaging/tests/test_pivot.py ..                                [ 43%]
openpyxl/packaging/tests/test_relationship.py ......                     [ 43%]
openpyxl/packaging/tests/test_workbook.py ...                            [ 43%]
openpyxl/pivot/tests/test_cache.py ..........................            [ 44%]
openpyxl/pivot/tests/test_fields.py ..............                       [ 45%]
openpyxl/pivot/tests/test_record.py .....                                [ 45%]
openpyxl/pivot/tests/test_table.py ..............................        [ 46%]
openpyxl/reader/tests/test_drawings.py ....                              [ 46%]
openpyxl/reader/tests/test_excel.py ...............................      [ 48%]
openpyxl/reader/tests/test_strings.py ...                                [ 48%]
openpyxl/reader/tests/test_workbook.py .........                         [ 48%]
openpyxl/styles/tests/test_alignments.py ...                             [ 48%]
openpyxl/styles/tests/test_borders.py ..                                 [ 48%]
openpyxl/styles/tests/test_cell_style.py ..........                      [ 49%]
openpyxl/styles/tests/test_colors.py ..................                  [ 50%]
openpyxl/styles/tests/test_differential.py ....                          [ 50%]
openpyxl/styles/tests/test_fills.py .............................        [ 51%]
openpyxl/styles/tests/test_fonts.py ....                                 [ 51%]
openpyxl/styles/tests/test_named_style.py ........................       [ 52%]
openpyxl/styles/tests/test_number_style.py ............................. [ 53%]
................................................                         [ 55%]
openpyxl/styles/tests/test_protection.py ..                              [ 55%]
openpyxl/styles/tests/test_proxy.py .....                                [ 56%]
openpyxl/styles/tests/test_styleable.py ..........                       [ 56%]
openpyxl/styles/tests/test_stylesheet.py ....................            [ 57%]
openpyxl/styles/tests/test_table.py ......                               [ 57%]
openpyxl/tests/test_backend.py ..                                        [ 57%]
openpyxl/tests/test_iter.py ............................................ [ 59%]
.......                                                                  [ 59%]
openpyxl/tests/test_read.py ......                                       [ 59%]
openpyxl/tests/test_vba.py .....                                         [ 60%]
openpyxl/utils/tests/test_bound_dictionary.py ...                        [ 60%]
openpyxl/utils/tests/test_cell.py ...................................... [ 61%]
...............................                                          [ 63%]
openpyxl/utils/tests/test_dataframe.py ......                            [ 63%]
openpyxl/utils/tests/test_datetime.py .................................. [ 64%]
..............................................................           [ 67%]
openpyxl/utils/tests/test_escape.py ..                                   [ 67%]
openpyxl/utils/tests/test_indexed_list.py ......                         [ 67%]
openpyxl/utils/tests/test_inference.py ..................                [ 68%]
openpyxl/utils/tests/test_protection.py .                                [ 68%]
openpyxl/utils/tests/test_units.py ..................................... [ 69%]
....................................                                     [ 71%]
openpyxl/workbook/external_link/tests/test_external.py .........         [ 71%]
openpyxl/workbook/tests/test_child.py .....................              [ 72%]
openpyxl/workbook/tests/test_defined_name.py ........................... [ 73%]
..............................                                           [ 75%]
openpyxl/workbook/tests/test_external_reference.py ..                    [ 75%]
openpyxl/workbook/tests/test_function_group.py ....                      [ 75%]
openpyxl/workbook/tests/test_properties.py ......                        [ 75%]
openpyxl/workbook/tests/test_protection.py .....                         [ 75%]
openpyxl/workbook/tests/test_smart_tags.py ......                        [ 75%]
openpyxl/workbook/tests/test_views.py ....                               [ 76%]
openpyxl/workbook/tests/test_web.py ......                               [ 76%]
openpyxl/workbook/tests/test_workbook.py ...........x................... [ 77%]
...............                                                          [ 78%]
openpyxl/workbook/tests/test_writer.py ............                      [ 78%]
openpyxl/worksheet/tests/test_cell_range.py ............................ [ 79%]
...............................                                          [ 81%]
openpyxl/worksheet/tests/test_controls.py ..                             [ 81%]
openpyxl/worksheet/tests/test_datavalidation.py ...................      [ 82%]
openpyxl/worksheet/tests/test_dimensions.py ........................     [ 83%]
openpyxl/worksheet/tests/test_filters.py .............................   [ 84%]
openpyxl/worksheet/tests/test_header.py ..................               [ 84%]
openpyxl/worksheet/tests/test_hyperlink.py .....                         [ 85%]
openpyxl/worksheet/tests/test_merge.py ...............                   [ 85%]
openpyxl/worksheet/tests/test_ole.py ..                                  [ 85%]
openpyxl/worksheet/tests/test_page.py ........                           [ 86%]
openpyxl/worksheet/tests/test_pagebreak.py .....                         [ 86%]
openpyxl/worksheet/tests/test_properties.py ...                          [ 86%]
openpyxl/worksheet/tests/test_protection.py ......                       [ 86%]
openpyxl/worksheet/tests/test_read_only.py ...................           [ 87%]
openpyxl/worksheet/tests/test_reader.py ................................ [ 88%]
.......................................                                  [ 90%]
openpyxl/worksheet/tests/test_related.py .                               [ 90%]
openpyxl/worksheet/tests/test_scenario.py ......                         [ 90%]
openpyxl/worksheet/tests/test_table.py ......................            [ 91%]
openpyxl/worksheet/tests/test_views.py ......                            [ 91%]
openpyxl/worksheet/tests/test_worksheet.py ............................. [ 93%]
......................................................................   [ 96%]
openpyxl/worksheet/tests/test_worksheet_copy.py ...............          [ 96%]
openpyxl/worksheet/tests/test_write_only.py ..........                   [ 97%]
openpyxl/worksheet/tests/test_writer.py ................................ [ 98%]
.                                                                        [ 98%]
openpyxl/writer/tests/test_excel.py ............                         [ 98%]
openpyxl/writer/tests/test_template.py ................                  [ 99%]
openpyxl/xml/tests/test_functions.py ..FFFF....

=================================== FAILURES ===================================
____________________________ TestImage.test_import _____________________________

self = <openpyxl.drawing.tests.test_image.TestImage object at 0x7f9c60b13c40>
Image = <class 'openpyxl.drawing.image.Image'>
datadir = local('/workspaces/openpyxl/openpyxl/drawing/tests/data')

    @pytest.mark.pil_not_installed
    def test_import(self, Image, datadir):
        from ..image import _import_image
        datadir.chdir()
>       with pytest.raises(ImportError):
E       Failed: DID NOT RAISE <class 'ImportError'>

Image      = <class 'openpyxl.drawing.image.Image'>
_import_image = <function _import_image at 0x7f9c61765630>
datadir    = local('/workspaces/openpyxl/openpyxl/drawing/tests/data')
self       = <openpyxl.drawing.tests.test_image.TestImage object at 0x7f9c60b13c40>

/workspaces/openpyxl/openpyxl/drawing/tests/test_image.py:17: Failed
----------------------------- Captured stderr call -----------------------------
/workspaces/openpyxl/openpyxl/drawing/tests/test_image.py:18: ResourceWarning: unclosed file <_io.BufferedReader name='plain.png'>
  _import_image("plain.png")
ResourceWarning: Enable tracemalloc to get the object allocation traceback
_ test_fromstring[<?xml version="1.0" encoding="ISO-8859-1"?>\n            <!DOCTYPE foo [\n            <!ELEMENT foo ANY >\n            <!ENTITY xxe SYSTEM "file:///dev/random" >]>\n            <foo>&xxe;</foo>] _

xml_input = b'<?xml version="1.0" encoding="ISO-8859-1"?>\n            <!DOCTYPE foo [\n            <!ELEMENT foo ANY >\n            <!ENTITY xxe SYSTEM "file:///dev/random" >]>\n            <foo>&xxe;</foo>'

    @pytest.mark.defusedxml_required
    @pytest.mark.parametrize("xml_input", vulnerable_xml_strings)
    def test_fromstring(xml_input):
        from defusedxml.common import DefusedXmlException
>       with pytest.raises(DefusedXmlException):
E       Failed: DID NOT RAISE <class 'defusedxml.common.DefusedXmlException'>

DefusedXmlException = <class 'defusedxml.common.DefusedXmlException'>
xml_input  = b'<?xml version="1.0" encoding="ISO-8859-1"?>\n            <!DOCTYPE foo [\n            <!ELEMENT foo ANY >\n            <!ENTITY xxe SYSTEM "file:///dev/random" >]>\n            <foo>&xxe;</foo>'

/workspaces/openpyxl/openpyxl/xml/tests/test_functions.py:54: Failed
_ test_fromstring[<?xml version="1.0" encoding="UTF-8"?>\n          <!DOCTYPE xmlbomb [\n          <!ENTITY a "1234567890" >\n          <!ENTITY b "&a;&a;&a;&a;&a;&a;&a;&a;">\n          <!ENTITY c "&b;&b;&b;&b;&b;&b;&b;&b;">\n          <!ENTITY d "&c;&c;&c;&c;&c;&c;&c;&c;">\n          ]>\n          <foo>&d;</foo>] _

xml_input = b'<?xml version="1.0" encoding="UTF-8"?>\n          <!DOCTYPE xmlbomb [\n          <!ENTITY a "1234567890" >\n        ... "&b;&b;&b;&b;&b;&b;&b;&b;">\n          <!ENTITY d "&c;&c;&c;&c;&c;&c;&c;&c;">\n          ]>\n          <foo>&d;</foo>'

    @pytest.mark.defusedxml_required
    @pytest.mark.parametrize("xml_input", vulnerable_xml_strings)
    def test_fromstring(xml_input):
        from defusedxml.common import DefusedXmlException
        with pytest.raises(DefusedXmlException):
>           fromstring(xml_input)

DefusedXmlException = <class 'defusedxml.common.DefusedXmlException'>
xml_input  = b'<?xml version="1.0" encoding="UTF-8"?>\n          <!DOCTYPE xmlbomb [\n          <!ENTITY a "1234567890" >\n        ... "&b;&b;&b;&b;&b;&b;&b;&b;">\n          <!ENTITY d "&c;&c;&c;&c;&c;&c;&c;&c;">\n          ]>\n          <foo>&d;</foo>'

/workspaces/openpyxl/openpyxl/xml/tests/test_functions.py:55: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
src/lxml/etree.pyx:3254: in lxml.etree.fromstring
    ???
src/lxml/parser.pxi:1913: in lxml.etree._parseMemoryDocument
    ???
src/lxml/parser.pxi:1800: in lxml.etree._parseDoc
    ???
src/lxml/parser.pxi:1141: in lxml.etree._BaseParser._parseDoc
    ???
src/lxml/parser.pxi:615: in lxml.etree._ParserContext._handleParseResultDoc
    ???
src/lxml/parser.pxi:725: in lxml.etree._handleParseResult
    ???
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

>   ???
E     File "<string>", line 1
E   lxml.etree.XMLSyntaxError: Detected an entity reference loop, line 1, column 4


src/lxml/parser.pxi:654: XMLSyntaxError
_ test_fromstring[<?xml version="1.0" encoding="UTF-8"?>\n          <!DOCTYPE test [\n          <!ENTITY % one SYSTEM "http://127.0.0.1:8100/x.xml" >\n          %one;\n          ]>] _

xml_input = b'<?xml version="1.0" encoding="UTF-8"?>\n          <!DOCTYPE test [\n          <!ENTITY % one SYSTEM "http://127.0.0.1:8100/x.xml" >\n          %one;\n          ]>'

    @pytest.mark.defusedxml_required
    @pytest.mark.parametrize("xml_input", vulnerable_xml_strings)
    def test_fromstring(xml_input):
        from defusedxml.common import DefusedXmlException
        with pytest.raises(DefusedXmlException):
>           fromstring(xml_input)

DefusedXmlException = <class 'defusedxml.common.DefusedXmlException'>
xml_input  = b'<?xml version="1.0" encoding="UTF-8"?>\n          <!DOCTYPE test [\n          <!ENTITY % one SYSTEM "http://127.0.0.1:8100/x.xml" >\n          %one;\n          ]>'

/workspaces/openpyxl/openpyxl/xml/tests/test_functions.py:55: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
src/lxml/etree.pyx:3254: in lxml.etree.fromstring
    ???
src/lxml/parser.pxi:1913: in lxml.etree._parseMemoryDocument
    ???
src/lxml/parser.pxi:1800: in lxml.etree._parseDoc
    ???
src/lxml/parser.pxi:1141: in lxml.etree._BaseParser._parseDoc
    ???
src/lxml/parser.pxi:615: in lxml.etree._ParserContext._handleParseResultDoc
    ???
src/lxml/parser.pxi:725: in lxml.etree._handleParseResult
    ???
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

>   ???
E     File "<string>", line 5
E   lxml.etree.XMLSyntaxError: Start tag expected, '<' not found, line 5, column 13


src/lxml/parser.pxi:654: XMLSyntaxError
_ test_fromstring[<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n        <!DOCTYPE bomb [\n        <!ENTITY a "{loads_of_bs}">\n        ]>\n        <foo>&a;&a;&a;</foo>] _

xml_input = b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n        <!DOCTYPE bomb [\n        <!ENTITY a "{loads_of_bs}">\n        ]>\n        <foo>&a;&a;&a;</foo>'

    @pytest.mark.defusedxml_required
    @pytest.mark.parametrize("xml_input", vulnerable_xml_strings)
    def test_fromstring(xml_input):
        from defusedxml.common import DefusedXmlException
>       with pytest.raises(DefusedXmlException):
E       Failed: DID NOT RAISE <class 'defusedxml.common.DefusedXmlException'>

DefusedXmlException = <class 'defusedxml.common.DefusedXmlException'>
xml_input  = b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n        <!DOCTYPE bomb [\n        <!ENTITY a "{loads_of_bs}">\n        ]>\n        <foo>&a;&a;&a;</foo>'

/workspaces/openpyxl/openpyxl/xml/tests/test_functions.py:54: Failed
=========================== short test summary info ============================
FAILED openpyxl/drawing/tests/test_image.py::TestImage::test_import - Failed:...
FAILED openpyxl/xml/tests/test_functions.py::test_fromstring[<?xml version="1.0" encoding="ISO-8859-1"?>\n            <!DOCTYPE foo [\n            <!ELEMENT foo ANY >\n            <!ENTITY xxe SYSTEM "file:///dev/random" >]>\n            <foo>&xxe;</foo>]
FAILED openpyxl/xml/tests/test_functions.py::test_fromstring[<?xml version="1.0" encoding="UTF-8"?>\n          <!DOCTYPE xmlbomb [\n          <!ENTITY a "1234567890" >\n          <!ENTITY b "&a;&a;&a;&a;&a;&a;&a;&a;">\n          <!ENTITY c "&b;&b;&b;&b;&b;&b;&b;&b;">\n          <!ENTITY d "&c;&c;&c;&c;&c;&c;&c;&c;">\n          ]>\n          <foo>&d;</foo>]
FAILED openpyxl/xml/tests/test_functions.py::test_fromstring[<?xml version="1.0" encoding="UTF-8"?>\n          <!DOCTYPE test [\n          <!ENTITY % one SYSTEM "http://127.0.0.1:8100/x.xml" >\n          %one;\n          ]>]
FAILED openpyxl/xml/tests/test_functions.py::test_fromstring[<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n        <!DOCTYPE bomb [\n        <!ENTITY a "{loads_of_bs}">\n        ]>\n        <foo>&a;&a;&a;</foo>]
============ 5 failed, 2419 passed, 1 skipped, 5 xfailed in 27.36s =============
