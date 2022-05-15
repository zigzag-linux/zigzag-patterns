#!/usr/bin/env python3

import json
from string import Template

TEMPLATE_MAIN_FILE = "templates/main_file.tpl"
TEMPLATE_PATTERN = "templates/section_pattern.tpl"
TEMPLATE_REQUIRES = "templates/section_requires.tpl"
FILE_INPUT = "patterns.json"
FILE_OUTPUT = "patterns-zigzag.spec"


def render_file_template(filename, subsitutions):
    with open(filename, "r") as file:
        template = Template(file.read())

    return template.substitute(**subsitutions)


def load_patterns():
    with open(FILE_INPUT, "r") as file:
        return json.load(file)


def render_requires(packages):
    get_input_vars = lambda x: {"package_name": x}
    rendered_list = [
        render_file_template(TEMPLATE_REQUIRES, get_input_vars(package))
        for package in packages
    ]

    return "".join(rendered_list)


def render_patterns(patterns):
    get_input_vars = lambda name, x: {
        "pattern_name": name,
        "pattern_summary": x["summary"],
        "pattern_description": x.get("description", x["summary"]),
        "extra_meta": "\n".join(x.get("meta", [])),
        "required_packages": render_requires(x["packages"]),
    }
    rendered_list = [
        render_file_template(TEMPLATE_PATTERN, get_input_vars(key, value))
        for key, value in patterns.items()
    ]

    return "".join(rendered_list)


def render_main_file():
    patterns = load_patterns()
    input_vars = {
        "all_patterns": ",".join(list(patterns.keys())),
        "pattern_sections": render_patterns(patterns),
    }

    with open(FILE_OUTPUT, "w") as file:
        file.write(render_file_template(TEMPLATE_MAIN_FILE, input_vars))


if __name__ == "__main__":
    render_main_file()
