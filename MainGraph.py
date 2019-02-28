import InputOutput
import utils

files = ["a_example.txt",
         "b_lovely_landscape.txt",
         "c_memorable_moments.txt",
         "d_pet_pictures.txt",
         "e_shiny_selfies.txt"]
data = InputOutput.Data("input_data/" + files[0])

slides = []  # [([photo ids], {tag ids})] each slide is a tuple ([photo ids], {tag ids})
vertical_photos = []

for photo in data.photos:
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
