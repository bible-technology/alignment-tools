#!/usr/bin/env python3

import json


timestamp = None

records = []

for line in open("import/example.vtt"):
    line = line.strip()
    if line == "WEBVTT":
        pass
    elif line == "":
        pass
    elif line.startswith("NOTE "):
        pass
    elif line.startswith("<c.u23003>"):
        if timestamp:
            # records.append({"references": [[timestamp], [line[len("<c.u23003>"):-len("</c>")]]]})
            records.append({"timecode": [timestamp], "text-reference": [line[len("<c.u23003>"):-len("</c>")]]})
    elif line.startswith("- "):
        pass
    elif " --> " in line:
        timestamp = line
    else:
        assert False, line

data = {
    "format": "alignment",
    "version": "0.3",
    "type": "audio-reference",
    "documents": {
        "timecode": {"scheme": "vtt-timecode", "docid": "ephesians_example_with_footnotes.mp3"},
        "text-reference:": {"scheme": "u23003"},
    },
    # "roles": ["timecode", "text-reference"],
    "records": records
}

print(json.dumps(data, indent=2))
