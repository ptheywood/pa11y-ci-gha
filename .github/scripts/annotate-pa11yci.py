#! /usr/bin/env python3
"""
Parse a provided json file which is assumed to include output from pa11y-ci and output strings to stdout which will produce annotations on github actions 
As there is no simple mapping from html output back to source, this will not embed lines / columns?
"""

import json
import argparse
import pathlib
import enum

@enum.unique
class GHAAnnotation(enum.Enum):
    NOTICE = "notice"
    WARNING = "warning"
    ERROR = "error"


def annotate(annotation_type, message, file):
    s = f"::{annotation_type.value} file={file}::{message}"
    print(s)

def main():
    # Parse cli
    parser = argparse.ArgumentParser(description='Parse pa11y-ci json output, producing annotation strings for GitHub ACtions')
    parser.add_argument(
        "input",
        type=pathlib.Path,
        help="Json file to parse"
    )
    args = parser.parse_args()

    # Load the json 
    with open(args.input) as input_file:
        data = json.load(input_file)
        # Process the data, outputting annotation strings.
        # print(data)
        # summary_errors=data["errors"]
        # print(summary_errors)

        annotate(GHAAnnotation.NOTICE, "a notice", "file.txt")
        annotate(GHAAnnotation.WARNING, "a warning", "file2.txt")
        annotate(GHAAnnotation.ERROR, "a error msg", "file.txt")
        annotate(GHAAnnotation.ERROR, "a error msg", "file.txt")

if __name__ == "__main__":
    main()


# cat report.json | jq ".total"
#   echo "::notice file=app.js,line=1,col=5,endColumn=7::Missing semicolon"
#   echo "::warning file=app.js,line=1,col=5,endColumn=7::Missing semicolon"
#   echo "::error file=app.js,line=1,col=5,endColumn=7::Missing semicolon"