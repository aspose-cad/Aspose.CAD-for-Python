![PyPI](https://img.shields.io/pypi/v/aspose-ca.svg?label=PyPI) ![PyPI](https://img.shields.io/pypi/dm/aspose-cad.svg?label=PyPI%20downloads) ![GitHub](https://img.shields.io/github/license/aspose-cad/Aspose.CAD-for-Python)

# CAD/BIM Drawings conversion and publish API for Python

[Aspose.CAD for Python](https://products.aspose.com/cad/python) is a standalone class library with Aspose.CAD for .NET under the hood to enhance applications to process, modify, render and publish CAD and BIM drawings without requiring AutoCAD or any other rendering workflow. The CAD Class Library allows high quality [conversion of DWG, DWF, DWFX, DWT, DGN, STL, DXB, OBJ, STL, CF2, IGES, IFC, PLT, and DXF](https://docs.aspose.com/cad/python/supported-file-formats/) files, layouts, and layers to PDF & raster image formats.

## CAD File Processing Features

- Supports the latest versions of DWG, DWF, DWFX, DXB, DWT, DGN, STL, OBJ, STL, CF2, IGES, IFC, DXB, PLT & DXF formats.
- Convert [CAD to PDF](https://docs.aspose.com/cad/python/converting-cad-drawings-to-pdf-and-raster-image-formats/).
- Convert CAD to images.
- Track files processing progress.
- Manipulate drawing entities and blocks.
- Select and convert specific layouts of CAD drawings.
- Select and convert specific layers of CAD drawings.
- [Adjust CAD drawing size before rendering](https://docs.aspose.com/cad/python/adjusting-cad-drawing-size/).

## New Features & Enhancements ![Version 22.2](https://img.shields.io/badge/nuget-v22.2-blue)

- Ability to export to the `OBJ` file format.
- Support for HoloLens 2.
- Support for the AutoCAD Plotter Configuration (`PC3`) files.

Please visit [Aspose.CAD for Python 22.2 - Release Notes](https://docs.aspose.com/cad/python/aspose-cad-for-python-22-2-release-notes/) for the detailed notes.

## Read CAD and BIM Formats

**AutoCAD:** DWG, DWT, DXF, PC3
**MicroStation:** DGN
**Other:** STL, DXB, IGES, DWF, DWFX, IFC, PLT, CF2, HPGL

## Save and publsih drawings As

**Fixed Layout:** PDF
**Vector Images** SVG, WMF, EMF, HTML5
**Raster Images:** PNG, BMP, TIFF, JPEG, GIF, PSD, JP2, PSD, WEBP, DICOM

## Read & Write

**CAD:** DXF, DWF, DWFX, FBX
**The Advanced Visualizer:** OBJ
(Write features is partially supported.)

## Platform Independence

Aspose.CAD for Python supports Python version 3.x. It supports any 32-bit or 64-bit operating system, this includes but is not limited to, Microsoft Windows desktop (XP, Vista, 7, 8, 10), Microsoft Windows Server (2003, 2008, 2012), Microsoft Azure, Linux (Ubuntu, OpenSUSE, CentOS, and others), and Mac OS X.

## Getting Started
Simply run ```pip install aspose-cad``` from the Console to fetch the package.
If you already have Aspose.CAD for Python and want to upgrade the version, please run ```pip install --upgrade aspose-cad``` to get the latest version.

You can run the following snippets in your environment to see how Aspose.CAD works, or check out the [GitHub Repository](https://github.com/aspose-python/Aspose.CAD-for-Python) or [Aspose.CAD for Python Documentation](https://docs.aspose.com/cad/python/) for other common use cases.

## Export DXF to PDF using C# Code

```python
import aspose.cad as cad

cadImage = cad.image.load("drawing.dxf");

rasterizationOptions = cad.CadRasterizationOptions();
pdfOptions = cad.PdfOptions();

cadImage.Save("output.pdf", pdfOptions);
```

[Home](https://www.aspose.com/) | [Product Page](https://products.aspose.com/cad/python) | [Docs](https://docs.aspose.com/cad/python/) | [Demos](https://products.aspose.app/cad/family) | [API Reference](https://apireference.aspose.com/cad/python) | [Examples](https://github.com/aspose-cad/Aspose.CAD-for-Python) | [Blog](https://blog.aspose.com/category/cad/)| [Search](https://search.aspose.com/) | [Free Support](https://forum.aspose.com/c/cad) | [Temporary License](https://purchase.aspose.com/temporary-license)
