import json


def convert(inp):
    records = []
    for record in inp["records"]:
        records.append(record)
    group = {
        "type": inp["type"],
        "records": records,
    }
    if "meta" in inp:
        group["meta"] = inp["meta"]
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

