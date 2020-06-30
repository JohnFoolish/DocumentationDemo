"""
This module is use to generate a png image from a tree_string.

Usage below:
    >>> tree_string = "Learner(ARG0, ModifyLearnerList(LearnerType('LIGHTGBM', {'max_depth': -1, 'learning_rate': 0.1, 'boosting_type': 0, 'num_leaves': 31}), myListAppend(myIntToList(32), passList([-3, 1])), passInt(4)), ModifyEnsembleFloat(EnsembleType('ADABOOST', {'n_estimators': 50, 'learning_rate': 1.0}), myFloatIntAdd(0.01, 7), 3))"
    >>> tree_string_parser(tree_string)

.. image:: _static/exampleOutput.png

.. warning::
    Install graphiz for this module to work if not then the plot_tree will cause error

Note:
    This module is based on a pickle file called node_typesV2.pkl.
    If need to update the pickle file use :doc:`updateNoteTypes`
Written by ADF team, Modified by Hoa V Luu
"""

import re, json, pydot, hashlib, pickle


def get_node_color(node_label):
    """ Get the color of a node in the tree

    Args:
        node_label (str): The label of a node

    Returns:
        The color that matched with the node_label
    """
    for NODE_KEY in list(NODE_TYPES.keys()):
        if node_label in NODE_TYPES[NODE_KEY]:
            return NODE_COLOR_DICT[NODE_KEY]
    try:
        x = int(node_label)
        return NODE_COLOR_DICT['Terminals']
    except:
        try:
            x = float(node_label)
            return NODE_COLOR_DICT['Terminals']
        except:
            try:
                node_label = node_label.replace("\'", "\"")
                tree = json.loads(node_label)
                for key in tree.keys():
                    if key not in NODE_TYPES['Learner Params']:
                        return NODE_COLOR_DICT['Uncategorized']
                    else:
                        try:
                            x = int(tree[key])
                        except:
                            try:
                                x = float(tree[key])
                            except:
                                return NODE_COLOR_DICT['Uncategorized']
                return NODE_COLOR_DICT['Learner Params']
            except:
                return NODE_COLOR_DICT['Uncategorized']
    return NODE_COLOR_DICT['Uncategorized']


def walk_dictionary(graph, dictionary, parent_node=None):
    for k in dictionary.keys():
        if parent_node is not None:
            from_name = parent_node.get_name().replace("\"", "") + '_' + str(k)
            from_label = str(k)
            node_color = get_node_color(from_label)
            node_from = pydot.Node(from_name, label=from_label, style="filled", fillcolor=node_color)
            graph.add_node(node_from)
            graph.add_edge(pydot.Edge(parent_node, node_from))

            if isinstance(dictionary[k], dict):
                walk_dictionary(graph, dictionary[k], node_from)
            else:
                to_name = str(k) + '_' + str(dictionary[k])
                to_label = str(dictionary[k])
                if to_label != '[]':
                    node_to = pydot.Node(to_name, label=to_label, shape='box')
                    graph.add_node(node_to)
                    graph.add_edge(pydot.Edge(node_from, node_to))
        else:
            from_name = str(k)
            from_label = str(k)
            node_color = get_node_color(from_label)
            node_from = pydot.Node(from_name, label=from_label, style="filled", fillcolor=node_color)
            graph.add_node(node_from)
            walk_dictionary(graph, dictionary[k], node_from)


def plot_tree(tree, name):
    """ Plot and generate a png image of a tree with the tree hashed name

    Args:
        tree (dict): A dictionary contains all information of a tree
        name (str): The hashed name of the tree
    """
    graph = pydot.Dot(graph_type='graph')
    tree_graph = pydot.Cluster(
        graph_name="Learner Tree",
        label="Learner Tree",
        fontsize="15",
    )
    graphlegend = pydot.Cluster(
        graph_name="legend",
        label="Legend",
        fontsize="15",
        rankdir="LR")
    legends = []
    for NODE_KEY in list(NODE_TYPES.keys()):
        legend = pydot.Node(
            NODE_KEY,
            style="filled",
            fillcolor=NODE_COLOR_DICT[NODE_KEY],
            rank="same"
        )
        graphlegend.add_node(legend)
        legends.append(legend)

    walk_dictionary(tree_graph, tree)
    graph.add_subgraph(tree_graph)
    graph.add_subgraph(graphlegend)
    for legend_index in range(1, len(legends)):
        graph.add_edge(pydot.Edge(legends[legend_index - 1], legends[legend_index], style="invis"))
    graph.write_png('./' + name + '.png')


def create_hash(tree_string):
    """ Generate a hash from the tree_string

    Args:
        tree_string: The tree_string want to hash

    Returns:
        A hashed name for the tree_string
    """
    return hashlib.md5(tree_string.encode()).hexdigest()


def fix_up_tree(tree_dict):
    """ Fix any edge cases of the tree_dict

    Args:
        tree_dict (dict): The dictionary that contains all the information of a tree

    Returns:
        A fixed dictionary that contains all the information of a tree
    """
    if isinstance(tree_dict, dict):
        for key in list(tree_dict.keys()):
            if key == 'ARGS':
                tree_dict[str(tree_dict[key][0]).replace("\'", "")] = []
                tree_dict.pop(key)
                continue
            if isinstance(tree_dict[key], dict) and (key == 'LearnerType' or key == "EnsembleType"):
                arg_dict = {}
                value_dict = {}
                for k in tree_dict[key].keys():
                    if isinstance(tree_dict[key][k], list):
                        arg_dict[k] = tree_dict[key][k]
                    else:
                        try:
                            value = int(tree_dict[key][k])
                        except:
                            try:
                                value = float(tree_dict[key][k])
                            except:
                                value = tree_dict[key][k]
                        value_dict[k] = value
                arg_dict[str(value_dict)] = []
                tree_dict[key] = arg_dict
            if isinstance(tree_dict[key], str):
                tree_dict[key] = {tree_dict[key]: []}
            if isinstance(tree_dict[key], list) and tree_dict[key] != []:
                arg_dict = {}
                for item in tree_dict[key]:
                    if isinstance(item, list):
                        item = [int(i) for i in item]
                        arg_dict[str(item)] = []
                    else:
                        arg_dict[item] = []
                tree_dict[key] = arg_dict
            fix_up_tree(tree_dict[key])
    else:
        return


def tree_string_parser(tree_string):
    """ Parse a tree_string to a dictionary

    Args:
        tree_string (str): Tree_string wanted to parse
    """
    tree_hash = create_hash(tree_string)
    tree_string = tree_string.replace("(", "{")
    tree_string = tree_string.replace(")", "}")
    tree_string = "{" + tree_string + "}"
    tree_string = tree_string.replace("'", "")

    data = re.sub(r'([\w\.\-]+)', r'"\1"', tree_string)  # {"val1" {"val2" {"d1" "d2" "d3"}}}
    data = re.sub(r'"\s*{', r'": {', data)  # {"val1": {"val2": {"d1" "d2" "d3"}}}
    data = re.sub(r'" "', r'", "', data)  # {"val1": {"val2": {"d1", "d2", "d3"}}}
    data = re.sub(r'{([^{}]*)}', r'[\1]', data)  # {"val1": {"val2": ["d1", "d2", "d3"]}}
    data = re.sub(r'\[([\"\:\, \w\.\-]+:+[\"\:\, \w\.\-]+)\]', r'\1', data)
    data = re.sub(r'({[\"\w\.\-]+),', r'\1: [],', data)
    data = re.sub(r', (\"[\"\w\.\-]+\")}', r', \1: []}', data)
    data = re.sub(r', (\"[\"\w\.\-]+\"),(?![^\[]*\])', r', \1: [],', data)
    data = re.sub(r', (\"[\"\w\.\-]+\"),(?![^\[]*\])', r', \1: [],', data)
    data = re.sub(r', \[(.*?)\]', r', "ARGS": [[\1]]', data)
    try:
        tree_dict = json.loads(data)
    except:
        print("Error from json.loads: " + data)
    try:
        fix_up_tree(tree_dict)
    except:
        print("Error from fix_up_tree: " + data)
    try:
        plot_tree(tree_dict, tree_hash)
    except:
        print("Error from plot tree: " + data)


if __name__ == "__main__":
    NODE_TYPES = {}
    NODE_COLOR_DICT = {}
    NODE_COLORS = [
        '#D09248',
        '#C0C572',
        '#90EE90',
        '#ACD4C0',
        '#B19CD9',
        '#26808A',
        "#FFFFFF"
    ]

    with open('node_typesV2.pkl', 'rb') as f:
        NODE_TYPES = pickle.load(f)

    NODE_TYPES['Uncategorized'] = []

    for i, NODE_KEY in enumerate(list(NODE_TYPES.keys())):
        NODE_COLOR_DICT[NODE_KEY] = NODE_COLORS[i]

    tree_string = "Learner(ARG0, ModifyLearnerList(LearnerType('LIGHTGBM', {'max_depth': -1, 'learning_rate': 0.1, 'boosting_type': 0, 'num_leaves': 31}), myListAppend(myIntToList(32), passList([-3, 1])), passInt(4)), ModifyEnsembleFloat(EnsembleType('ADABOOST', {'n_estimators': 50, 'learning_rate': 1.0}), myFloatIntAdd(0.01, 7), 3))"
    tree_string = "MyDiff(Learner(EmadeDataNumpyMultiplyFloat(EmadeDataSubtractFloat(ARG0, TriState.FEATURES_TO_FEATURES, Axis.AXIS_0, 10.0), TriState.STREAM_TO_STREAM, Axis.AXIS_1, 4.290944071481347), ModifyLearnerBool(LearnerType('BAYES', None), trueBool, myIntMult(equal(1.0, 0.01), greaterThanEqual(0.1, 100.0))), ModifyEnsembleInt(EnsembleType('ADABOOST', {'n_estimators': 50, 'learning_rate': 1.0}), 5, 9)), passTriState(passTriState(TriState.FEATURES_TO_FEATURES)), passAxis(passAxis(Axis.AXIS_0)))"
    tree_string = "Learner(ARG0, ModifyLearnerList(ModifyLearnerFloat(ModifyLearnerBool(LearnerType('BOOSTING', {'learning_rate': 0.1, 'n_estimators': 100, 'max_depth': 3}), trueBool, 2496), myIntToFloat(9), notEqual(0.01, 10.0)), myListAppend(passList([-13, -15]), [6, -7]), equal(10.0, myFloatIntSub(100.0, 64))), EnsembleType('BAGGED', None))"
    tree_string_parser(tree_string)
