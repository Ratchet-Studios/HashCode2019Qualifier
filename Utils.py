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


def create_slides(photos):
    slides = []  # [([photo ids], {tag ids})] each slide is a tuple ([photo ids], {tag ids})
    vertical_photos = []

    for photo in photos:
        if photo[1] == 'h':
            slides.append(([photo[0]], set(photo[4])))  # tuple containing ([photo ids], {tag ids})
        else:
            vertical_photos.append(photo)

    # vertical photo matchmaking
    index = 0
    while index + 1 < len(vertical_photos):
        slides.append(
            (
                [vertical_photos[index][0], vertical_photos[index + 1][0]],  # the photo ids in this slide
                set(vertical_photos[index][4]).union(set(vertical_photos[index + 1][4]))  # the tags in this slide
            )
        )

        index += 1

    return slides
