"""
This module is used to update the pickle file that contains all the primitive,
terminal, ephemeral, and constants use in EMADE

Usage below:
    >>> pickleFile = 'node_typesV2.pkl'
    >>> previousInfo = addNewLearner(pickleFile, ['SINGLE', 'GRID'])

Written by Hoa V Luu - Henry
"""

import pickle


def loadFile(pickleFile):
    """ Load a pickle file and return the information that contains in the pickle file

    Args:
        pickleFile (str): Path and name of the pickle file

    Returns:
        A dictionary contains all the information in the given pickle file
    """
    pkl_file = open(pickleFile, 'rb')
    info = pickle.load(pkl_file)
    pkl_file.close()
    return info


def writeFile(pickleFile, dict):
    """ Write back information to a pickle file

    Args:
        pickleFile (str): Path and name of the pickle file
        dict (dict): Dictionary contains all the information want to write back

    """
    output = open(pickleFile, 'wb')
    pickle.dump(dict, output)
    output.close()


def addNewLearner(pickleFile, newLearners):
    """ Add a list of new learners to the pickle file

    Args:
        pickleFile (str): Path and name of the pickle file
        newLearners (list): List of new learners want to add to the pickle file

    Returns:
        A copy of the dictionary that contains all the information previously
    """
    currentInfo = loadFile(pickleFile)
    copyCurrentInfo = currentInfo.copy()
    currentInfo['Learners'].extend(newLearners)
    writeFile(pickleFile, currentInfo)
    return copyCurrentInfo


if __name__ == "__main__":
    pickleFile = 'node_typesV2.pkl'
    # previousInfo = addNewLearner(pickleFile, ['SINGLE', 'GRID'])
    loadFile(pickleFile)
