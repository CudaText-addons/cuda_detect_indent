"""
Code is based on Sublime Text's plugin detect_indentation.py
It is open source at https://github.com/randy3k/sublime-default
"""
from cudatext import *
from functools import partial

MIN_INDENTED_LINES = 10
MAX_READ_LINES = 40


def do_detect(ed):

    def do_set_spaces(n):
        ed.set_prop(PROP_TAB_SPACES, True)
        ed.set_prop(PROP_TAB_SIZE, n)
        print("Detect Indent: %d spaces"%n)

    def do_set_tabs():
        ed.set_prop(PROP_TAB_SPACES, False)
        print("Detect Indent: tabs")

    nlines = min(MAX_READ_LINES, ed.get_line_count())
    lines = [ed.get_text_line(i) for i in range(nlines)]

    starts_with_tab = 0
    spaces_list = []
    indented_lines = 0

    for line in lines:
        if not line: continue
        if line[0] == "\t":
            starts_with_tab += 1
            indented_lines += 1
        elif line.startswith(' '):
            spaces = 0
            for ch in line:
                if ch == ' ': spaces += 1
                else: break
            if spaces > 1 and spaces != len(line):
                indented_lines += 1
                spaces_list.append(spaces)

    evidence = [1.0, 1.0, 0.8, 0.9, 0.8, 0.9, 0.9, 0.95, 1.0]

    if indented_lines >= MIN_INDENTED_LINES:
        if len(spaces_list) > starts_with_tab:
            for indent in range(8, 1, -1):
                same_indent = list(filter(lambda x: x % indent == 0, spaces_list))
                if len(same_indent) >= evidence[indent] * len(spaces_list):
                    do_set_spaces(indent)
                    return

            for indent in range(8, 1, -2):
                same_indent = list(filter(lambda x: x % indent == 0 or x % indent == 1, spaces_list))
                if len(same_indent) >= evidence[indent] * len(spaces_list):
                    do_set_spaces(indent)
                    return

        elif starts_with_tab >= 0.8 * indented_lines:
            do_set_tabs()


class Command:
    def on_open(self, ed_self):
        do_detect(ed_self)
