#!/usr/bin/env python

import argparse
import i3ipc


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--compat", action="store_true", help="Output compatible with i3tree")
    parser.add_argument("-w", "--workspace", type=str, nargs="*", help="Workspace to display")
    parser.add_argument("-f", "--focused", action="store_true", help="Display info for focused workspace")
    args = parser.parse_args()

    i3 = i3ipc.Connection()
    tree = i3.get_tree()

    if args.compat:
        i3tree_walk_tree(tree, 0)
    else:
        if args.focused:
            current_workspace = find_focused_workspace(i3).name
            args.workspace = [current_workspace] if not args.workspace else \
                args.workspace + [current_workspace]

        walk_tree(tree, 0, filter_workspaces=args.workspace,
                  mute=args.workspace is not None)


def find_focused_workspace(con):
    workspaces = con.get_workspaces()
    for workspace in workspaces:
        if workspace.visible and workspace.focused:
            return workspace
    return None


def i3tree_display_node(description, depth):
    margin = "\t" * depth
    print("{margin}{description}".format(margin=margin, description=description))
    return depth + 1


def i3tree_walk_tree(node, depth):
    type = node.type
    orientation = node.orientation
    layout = node.layout
    name = node.name

    if type == "workspace":
        depth = i3tree_display_node("Workspace {name} ({layout} - {orientation})"
                                    .format(name=name,
                                     layout=layout,
                                     orientation=orientation),
                                    depth)

    if type == "con":
        if orientation == "none":
            if name == "content" or not name.startswith("i3bar"):
                depth = i3tree_display_node("Window {name}".format(name=name), depth)
        else:
            depth = i3tree_display_node("Split ({layout} - {orientation})".format(layout=layout,
                                                                                  orientation=orientation), depth)

    for node in node.nodes:
        i3tree_walk_tree(node, depth)


def display_node(description, depth):
    margin = "    " * depth
    print("{margin}{description}".format(margin=margin, description=description))
    return depth + 1


def walk_tree(node, depth, filter_workspaces=None, mute=False):
    type_ = node.type
    orientation = node.orientation
    layout = node.layout
    name = node.name

    if filter_workspaces is not None:
        if type_ == "workspace":
            if name not in filter_workspaces:
                mute = True
            else:
                mute = False

    if not mute:
        if type_ == "workspace":
            depth = display_node("Workspace {name} ({layout} - {orientation})"
                                 .format(name=name,
                                         layout=layout,
                                         orientation=orientation),
                                 depth)

        if type_ == "con":
            if orientation == "none":
                if name == "content" or not name.startswith("i3bar"):
                    depth = display_node("Window {name}".format(name=name), depth)
            else:
                depth = display_node("Split ({layout} - {orientation})".format(layout=layout,
                                                                                      orientation=orientation), depth)

    for node in node.nodes:
        walk_tree(node, depth, filter_workspaces=filter_workspaces, mute=mute)


if __name__ == '__main__':
    main()
