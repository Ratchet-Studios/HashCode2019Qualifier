import InputOutput
import utils

files = ["a_example.txt",
         "b_lovely_landscape.txt",
         "c_memorable_moments.txt",
         "d_pet_pictures.txt",
         "e_shiny_selfies.txt"]
data = InputOutput.Data("input_data/" + files[0])

slides = utils.create_slides(data.photos)
