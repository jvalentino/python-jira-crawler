import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../main/python')))

from charting_service import ChartingService
from chart_settings import ChartSettings
from epic_grouping import EpicGrouping
from epic_setting import EpicSetting
from epic import Epic

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
        
    def test_process_grouping(self):
        # GIVEN the chart settings
        chart_settings = ChartSettings()
        chart_settings.date_min = '2024-10-07'
        chart_settings.weeks = 12
        chart_settings.row_min = 0
        chart_settings.column_min = 0
        chart_settings.column_max = 12
        
        chart_settings.date_to_column = self.charting_service.get_mapping_of_date_to_column(chart_settings)
        
        # AND There is only one grouping, that contains several epics
        epic_grouping = EpicGrouping(grouping='Group 1')
        
        # AND The first epic always has the earliest start date
        epic_setting_1 = EpicSetting()
        epic_grouping.epic_settings.append(epic_setting_1)
        
        epic_1 = Epic()
        epic_setting_1.epic = epic_1
        epic_1.key = 'EPIC-131'
        epic_1.title = 'Multi Environment'
        epic_1.start_date = '2024-10-07'
        epic_1.due_date = '2024-11-04'
        
        # AND there is a second epic
        epic_setting_2 = EpicSetting()
        epic_grouping.epic_settings.append(epic_setting_2)
        
        epic_2 = Epic()
        epic_setting_2.epic = epic_2
        epic_2.key = 'EPIC-76'
        epic_2.title = 'Storage'
        epic_2.start_date = '2024-10-21'
        epic_2.due_date = '2024-11-04'
        
        # AND there is a third epic
        epic_setting_3 = EpicSetting()
        epic_grouping.epic_settings.append(epic_setting_3)
        
        epic_3 = Epic()
        epic_setting_3.epic = epic_3
        epic_3.key = 'EPIC-72'
        epic_3.title = 'Signal'
        epic_3.start_date = '2024-10-21'
        epic_3.due_date = '2024-11-04'
        
        # AND there is a fourth epic
        epic_setting_4 = EpicSetting()
        epic_grouping.epic_settings.append(epic_setting_4)
        
        epic_4 = Epic()
        epic_setting_4.epic = epic_4
        epic_4.key = 'EPIC-74'
        epic_4.title = 'P-MAN'
        epic_4.start_date = '2024-11-04'
        epic_4.due_date = '2024-12-02'
        
        # AND there is a fifth epic
        epic_setting_5 = EpicSetting()
        epic_grouping.epic_settings.append(epic_setting_5)
        
        epic_5 = Epic()
        epic_setting_5.epic = epic_5
        epic_5.key = 'EPIC-77'
        epic_5.title = 'Events'
        epic_5.start_date = '2024-11-04'
        epic_5.due_date = '2024-11-18'
        
        # WHEN
        self.charting_service.process_grouping(chart_settings, epic_grouping)
        
        # THEN verify the position of the first epic (EPIC-131)
        self.assertEqual(0, epic_setting_1.column_start)
        self.assertEqual(3, epic_setting_1.column_end)
        self.assertEqual(0, epic_setting_1.row)
        self.assertEqual('A', epic_setting_1.alpha_key)
        
        # AND verify the position of the second epic (EPIC-76)
        self.assertEqual(2, epic_setting_2.column_start)
        self.assertEqual(3, epic_setting_2.column_end)
        self.assertEqual(1, epic_setting_2.row)
        self.assertEqual('B', epic_setting_2.alpha_key)
        
        # AND verify the position of the third epic (EPIC-72)
        self.assertEqual(2, epic_setting_3.column_start)
        self.assertEqual(3, epic_setting_3.column_end)
        self.assertEqual(2, epic_setting_3.row)
        self.assertEqual('C', epic_setting_3.alpha_key)
        
        # AND verify the position of the fourth epic (EPIC-74)
        self.assertEqual(4, epic_setting_4.column_start)
        self.assertEqual(7, epic_setting_4.column_end)
        self.assertEqual(0, epic_setting_4.row)
        self.assertEqual('D', epic_setting_4.alpha_key)
        
        # AND verify the position of the firth epic (EPIC-77)
        self.assertEqual(4, epic_setting_5.column_start)
        self.assertEqual(5, epic_setting_5.column_end)
        self.assertEqual(1, epic_setting_5.row)
        self.assertEqual('E', epic_setting_5.alpha_key)
        
        # and verify the max row for the grouping
        self.assertEqual(2, epic_grouping.row_max)
        self.assertEqual(7, epic_grouping.column_max)
        self.assertEqual(0, epic_grouping.column_min)
        

        
        
        
        
        
        
        