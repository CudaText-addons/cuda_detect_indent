"""
Code is based on Sublime Text's plugin detect_indentation.py
It is open source at https://github.com/randy3k/sublime-default
"""
import os
from cudatext import *
from functools import partial

MIN_INDENTED_LINES = 10
MAX_READ_LINES = 40


_homedir = os.path.expanduser('~')

def collapse_filename(fn):
    if (fn+'/').startswith(_homedir+'/'):
        fn = fn.replace(_homedir, '~', 1)
    return fn

def do_detect(ed):
    detected = False

    def do_set_spaces(n):
        nonlocal detected
        detected = True
        ed.set_prop(PROP_TAB_SPACES, True)
        ed.set_prop(PROP_TAB_SIZE, n)
        print("Detect Indent for '%s': %d spaces"%(collapse_filename(ed.get_filename()), n))

    def do_set_tabs():
        nonlocal detected
        detected = True
        ed.set_prop(PROP_TAB_SPACES, False)
        print("Detect Indent for '%s': tabs"%collapse_filename(ed.get_filename()))

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

    if not detected:
        print("Detect Indent for '%s': undetected"%collapse_filename(ed.get_filename()))


class Command:
    def on_open(self, ed_self):
        #print('on_open:', ed_self.get_filename())
        do_detect(ed_self)
