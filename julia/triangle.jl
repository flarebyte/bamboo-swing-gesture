import Pkg
Pkg.add("QuartzImageIO")
Pkg.add("ImageMagick")
Pkg.add("Images")

using Images
save("../temp/gray.png", colorview(Gray, rand(256,256)))
