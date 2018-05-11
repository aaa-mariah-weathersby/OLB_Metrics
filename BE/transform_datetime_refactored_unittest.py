import unittest
import datetime
import transform_datetime_refactored as transform_datetime

"""
to run:

    python transform_datetime_refactored_unittest.py

"""

class TestQuoteTransform(unittest.TestCase):

    def test_open_filehandles(self):
        quotetransform = transform_datetime.QuoteTransform()
        self.assertIsNone(quotetransform.input_file)
        self.assertIsNone(quotetransform.output_file)
        quotetransform.open_filehandles()
        self.assertIsNotNone(quotetransform.input_file)
        self.assertIsNotNone(quotetransform.output_file)

    def test_close_filehandles(self):
        quotetransform = transform_datetime.QuoteTransform()
        quotetransform.open_filehandles()
        quotetransform.close_filehandles()
        self.assertIsNone(quotetransform.input_file)
        self.assertIsNone(quotetransform.output_file)

    def test_construct_header(self):
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(quotetransform.construct_header(), "QuoteID CreateDate\n")

    def test_remove_plus_symbol_positive_short(self):
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(quotetransform.remove_plus_symbol("\x00+999500000"), "999500000")
        self.assertEqual(quotetransform.remove_plus_symbol("\x00\x2b999500000"), "999500000")
    def test_remove_plus_symbol_positive_long(self):
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(
            quotetransform.remove_plus_symbol("\x00+999500000 2017-01-10-09.10.47.461118 2017-01-10-09.34.53.077890 RM 01/10/2017"),
            "999500000 2017-01-10-09.10.47.461118 2017-01-10-09.34.53.077890 RM 01/10/2017"
        )
        self.assertEqual(
            quotetransform.remove_plus_symbol("\x00\x2b999500000 2017-01-10-09.10.47.461118 2017-01-10-09.34.53.077890 RM 01/10/2017"),
            "999500000 2017-01-10-09.10.47.461118 2017-01-10-09.34.53.077890 RM 01/10/2017"
        )

    def test_remove_plus_symbol_negative_short(self):
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(quotetransform.remove_plus_symbol("999500000"), "999500000")
    def test_remove_plus_symbol_negative_long(self):
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(
            quotetransform.remove_plus_symbol("999500000 2017-01-10-09.10.47.461118 2017-01-10-09.34.53.077890 RM 01/10/2017"),
            "999500000 2017-01-10-09.10.47.461118 2017-01-10-09.34.53.077890 RM 01/10/2017"
        )

    def test_process_quoteid_positive(self):
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(quotetransform.remove_plus_symbol("\x00+999500000"), "999500000")
        self.assertEqual(quotetransform.remove_plus_symbol("\x00\x2b999500000"), "999500000")

    def test_process_quoteid_negative(self):
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(quotetransform.remove_plus_symbol("999500000"), "999500000")

    def test_split_datum_positive(self):
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(quotetransform.split_datum("\x00\x2b999500000 2017-01-10-09.10.47.461118 2017-01-10-09.34.53.077890 RM 01/10/2017"),
            ['\x00+999500000', '2017-01-10-09.10.47.461118', '2017-01-10-09.34.53.077890', 'RM', '01/10/2017']
        )
        self.assertEqual(quotetransform.split_datum("\x00+999500022 2017-01-10-12.08.25.728764 2017-01-11-13.21.39.253151 D  01/11/2017"),
            ['\x00+999500022', '2017-01-10-12.08.25.728764', '2017-01-11-13.21.39.253151', 'D', '', '01/11/2017']
        )
    def test_process_datein_to_dtime(self):
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(quotetransform.process_datein_to_dtime('2017-01-10-12.08.25.728764'), datetime.datetime(2017, 1, 10))

    def test_process_dtime_to_formatteddtime(self):
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(quotetransform.process_dtime_to_formatteddtime(datetime.datetime(2017, 1, 10)), '01/10/2017')

    def test_process_createdate(self):
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(quotetransform.process_createdate('2017-01-10-12.08.25.728764'), '01/10/2017')

    def test_process_datum(self):
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(
                quotetransform.process_datum("\x00\x2b999500000 2017-01-10-09.10.47.461118 2017-01-10-09.34.53.077890 RM 01/10/2017"),
                "999500000 01/10/2017\n"
                )
        self.assertEqual(
                quotetransform.process_datum("\x00+999500022 2017-01-10-12.08.25.728764 2017-01-11-13.21.39.253151 D  01/11/2017"),
                "999500022 01/10/2017\n"
                )

    def test_join_datum(self):
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(
                quotetransform.join_datum('999500022', '01/10/2017'),
                "999500022 01/10/2017\n"
        )

if __name__ == '__main__':
    from pylint.lint import Run
    from pylint.reporters.text import TextReporter
    Run(['transform_datetime_refactored.py'], exit=False)
    unittest.main()
