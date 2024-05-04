import unittest

import Solution_3 as Rs


class TestFunctions(unittest.TestCase):

    def test_find_smallest_temp_spread(self):

        result = Rs.find_smallest_temp_spread("./weather.dat")
        expected_result = ("14", 2.0)
        self.assertEqual(result, expected_result)

    def test_find_smallest_goal_difference(self):

        result = Rs.find_smallest_goal_difference("./football.dat")
        expected_result = ("Aston Villa", 1.0)
        self.assertEqual(result, expected_result)

    def test_find_difference_in_column_empty_file(self):

        result = Rs.find_difference_in_column([], 1, 2, 3)
        expected_result = ("", None)
        self.assertEqual(result, expected_result)

    def test_find_difference_in_column_non_numeric_data(self):

        with self.assertRaises(ValueError):
            Rs.find_difference_in_column(
                [
                    "  Dy MxT   MnT   AvT   HDDay  AvDP 1HrP TPcpn WxType PDir AvSp Dir MxS SkyC MxR MnR AvSLP\n",
                    "\n",
                    "1 88 ab 74 53.8 0.00 F 280  9.6 270 17 1.6 93 23 1004.5\n",
                ],
                0,
                1,
                2,
            )

    def test_find_difference_in_column_omit_stars_in_col(self):

        result = Rs.find_difference_in_column(
            ["Dy Mxt Mnt\n", "\n", "1 23* 12"], 0, 1, 2
        )
        expected_result = ("1", 11.0)
        self.assertEqual(result, expected_result)

    def test_find_difference_in_column_omit_invalid_col(self):

        result = Rs.find_difference_in_column(
            [
                "Team For Against\n",
                "\n",
                "America 23* 12\n",
                "\n",
                "----------\n",
                "India 24 20",
            ],
            0,
            1,
            2,
        )
        expected_result = ("India", 4.0)
        self.assertEqual(result, expected_result)

    def test_find_difference_in_column_retunrns_label_as_string(self):

        result = Rs.find_difference_in_column(
            [
                "Team For Against\n",
                "\n",
                "America 23* 12\n",
                "\n",
                "----------\n",
                "India 24 20",
            ],
            0,
            1,
            2,
        )
        expected_result = str
        self.assertEqual(type(result[0]), expected_result)


if __name__ == "__main__":
    unittest.main()
