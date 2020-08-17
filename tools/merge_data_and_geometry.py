import click
import functools

import pandas as pd
import geopandas as gpd

from utils import CRS, combine_data_frames, import_geometry, import_data


"""
merges data (CSV) and geometry (GeoJSON) into a single file
"""


@click.command()
@click.option("--geometry-index", default="index")
@click.option("--data-index", default="index")
@click.option("--output", default="out.geojson", type=click.Path(dir_okay=False))
@click.argument("geometry", type=click.File("r"))
@click.argument("data", nargs=-1, type=click.File("r"))
def merge_data_and_geometry(geometry_index, data_index, output, geometry, data):
    geo_data_frame = import_geometry(geometry, index_name=geometry_index)
    data_frame = functools.reduce(
        lambda a, b: combine_data_frames(a, b),
        map(lambda x: import_data(x, index_name=data_index), data),
    )

    # (have to recast to gdf b/c combining gdf w/ df can result in df)
    merged_geo_data_frame = gpd.GeoDataFrame(
        combine_data_frames(geo_data_frame, data_frame),
        geometry=geo_data_frame.geometry,
        crs=CRS,
    )
    merged_geo_data_frame.to_file(output, driver="GeoJSON")


if __name__ == "__main__":
    merge_data_and_geometry()
