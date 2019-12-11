from PIL import Image
import numpy

numpy.random.seed(0)
zz = numpy.random.rand(3000, 4000)
img = Image.fromarray(zz, mode='L')
img.save('../temp/pil_noise.png')