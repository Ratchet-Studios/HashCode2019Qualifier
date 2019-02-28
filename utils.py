def print_tag_count(data):
    for key, value in sorted(data.tags.items(), key=lambda e: e[1][1], reverse=True):
        print(key, value)
