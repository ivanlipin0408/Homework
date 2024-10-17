def filter_by_state(list_of_dict: list[dict], state="EXECUTED") -> list[dict]:
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


def sort_by_date(list_of_dict: list[dict], sorting_method="Reverse=True"):
    sorted_list_of_dict = []


    print(sorted_list_of_dict)
    return sorted_list_of_dict

