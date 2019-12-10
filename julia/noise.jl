using Images

details = rand(4000,3000)
save("../temp/gray.png", colorview(Gray, details))
