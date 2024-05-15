#!/usr/bin/env python3

from validator import validate


def test(filename, error=None):
    result = validate(filename)
    if result is True:
        if error is None:
            print(f"✅ {filename} passed")
        else:
            print(f"❌ {filename} should have failed with error: {error:03d}")  # pragma: no cover
    else:
        if error is None:
            print(f"❌ {filename} failed with error: {result[0]:03d} but should have passed")  # pragma: no cover
        elif result[0] != error:
            print(f"❌ {filename} failed with error: {result[0]:03d} instead of {error:03d}")  # pragma: no cover
        else:
            print(f"✅ {filename} correctly failed with error: {error:03d}")


test("tests/test_001.json")
test("tests/test_002.json")
test("tests/test_003_bad.json", 3)
test("tests/test_004_bad.json", 3)
test("tests/test_005_bad.json", 1)
test("tests/test_006_bad.json", 2)
test("tests/test_007_bad.json", 4)
test("tests/test_008_bad.json", 5)
test("tests/test_009.json")
test("tests/test_010_bad.json", 6)
test("tests/test_011_bad.json", 7)
test("tests/test_012_bad.json", 8)
test("tests/test_013_bad.json", 9)
test("tests/test_014_bad.json", 10)
test("tests/test_015_bad.json", 11)
test("tests/test_016.json")
test("tests/test_017_bad.json", 12)
test("tests/test_018_bad.json", 13)
test("tests/test_019_bad.json", 14)
test("tests/test_020_bad.json", 12)
test("tests/test_021_bad.json", 15)
test("tests/test_022.json")
test("tests/test_023_bad.json", 15)
test("tests/test_024_bad.json", 16)
test("tests/test_025_bad.json", 17)
test("tests/test_026_bad.json", 18)
test("tests/test_027.json")
test("tests/test_028.json")
test("tests/test_029.json")
test("tests/test_030.json")
