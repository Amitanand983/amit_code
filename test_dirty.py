import unittest
import os
from io import StringIO
import sys

# ✅ Dynamic import: Try optimised_code.py first, else fall back to dirty_code.py
try:
    from optimised_code import (
        process_data,
        build_big_string,
        write_temp_files,
        generate_huge_list,
        calculate_stats
    )
except ImportError:
    from dirty_code import (
        process_data,
        build_big_string,
        write_temp_files,
        generate_huge_list,
        calculate_stats
    )

class TestDirtyCode(unittest.TestCase):

    def test_process_data(self):
        result = process_data()
        self.assertEqual(len(result), 100)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[-1], 198)

    def test_build_big_string(self):
        result = build_big_string()
        self.assertTrue(result.startswith("0"))
        self.assertTrue(result.endswith("999"))
        self.assertEqual(len(result), len("".join(str(i) for i in range(1000))))

    def test_write_temp_files(self):
        write_temp_files()
        for i in range(50):
            filename = f"temp_{i}.txt"
            self.assertTrue(os.path.exists(filename))
            with open(filename, "r") as f:
                self.assertEqual(f.read(), "test")
            os.remove(filename)  # Clean up

    def test_generate_huge_list(self):
        result = generate_huge_list()
        self.assertEqual(len(result), 1000000)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 1)
        self.assertEqual(result[-1], (1000000 - 1) ** 2)

    def test_calculate_stats_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        calculate_stats()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip().splitlines()
        self.assertTrue(all(line.strip().isdigit() for line in output))

if __name__ == "__main__":
    unittest.main()
