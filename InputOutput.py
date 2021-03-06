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
            
            self.photos[-1].append(
                [self.tags[tag_name][0] for tag_name in self.photos[-1][3]]
            )

            count += 1


class Output:
    """
    output.add_slide(index_of_slide_in_show, [photo_id_0, optional_id_1])
    output.write(my_output_file_name)
    output.photos[0]
    """

    def __init__(self):
        self.slides_photo_ids = []

    def add_slide(self, index, photo_ids):
        self.slides_photo_ids.insert(index, photo_ids)

    def write(self, filename):
        f = open(filename, "w")
        # Write the 2D array self.arr1's contents to the file, separating first by newlines, then by single spaces
        n_slides = len(self.slides_photo_ids)
        
        # print(n_slides)
        f.write(str(n_slides) + "\n")
        
        for photo_ids in self.slides_photo_ids:
            output = ' '.join([str(id) for id in photo_ids])
            
            # print(output)
            f.write(output + "\n")
        
        f.close()
        print("Successful write to file {} {}".format(filename, "😁"))
