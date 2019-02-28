class Data:
    """
    data.photos[photo_id][0] - photo id
    data.photos[photo_id][1] - 'h' or 'v'
    data.photos[photo_id][2] - number of tags of this photo
    data.photos[photo_id][3] - a list, all the tags of that photo

    data.num_photos - the number of photos in the collection in total

    data.tags[my_tag][0] - unique id for each tag
    data.tags[my_tag][1] - counter for how often that tag occurs
    """

    def __init__(self, filename):
        file = open(filename)
        # Read the file into an array of lines
        lines = [line.rstrip('\n') for line in file]

        # Create a 2D array, split first by each line, then by spaces foreach line
        elements = []
        for line in lines:
            elements.append(list(entry for entry in line.split(" ")))  # convert the strings to integers

        self.num_photos = int(elements[0][0])

        origin = 1
        self.photos = []
        count = 0
        self.tags = {}
        tag_id = 0
        for index in range(origin, origin + self.num_photos):
            self.photos.append([
                count,  # [0] = id of the photo
                elements[index][0].lower(),  # [1] = Horizontal or vertical?, lowercase 'h' or 'v'
                int(elements[index][1]),  # [2] = number of tags, integer
                elements[index][2:]  # [3] = all the tags of that photo, array with lowercase strings
            ])
            for tag in self.photos[index - origin][3]:  # for all the tags in our current photo
                if tag in self.tags:  # if the tag already exists, increment its count
                    self.tags[tag][1] += 1
                else:
                    self.tags[tag] = [tag_id, 1]
                tag_id += 1

            count += 1


class Output:
    """
    output.add_slide(index_of_slide_in_show, [photo_id_0, optional_id_1])
    output.write(my_output_file_name)
    """

    def __init__(self):
        self.photos = []

    def add_slide(self, index, photo_ids):
        self.photos.insert(index, photo_ids)

    def write(self, filename):
        f = open(filename, "w")
        # Write the 2D array self.arr1's contents to the file, separating first by newlines, then by single spaces
        str_photos = []
        for photo_ids in self.photos:
            str_photos.append(" ".join(str(photo_ids)))
        output = str(sum(self.photos))
        for string in str_photos:
            output += "\n" + string
        f.write(output)

        # f.write(str(sum(self.photos)) +
        #         "\n".join(
        #             [" ".join(str(inner_array)) for inner_array in self.photos]
        #         ))
        f.close()
        print("Successful write to file {} {}".format(filename, "😁"))
