import aspose.cad as cad

image = cad.Image.load("file.dwf")

cadRasterizationOptions = cad.imageoptions.CadRasterizationOptions()
cadRasterizationOptions.page_height = 800.5
cadRasterizationOptions.page_width = 800.5
cadRasterizationOptions.zoom = 1.5
cadRasterizationOptions.layers = "Layer"
cadRasterizationOptions.background_color = Color.green

options = ThreeDSOptions()
options.vector_rasterization_options = cadRasterizationOptions

image.save("result.3ds", options)
