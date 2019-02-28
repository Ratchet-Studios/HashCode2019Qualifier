def calculate_score(set_of_tags_1, set_of_tags_2):
    """
    :param set_of_tags_1: collection of unique strings
    :param set_of_tags_2: same as above
    :return: score based on hashcode scoring
    """
    one_and_two = len(set_of_tags_1.intersection(set_of_tags_2))
    one_not_two = len(set_of_tags_1.difference(set_of_tags_2))
    two_not_one = len(set_of_tags_2.difference(set_of_tags_1))
    return min(one_and_two, one_not_two, two_not_one)
