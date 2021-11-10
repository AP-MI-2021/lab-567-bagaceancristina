def do_undo(undo_list:list, redo_list:list, current_list:list):
    """
    merge un pas inapoi in functionalitatile executate
    :param undo_list: lista undo
    :param redo_list: lista redo
    :param current_list: lista pe care se executa undo
    :return:
    """

    if undo_list:
        redo_list.append(current_list)
        return undo_list.pop()
    return None


def do_redo(undo_list:list, redo_list:list, current_list:list):
    """
    revine la pasul initial in functionalitatile executate
    :param undo_list: lista undo
    :param redo_list: lista redo
    :param current_list: lista pe care se executa redo
    :return:
    """
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(current_list)
        return top_redo

    return None