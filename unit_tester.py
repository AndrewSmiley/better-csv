# 2015.09.18 21:37:43 EDT
#Embedded file name: /Volumes/Untitled/Excel Parser/unit_tester.py
__author__ = 'pridemai'
import unittest
from parse_functions import get_lists, search

class ParseTestCases(unittest.TestCase):

    def test_1(self):
        self.assertEqual(len(get_lists(['\" $(3,562.86)\",\"$174,565.86\",,,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls'])[0]), 11)

    def test_2(self):
        self.assertEqual(len(get_lists(['\" $(3,562.86)\",\"$174,565.86\",,,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls,'])[0]), 12)

    def test_3(self):
        self.assertEqual(len(get_lists(['\" $(3,562.86)\",\"$174,565.86\",,,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls,,'])[0]), 13)

    def test_4(self):
        self.assertEqual(len(get_lists(['\" $(3,562.86)\",\"$174,565.86\",,,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls,,\"\",'])[0]), 14)

    def test_5(self):
        self.assertEqual(len(get_lists(['\" $(3,562.86)\",\"$174,565.86\",,,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls,,\"asf\",,'])[0]), 15)

    def test_6(self):
        self.assertEqual(len(get_lists(['\" $(3,562.86)\",\"$174,565.86\",,,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls,,\"asf\",,data'])[0]), 15)

    def test_7(self):
        self.assertEqual(len(get_lists(['$(3562.86),\"$174,565.86\",\"as\",,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls,,\"asf\",,data'])[0]), 15)

    def test_8(self):
        self.assertEqual(len(get_lists(['\" $(3,562.86)\",,,\"$174,565.86\",,,\"Liming new source\",,,\"sympathetic, never let it show the way i feel i do \",,,\"data\",,,\"fuck\",,,\"balls\"'])[0]), 19)

    def test_9(self):
        self.assertEqual(len(get_lists(['\" $(3,562.86)\",,,\"$174,565.86\",,,\"Liming new source\",,,\"sympathetic, never let it show the way i feel i do \",,,\"data\",,,\"fuck\",,,\"balls\",,,'])[0]), 22)

    def test_10(self):
        self.assertEqual(len(get_lists([',,\" $(3,562.86)\",,,\"$174,565.86\",,,\"Liming new source\",,,\"sympathetic, never let it show the way i feel i do \",,,\"data\",,,\"fuck\",,,\"balls\",,,'])[0]), 24)

    def test_11(self):
        self.assertEqual(len(get_lists(['hello,,\" $(3,562.86)\",,,\"$174,565.86\",,,\"Liming new source\",,,\"sympathetic, never let it show the way i feel i do \",,,\"data\",,,\"fuck\",,,\"balls\",,,'])[0]), 24)

    def test_12(self):
        self.assertEqual(len(get_lists(['\" $(3,562.86)\",\"$174,565.86\",\"Liming new source\",\"sympathetic, never let it show the way i feel i do \",\"data\",\"fuck\",\"balls\"'])[0]), 7)
    def test_13(self):
        self.assertEqual(len(get_lists(["\" $(3,562.86)\",\"$174,565.86\",\"Liming new source\",\"sympathetic, never let it show the way i feel i do \",\"data\",\"fuck\",\"balls\""])[0]), 7)
    def test_14(self):
        self.assertEqual(len(get_lists([",,,,,,,"])[0]), 8)
    def test_15(self):
        self.assertEqual(len(get_lists(["\n,\n,\n,\n,\n,\n,\n,\n"])[0]), 8)
    def test_16(self):
        self.assertEqual(len(get_lists(["\r,\r,\r,\r,\r,\r,\r,\r"])[0]), 8)
    def test_17(self):
        self.assertEqual(search(["2463M43P05","2463M43P05"], ["2463M43P05","2463M43P05"]),True)
    def test_18(self):
        self.assertEqual(search(["2463M43P05",""], ["2463M43P05-AS02","2463M43P05JEKQ"]),True)
    def test_19(self):
        self.assertEqual(search(["",""], ["2463M43P05-AS02","2463M43P05JEKQ"]),False)
    def test_20(self):
        self.assertEqual(search(["2463M43P05",""], ["",""]),False)
    def test_21(self):
        self.assertEqual(search([" ","2463M43P05"], [" "," "]),False)
if __name__ == '__main__':
    unittest.main()

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.09.18 21:37:43 EDT
