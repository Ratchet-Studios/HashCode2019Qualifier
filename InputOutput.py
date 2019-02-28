class Data:
    def __init__(self, filename):
        file = open(filename)
        # Read the file into an array of lines
        lines = [line.rstrip('\n') for line in file]

        # Create a 2D array, split first by each line, then by spaces foreach line
        elements = []
        for line in lines:
            # TODO: The line below assumes all entries are integers. Is this true?
            elements.append(int(entry) for entry in line.split(" "))  # convert the strings to integers

        # TODO rename the variables as appropriate
        self.rows = elements[0][0]
        self.cols = elements[0][1]
        self.var1 = elements[0][2]
        self.var2 = elements[0][3]
        self.var3 = elements[0][4]

        origin = 1
        self.arr1 = []
        for index in range(origin, origin + self.var1):
        # TODO restructure the line below as appropriate
            self.arr1.append(elements[index])
        origin += self.var1

        self.arr2 = []
        for index in range(origin, origin + self.var2):
            # TODO restructure the line below as appropriate
            self.arr2.append(elements[index])

        # TODO Sort the arrays on proper variables
        self.arr1.sort(key=lambda entry: entry[0])
        self.arr2.sort(key=lambda entry: entry[0])


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
        print("Successful write to file " + filename)