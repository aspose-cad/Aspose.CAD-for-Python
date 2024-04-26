import aspose.cad as cad

image = cad.Image.load("file.stl")

cadRasterizationOptions = cad.imageoptions.CadRasterizationOptions()
cadRasterizationOptions.page_height = 800.5
cadRasterizationOptions.page_width = 800.5
cadRasterizationOptions.zoom = 1.5
cadRasterizationOptions.layers = "Layer"
cadRasterizationOptions.background_color = Color.green

options = U3dOptions()
options.vector_rasterization_options = cadRasterizationOptions

image.save("result.u3d", options)
