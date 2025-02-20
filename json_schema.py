#!/usr/bin/env python3

import json

from jsonschema import validate


SCHEMA_04 = json.load(open("schema-0.4.json"))


def test(filename, error=False):
    instance = json.load(open(filename))
    try:
        validate(
            instance=instance,
            schema=SCHEMA_04,
        )
        result = True
    except Exception as e:
        result = e

    if result is True:
        if error is False:
            print(f"✅ {filename} passed")
        else:
            print(f"❌ {filename} should have failed with error.")  # pragma: no cover
    else:
        if error is False:
            print(f"❌ {filename} failed with error: {result} but should have passed")  # pragma: no cover
        else:
            print(f"✅ {filename} correctly failed.")



test("tests/test_001.json")
test("tests/test_002_bad.json", True)
test("tests/test_003_bad.json", True)
test("tests/test_004_bad.json", True)
test("tests/test_005_bad.json", True)
test("tests/test_006_bad.json", True)
test("tests/test_007_bad.json", True)
test("tests/test_008_bad.json", True)
test("tests/test_009.json")
test("tests/test_010_bad.json", True)
test("tests/test_011_bad.json", True)
test("tests/test_012_bad.json", True)
test("tests/test_013_bad.json", True)
test("tests/test_014_bad.json", True)
test("tests/test_015_bad.json", True)
test("tests/test_016.json")
test("tests/test_017_bad.json", True)
test("tests/test_018_bad.json", True)
test("tests/test_019_bad.json", True)
test("tests/test_020_bad.json", True)
test("tests/test_021_bad.json", True)
test("tests/test_022.json")
test("tests/test_023_bad.json", True)
test("tests/test_024_bad.json", True)
test("tests/test_025_bad.json", True)
test("tests/test_026_bad.json", True)
test("tests/test_027.json")
# test("tests/test_028.json")
# test("tests/test_029.json")
test("tests/test_030.json")


