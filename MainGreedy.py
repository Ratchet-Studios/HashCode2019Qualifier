import InputOutput
import utils

files = ["a_example.txt",
         "b_lovely_landscapes.txt",
         "c_memorable_moments.txt",
         "d_pet_pictures.txt",
         "e_shiny_selfies.txt"]
data = InputOutput.Data("input_data/" + files[2])

slides = utils.create_slides(data.photos, 1)

slideshow = [slides.pop(0)]

while slides:  # while slides is not empty
    best_slide_index = 0
    best_score = utils.calculate_score(slideshow[-1][1], slides[0][1])
    for i in range(1, len(slides)):
        score = utils.calculate_score(slideshow[-1][1], slides[i][1])
        if score > best_score:
            best_slide_index = i
            best_score = score
    
    slideshow.append(slides.pop(best_slide_index))
    print(' '.join([str(x) for x in slideshow[-1][0]]))

output = InputOutput.Output()

for slide in slideshow:
    output.add_slide(-1, slide[0])

output.write("out2.txt")
