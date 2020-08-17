import click

import geopandas as gpd

from utils import CRS, combine_data_frames, import_geometry


"""
converts shapefile to geojson
"""


@click.command()
@click.option("--index", default="index")
@click.option("--output", default="out.geojson", type=click.Path(dir_okay=False))
@click.argument("geometry", type=click.Path(dir_okay=False))
def convert_geometry(index, output, geometry):
    geo_data_frame = import_geometry(geometry, index_name=index)
    geo_data_frame = geo_data_frame.to_crs(crs=CRS)
    geo_data_frame.to_file(output, driver="GeoJSON")


if __name__ == "__main__":
    convert_geometry()
