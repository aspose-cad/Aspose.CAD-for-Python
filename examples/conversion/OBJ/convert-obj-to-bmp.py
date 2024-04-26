import aspose.cad as cad

image = cad.Image.load("file.obj")

cadRasterizationOptions = cad.imageoptions.CadRasterizationOptions()
cadRasterizationOptions.page_height = 800.5
cadRasterizationOptions.page_width = 800.5
cadRasterizationOptions.zoom = 1.5
cadRasterizationOptions.layers = "Layer"
cadRasterizationOptions.background_color = Color.green

options = BmpOptions()
options.vector_rasterization_options = cadRasterizationOptions

image.save("result.bmp", options)
