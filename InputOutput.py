class Data:
    def __init__(self, filename):
        file = open(filename)
        # Read the file into an array of lines
        lines = [line.rstrip('\n') for line in file]

        # Create a 2D array, split first by each line, then by spaces foreach line
        elements = []
        for line in lines:
            elements.append(entry for entry in line.split(" "))  # convert the strings to integers

        self.num_photos = int(elements[0][0])

        origin = 1
        self.photos = []
        for index in range(origin, origin + self.num_photos):
            self.photos.append([
                elements[index][0].lower(),  # [0] = Horizontal or vertical?, lowercase 'h' or 'v'
                int(elements[index][1]),  # [1] = number of tags, integer
                elements[index][2:]  # [2] = all the tags of that photo, array with lowercase strings
            ])


class Output:
    def __init__(self):
        self.arr1 = []

    def add(self, index, var1, var2, var3):
        self.arr1.insert(index, [var1, var2, var3])

    def write(self, filename):
        f = open(filename, "w")
        # TODO  add formatting required by HashCode for the output
        # Write the 2D array self.arr1's contents to the file, separating first by newlines, then by single spaces
        f.write("\n".join(
            [" ".join(inner_array) for inner_array in self.arr1]
        ))
        f.close()
        print("Successful write to file {} {}".format(filename, "😁"))
