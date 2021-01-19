import click

import geopandas as gpd

from utils import CRS, EXTRA_DATA_INDEX, combine_data_frames, import_geometry, import_data
"""
converts shapefile to geojson
and adds extra data
"""


@click.command()
@click.option("--index", default="index")
@click.option(
    "--output", default="out.geojson", type=click.Path(dir_okay=False)
)
@click.option("--extra", type=click.File("r"))
@click.argument("geometry", type=click.Path(dir_okay=False))
def convert_geometry(index, output, extra, geometry):
    geo_data_frame = import_geometry(geometry, index_name=index)
    geo_data_frame = geo_data_frame.to_crs(crs=CRS)

    if extra:
        extra_data_frame = import_data(extra, index_name=EXTRA_DATA_INDEX)
        geo_data_frame = geo_data_frame.merge(extra_data_frame, left_on=index, right_on=EXTRA_DATA_INDEX)

    geo_data_frame.to_file(output, driver="GeoJSON")


if __name__ == "__main__":
    convert_geometry()
