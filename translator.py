def map_corrections(corrections: list[str]) -> dict[str, str]:
    map = {}
    for correction in corrections:
        split = correction.split(" -> ")
        map[split[0]] = split[1]
    return map


def subst_corrections(program: str, corrections: dict[str, str]) -> str:
    transformed = program
    for var, sub in corrections.items():
        transformed = transformed.replace(var, "{" + sub + "}")

    return transformed


def subst_vars(program: str, vars: dict[str, str]) -> str:
    transformed = program
    for var, val in vars.items():
        transformed = transformed.replace(var, val)

    return transformed


def translate_to_sketch(
    program: str, assignments: dict[str, str], correction_map: dict[str, str]
) -> str:
    translated = ""
    func_map = {}
    sub_number = 0
    for var, sub in correction_map.items():
        func_map[var] = sub_number
        translated += "int correction" + str(sub_number) + "(int " + var + ") {\n"
        for i, val in enumerate(sub.split(", ")):
            if i == 0:
                translated += "\tif (??) return " + val + ";\n"
            else:
                translated += "\telse if (??) return " + val + ";\n"
        translated += "}\n\n"
        sub_number += 1

    translated += "harness void main() {\n"
    for var, val in assignments.items():
        translated += (
            "\tint " + var + " = correction" + str(func_map[var]) + "(" + val + ");\n"
        )
    translated += "\tassert " + program + ";\n"
    translated += "}\n"

    return translated


def main():
    corrections = ["n -> n, n - 1, n + 1"]
    vars = ["n = 4"]
    program = "1 + 2 + 3 + 4 + n == 15"

    correction_map = map_corrections(corrections)
    assignments = {var.split(" = ")[0]: var.split(" = ")[1] for var in vars}
    transformed = subst_vars(subst_corrections(program, correction_map), assignments)
    print(transformed)

    translated = translate_to_sketch(program, assignments, correction_map)
    with open("translated.sk", "w") as sk_file:
        print(translated, file=sk_file)


if __name__ == "__main__":
    main()
