# py3tree

A reimplementation of [i3tree](https://github.com/sciurus/i3tree) in Python, using [i3ipc](https://github.com/acrisci/i3ipc-python).

# Overview

i3tree is a program written by sciurus in Perl for the i3 tiling window manager.

This project is a reimplementation of this tool in Python.

# Installation

    $ pip install --user py3tree

# Usage

Show the entire tree, including all workspaces:

    $ py3tree

Show the tree for just the workspace named "1":

    $ py3tree -w 1

Show the tree for both the workspace named "1" and the workspace named "two":

    $ py3tree -w 1 two

Show the tree for the current focused workspace:

    $ py3tree -f

# Acknowledgements

Thank you to sciurus for the original i3tree, licensed under the GPLv3.



