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


def create_slides(photos, vertical_photos_method=0):
    slides = []  # [([photo ids], {tag ids})] each slide is a tuple ([photo ids], {tag ids})
    vertical_photos = []

    for photo in photos:
        if photo[1] == 'h':
            slides.append(([photo[0]], set(photo[4])))  # tuple containing ([photo ids], {tag ids})
        else:
            vertical_photos.append(photo)

    if vertical_photos_method == 1:

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
    else:
        used_photos = []
        for i in range(len(vertical_photos) - 1):
            if vertical_photos[i] not in used_photos:
                low_score = sys.maxsize
                low_index = -1
                for j in range(i + 1, len(vertical_photos)):
                    if vertical_photos[j] not in used_photos:

                        score = len(vertical_photos[i][3] & vertical_photos[j][3])
                        if score < low_score:
                            low_score = score
                            low_index = j

                slides.append((
                    [vertical_photos[i][0], vertical_photos[low_index][0]],
                    vertical_photos[i][3] | vertical_photos[low_index][3]
                ))
                used_photos.append(vertical_photos[i])
                used_photos.append(vertical_photos[low_index])
    return slides
