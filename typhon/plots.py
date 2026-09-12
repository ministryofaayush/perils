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