# import Pkg
# Pkg.add("QuartzImageIO")
# Pkg.add("ImageMagick")
# Pkg.add("Images")
using Images

details = rand(1024,768)
save("../temp/gray.png", colorview(Gray, details))
