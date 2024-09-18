from lxml import etree
from pykml.factory import KML_ElementMaker as KML
import shapefile
import sys
import os


def create_reader(shp_fname):
    return shapefile.Reader(shp_fname)


def read_projection(prj_fname):
    with open(prj_fname, 'r') as prj_file:
        return prj_file.read()


def create_kml_root():
    doc = KML.kml()
    document = KML.Document()
    doc.append(document)
    return doc, document


def main(args):
    shp_fname = args[1]
    prj_fname = args[2]

    if not os.path.isfile(shp_fname):
        print(f"Shapefile {shp_fname} not found.")
        return 1

    base_name, _ = os.path.splitext(shp_fname)
    if not (os.path.isfile(f"{base_name}.shx") and os.path.isfile(f"{base_name}.dbf")):
        print(f"Related files for {shp_fname} are missing.")
        return 1

    reader = create_reader(shp_fname)

    if prj_fname and os.path.isfile(prj_fname):
        projection = read_projection(prj_fname)
        print("Projection info:", projection)

    for idx, shapeRec in enumerate(reader.shapeRecords()):
        doc, document = create_kml_root()

        name = ''
        for i in range(len(shapeRec.record)):
            name += f'{shapeRec.record[i]}|'

        points = shapeRec.shape.points

        if points[0] != points[-1]:
            points.append(points[0])

        coordinates = ' '.join([f'{p[0]},{p[1]}' for p in points])

        placemark = KML.Placemark(
            KML.name(name),
            KML.MultiGeometry(
                KML.Polygon(
                    KML.outerBoundaryIs(
                        KML.LinearRing(
                            KML.coordinates(coordinates)
                        )
                    )
                )
            )
        )

        document.append(placemark)

        with open(f'{shapeRec.record[2]}.kml', 'wb') as f:
            f.write(etree.tostring(doc, pretty_print=True))

        print(f"KML file saved as {shapeRec.record[2]}.kml")

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))