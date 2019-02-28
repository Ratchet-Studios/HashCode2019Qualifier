import InputOutput

files = ["a_example.txt",
         "b_lovely_landscape.txt",
         "c_memorable_moments.txt",
         "d_pet_pictures.txt",
         "e_shiny_selfies.txt"]
data = InputOutput.Data("input_data/" + files[0])
"""
data.photos[photo_id][0] - photo id
data.photos[photo_id][1] - 'h' or 'v'
data.photos[photo_id][2] - number of tags of this photo
data.photos[photo_id][3] - a list, all the tags of that photo

data.num_photos - the number of photos in the collection in total

data.tags[my_tag][0] - unique id for each tag
data.tags[my_tag][1] - counter for how often that tag occurs
"""
output = InputOutput.Output()
"""
output.add_slide(index_of_slide_in_show, [photo_id_0, optional_id_1])
output.write(my_output_file_name)
"""

# Testing that data and output actually work:
print("All the tags: ")
for index in range(data.num_photos):
    print(data.photos[index][3])

print("\nThe Dictionary:")
for tag in data.tags:
    print(tag + " : " + str(data.tags[tag]))
