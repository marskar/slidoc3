#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Main module."""

import sys
import pytest
from pypandoc import convert_file


def write_file(filename: str, contents: str) -> None:
    """Writes contents to a file named filename

    Arguments:
        filename: The name of the target file
        contents: The contents of the target file

    Examples:
        >>> import tempfile
        >>> outfile_path = tempfile.mkstemp()[1]
        >>> write_file(outfile_path, "Test file contents")
        >>> with open(outfile_path) as file: file.read()
        'Test file contents'
    """
    with open(filename, 'w') as f:
        f.write(contents)


def make_slides(to: str = 'slidy') -> str:
    """Create HTML slides from a slides.md file

    Arguments:
        to: The HTML slideshow format, must be slidy or dzslides

    Returns:
        A string of characters that are the contents of an html slideshow

    Raises:
        ValueError: If the 'to' argument is not 'slidy' or 'dzslides'

    Examples:
        >>> import tempfile # library needed to make temp files
        >>> infile_path = tempfile.mkstemp('.md')[1] # markdown file path
        >>> write_file(infile_path, "# Markdown header") # markdown content
        >>> outfile_path = tempfile.mkstemp(suffix='.html')[1] # html file path
        >>> write_file(outfile_path, make_slides(infile_path)) # html slides
        >>> with open(outfile_path, "r") as f: outfile_contents = f.read()
        >>> lines = outfile_contents.split('\\n') # split contents into lines
        >>> lines[0] # first line
        '<?xml version="1.0" encoding="utf-8" ?>'
        >>> lines[-4] # fourth to last line
        '<div id="markdown-header" class="titleslide slide section level1"><h1>Markdown header</h1></div>'
    """
    if to in ('slidy', 'dzslides'):
        return convert_file('slides.md', to=to, extra_args=['--self-contained'])
    else:
        raise ValueError


if __name__ == '__main__':
    pytest.main(sys.argv)
