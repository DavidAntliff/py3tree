#!/usr/bin/env python

import argparse
import i3ipc


def main():
    i3 = i3ipc.Connection()
    tree = i3.get_tree()

    walk_tree(tree, 0)


def display_node(description, depth):
    margin = "\t" * depth
    print("{margin}{description}".format(margin=margin, description=description))
    return depth + 1


def walk_tree(node, depth):
    type = node.type
    orientation = node.orientation
    layout = node.layout
    name = node.name

    if type == "workspace":
        depth = display_node("Workspace {name} ({layout} - {orientation})"
                             .format(name=name,
                                     layout=layout,
                                     orientation=orientation),
                             depth)

    if type == "con":
        if orientation == "none":
            if name == "content" or not name.startswith("i3bar"):
                depth = display_node("Window {name}".format(name=name), depth)
        else:
            depth = display_node("Split ({layout} - {orientation})".format(layout=layout,
                                                                          orientation=orientation), depth)

    for node in node.nodes:
        walk_tree(node, depth)


if __name__ == '__main__':
    main()
