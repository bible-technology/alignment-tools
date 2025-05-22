import json

# `format` and `version` are required
# as of 0.4, the alignment spec requires an explicit `groups`
# a `scheme` needs to be declared


def convert(inp):
    group = {}
    group["type"] = inp["type"]
    if "meta" in inp:
        group["meta"] = inp["meta"]
    records = []
    for record in inp["records"]:
        records.append(record)
    group["records"] = records
    out = {
        "format": "alignment",
        "version": "0.4",
        "groups": [group]
    }
    return out


if __name__ == "__main__":
    inp = json.load(open("clear-aligner.json"))
    out = convert(inp)
    with open("clear-aligner-converted.json", "w") as f:
        json.dump(out, f, indent=2)

