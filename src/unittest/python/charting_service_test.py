import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../main/python')))

from charting_service import ChartingService
from chart_settings import ChartSettings

class ChartingServiceTest(unittest.TestCase):
    def setUp(self):
        # This method will be run before each test
        self.charting_service = ChartingService()
        
    def test_helloworld(self):
        print("hello world")
        self.assertEqual(3, 3)
        
    def test_get_mapping_of_date_to_column(self):
        print("test_get_mapping_of_date_to_column")
        chart_settings = ChartSettings()
        chart_settings.date_min = '2024-10-07'
        chart_settings.weeks = 12
        
        mapping = self.charting_service.get_mapping_of_date_to_column(chart_settings)
        print(f"   Mapping: {mapping}")
        
        self.assertEqual(13, len(mapping))
        self.assertEqual(0, mapping['2024-10-07'])
        self.assertEqual(1, mapping['2024-10-14'])
        self.assertEqual(2, mapping['2024-10-21'])
        self.assertEqual(3, mapping['2024-10-28'])
        self.assertEqual(4, mapping['2024-11-04'])
        self.assertEqual(5, mapping['2024-11-11'])
        self.assertEqual(6, mapping['2024-11-18'])
        self.assertEqual(7, mapping['2024-11-25'])
        self.assertEqual(8, mapping['2024-12-02'])
        self.assertEqual(9, mapping['2024-12-09'])
        self.assertEqual(10, mapping['2024-12-16'])
        self.assertEqual(11, mapping['2024-12-23'])
        self.assertEqual(12, mapping['2024-12-30'])
        