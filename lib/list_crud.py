def create_an_empty_list():
    return []


def create_a_list():
    return [1, 2, 3, 4]  


def add_element_to_end_of_list(my_list, element_to_add):
    my_list.append(element_to_add)
    return my_list


def add_element_to_start_of_list(my_list, element_to_add):
    my_list.insert(0, element_to_add)
    return my_list


def add_element_to_start_of_list(my_list, element_to_add):
    my_list.insert(0, element_to_add)
    return my_list


def remove_element_from_start_of_list(my_list):
    if my_list:
        del my_list[0]
    return my_list


def retrieve_first_element_from_list(my_list):
    if my_list:
        return my_list[0]
    return None  


def retrieve_element_from_index(my_list, index):
    if 0 <= index < len(my_list):
        return my_list[index]
  


def retrieve_last_element_from_list(my_list):
    if my_list:
        return my_list[-1]
   

