import json


def validate_reference_unit(reference_unit, document_hoist):
    if isinstance(reference_unit, list):
        if document_hoist.get("scheme"):
            for selector in reference_unit:
                if not isinstance(selector, str):
                    return (15, 'Each selector must be a string')
        else:
            return (20, 'A reference unit can only be a list of selectors if the scheme is hoisted')
    elif isinstance(reference_unit, dict):
        for key in reference_unit.keys():
            if key not in ["scheme", "docid", "selectors"]:
                return (12, 'A reference unit object must have only have "scheme", "docid", and "selectors" properties')
        if "scheme" not in reference_unit.keys() and "scheme" not in document_hoist.keys():
            return (21, 'If "scheme" is not present on a reference unit, it must be present on the document hoist')
        if not isinstance(reference_unit["scheme"], str):
            return (16, 'The "scheme" property must be a string')
        if not isinstance(reference_unit["docid"], str):
            return (17, 'The "docid" property must be a string')
        if not isinstance(reference_unit["selectors"], list):
            return (18, 'The "selectors" property must be a list')
        for selector in reference_unit["selectors"]:
            if not isinstance(selector, str):
                return (15, 'Each selector must be a string')
    else:
        return (13, 'A reference unit must be a list or an object')


def validate(filename):
    data = json.load(open(filename))

    if data.get("format") != "alignment":
        return (1, 'Must have "format": "alignment"')
    if data.get("version") not in ["0.4"]:
        return (2, 'Must have "version" that is in ["0.4"]')
    if "groups" not in data:
        return (3, 'Must have "groups"')
    if "groups" in data and not isinstance(data["groups"], list):
        return (4, '"groups" must be a list')
    if "records" in data:
        return (5, '"records" is not allowed at the top level in this version of the format')

    for group in data["groups"]:
        if not isinstance(group, dict):
            return (19, 'Each group must be a dictionary')
        for record in group.get("records", []):
            if not isinstance(record, dict):
                return (6, 'Each record must be a dictionary')
            if "type" not in record and "type" not in group:
                return (7, 'Each record must have a "type" unless the group has a type')
            if not isinstance(record.get("meta", {}), dict):
                return (8, 'If "meta" is present on a record, it must be a dictionary')
            if not isinstance(record.get("references", []), list):
                return (9, 'If "references" is present on a record, it must be a list')
            if "references" not in record and not [key for key in record.keys() if key not in ["type", "meta"]]:
                return (10, 'If "references" is not present on a record, it must have other keys besides "type" and "meta"')
            if "references" in record and [key for key in record.keys() if key not in ["type", "meta", "references"]]:
                return (11, 'If "references" is present on a record, it must not have other keys besides "type", "meta", and "references"')
            for key, value in record.items():
                if key not in ["type", "meta", "references"]:
                    # unit role
                    result = validate_reference_unit(value, group)
                    if result is not None:
                        return result
            if "references" in record:
                if record["references"] == []:
                    return (14, 'A references list cannot be empty')
                for reference_unit in record["references"]:
                    result = validate_reference_unit(reference_unit, group)
                    if result is not None:
                        return result

    return True
