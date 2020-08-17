import click
import functools

import pandas as pd
import geopandas as gpd

from utils import CRS, import_geometry, combine_data_frames

"""
combines several geojson files into a single file
"""


@click.command()
@click.option("--index", default="index")
@click.option("--output", default="out.geojson", type=click.Path(dir_okay=False))
@click.argument("geometry", nargs=-1, type=click.File("r"))
def combine_geometry(index, output, geometry):
    geo_data_frame = functools.reduce(
        lambda a, b: combine_data_frames(a, b),
        map(lambda x: import_geometry(x, index_name=index), geometry),
    )
    # geo_data_frame = geo_data_frame.to_crs(CRS)
    geo_data_frame.to_file(output, driver="GeoJSON")


if __name__ == "__main__":
    combine_geometry()
