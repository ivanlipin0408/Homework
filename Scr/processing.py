def filter_by_state(list_of_dict: list, state="EXECUTED") -> list:
    """Возвращение новых списков словарей по статусу "Выполнено" или "Отменено" """

    filtered_list_of_dict = []
    if state == "CANCELED":
        for dict in list_of_dict:
            if dict.get("state") == "CANCELED":
                filtered_list_of_dict.append(dict)
    else:
        for dict in list_of_dict:
            if dict.get("state") == "EXECUTED":
                filtered_list_of_dict.append(dict)
    print(filtered_list_of_dict)
    return filtered_list_of_dict

