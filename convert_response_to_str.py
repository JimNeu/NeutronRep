a = {'b': [['as'], ['ss']]}

def convert_to_str(report):
    keys = report.keys()
    for key in keys:
        report[key] = "\n".join(list(map(lambda item: ";".join(item), report[key])))
        print(report[key])
    return report


a = convert_to_str(a)
