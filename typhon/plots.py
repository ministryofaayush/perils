import pandas as pd
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib import pyplot as plt

def EventPlot(df: pd.DataFrame, event_id: str):
    """ Function to plot the storm tracks for a given event ID."""
    event_df = df[df['SID'] == event_id].copy()
    
    fig = plt.figure(figsize=(16, 4))
    ax = plt.axes(projection=ccrs.PlateCarree())
    
    # Scatter points
    sc = ax.scatter(event_df['LON'], event_df['LAT'], c=event_df['USA_WIND'], cmap='jet', s=60, alpha=0.8, transform=ccrs.PlateCarree())
    
    # coastlines and country borders
    ax.coastlines(resolution='110m', linewidth=0.8)
    ax.add_feature(cfeature.BORDERS, linewidth=0.5)
    
    # gridlines lat lon
    gl = ax.gridlines(draw_labels=True, linestyle='--', alpha=0.5)
    gl.top_labels = False; gl.right_labels = False

    plt.colorbar(sc, ax=ax, label='Max Sustained Wind (kt)')
    plt.title(f'Storm Track for Event ID: {event_id}')
    plt.show()


def RegionalStormTracks(Region, tracks_through_area, area_name):
    """ Plot storm tracks that intersect a given region. """

    fig, ax = plt.subplots(figsize=(7, 3))

    # Area boundary
    Region.boundary.plot(ax=ax, color='black', linewidth=1, label=area_name)

    # Tracks that passed through
    tracks_through_area.plot(ax=ax, color='#120A8F', linewidth=0.5, alpha=0.7, label='Storm Tracks')

    # Zoom to a bit around the area so tracks aren't lost in a huge global view
    minx, miny, maxx, maxy = Region.total_bounds
    buffer = 1  # degrees
    ax.set_xlim(minx - buffer, maxx + buffer)
    ax.set_ylim(miny - buffer, maxy + buffer)

    ax.set_title(f'{len(tracks_through_area)} storm tracks passing through {area_name}')
    ax.set_xlabel('Longitude'); ax.set_ylabel('Latitude')
    plt.legend()
    plt.show()