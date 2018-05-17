# -*- coding: utf-8 -*-
"""Usage:
    python transform_datetime_refactored_unittest.py

"""

import unittest
import datetime
import transform_datetime_refactored as transform_datetime


class TestQuoteTransform(unittest.TestCase):
    """TestQuoteTransform"""

    def test_open_filehandles(self):
        """test - open_filehandles()"""
        quotetransform = transform_datetime.QuoteTransform()
        self.assertIsNone(quotetransform.input_file)
        self.assertIsNone(quotetransform.output_file)
        quotetransform.open_filehandles()
        self.assertIsNotNone(quotetransform.input_file)
        self.assertIsNotNone(quotetransform.output_file)

    def test_close_filehandles(self):
        """test - close_filehandles()"""
        quotetransform = transform_datetime.QuoteTransform()
        quotetransform.open_filehandles()
        quotetransform.close_filehandles()
        self.assertIsNone(quotetransform.input_file)
        self.assertIsNone(quotetransform.output_file)

    def test_construct_header(self):
        """test - construct_header()"""
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(quotetransform.construct_header(), "QuoteID CreateDate\n")

    def test_remove_plus_symbol(self):
        """test - remove_plus_symbol()
        tests for positive and negative, on short and long strings
        """
        quotetransform = transform_datetime.QuoteTransform()

        # test - remove_plus_symbol - positive test case on short string
        self.assertEqual(quotetransform.remove_plus_symbol("\x00+999500000"), "999500000")
        self.assertEqual(quotetransform.remove_plus_symbol("\x00\x2b999500000"), "999500000")

        # test - remove_plus_symbol - positive test case on long string
        self.assertEqual(
            quotetransform.remove_plus_symbol(
                "\x00+999500000 "
                "2017-01-10-09.10.47.461118 2017-01-10-09.34.53.077890 "
                "RM 01/10/2017"),
            "999500000 "
            "2017-01-10-09.10.47.461118 2017-01-10-09.34.53.077890 "
            "RM 01/10/2017"
        )
        self.assertEqual(
            quotetransform.remove_plus_symbol(
                "\x00\x2b999500000 "
                "2017-01-10-09.10.47.461118 2017-01-10-09.34.53.077890 "
                "RM 01/10/2017"),
            "999500000 "
            "2017-01-10-09.10.47.461118 2017-01-10-09.34.53.077890 "
            "RM 01/10/2017"
        )

        # test - remove_plus_symbol - negative test case on short string
        self.assertEqual(quotetransform.remove_plus_symbol("999500000"), "999500000")

        # test - remove_plus_symbol - negative test case on long string
        self.assertEqual(
            quotetransform.remove_plus_symbol(
                "999500000 "
                "2017-01-10-09.10.47.461118 2017-01-10-09.34.53.077890 "
                "RM 01/10/2017"),
            "999500000 "
            "2017-01-10-09.10.47.461118 2017-01-10-09.34.53.077890 "
            "RM 01/10/2017"
        )

    def test_process_quoteid_positive(self):
        """test - process_quoteid() - positive test case"""
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(quotetransform.remove_plus_symbol("\x00+999500000"), "999500000")
        self.assertEqual(quotetransform.remove_plus_symbol("\x00\x2b999500000"), "999500000")

    def test_process_quoteid_negative(self):
        """test - process_quoteid() - negative test case"""
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(quotetransform.remove_plus_symbol("999500000"), "999500000")

    def test_split_datum(self):
        """ test - split_datum()"""
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(
            quotetransform.split_datum(
                "\x00\x2b999500000 "
                "2017-01-10-09.10.47.461118 2017-01-10-09.34.53.077890 "
                "RM 01/10/2017"
                ),
            ['\x00+999500000',
             '2017-01-10-09.10.47.461118', '2017-01-10-09.34.53.077890',
             'RM', '01/10/2017']
        )
        self.assertEqual(
            quotetransform.split_datum(
                "\x00+999500022 "
                "2017-01-10-12.08.25.728764 2017-01-11-13.21.39.253151 "
                "D  01/11/2017"),
            ['\x00+999500022',
             '2017-01-10-12.08.25.728764',
             '2017-01-11-13.21.39.253151',
             'D', '', '01/11/2017']
        )
    def test_process_datein_to_dtime(self):
        """test - process_datein_to_dtime()"""
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(
            quotetransform.process_datein_to_dtime('2017-01-10-12.08.25.728764'),
            datetime.datetime(2017, 1, 10)
        )

    def test_dtime_to_formatteddtime(self):
        """test - process_dtime_to_formatteddtime()"""
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(
            quotetransform.process_dtime_to_formatteddtime(datetime.datetime(2017, 1, 10)),
            '01/10/2017'
        )

    def test_process_createdate(self):
        """test - process_createdate()"""
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(
            quotetransform.process_createdate('2017-01-10-12.08.25.728764'),
            '01/10/2017'
        )

    def test_process_datum(self):
        """test - process_datum() - 3x example datum"""
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(
            quotetransform.process_datum(
                "\x00\x2b999500000 "
                "2017-01-10-09.10.47.461118 2017-01-10-09.34.53.077890 "
                "RM 01/10/2017"),
            "999500000 01/10/2017\n"
        )
        self.assertEqual(
            quotetransform.process_datum(
                "\x00+999500022 "
                "2017-01-10-12.08.25.728764 2017-01-11-13.21.39.253151 "
                "D  01/11/2017"),
            "999500022 01/10/2017\n"
        )

    def test_join_datum(self):
        """test join_datum() method"""
        quotetransform = transform_datetime.QuoteTransform()
        self.assertEqual(
            quotetransform.join_datum('999500022', '01/10/2017'),
            "999500022 01/10/2017\n"
        )

if __name__ == '__main__':
    from pylint.lint import Run
    Run(['transform_datetime_refactored.py'], exit=False)
    Run(['transform_datetime_refactored_unittest.py'], exit=False)
    unittest.main()
