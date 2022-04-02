import geopandas as gpd
import wikipedia as wk
import re # regex

#  download the dataset
# os.system('curl -f https://raw.githubusercontent.com/aourednik/historical-basemaps/master/geojson/world_900.geojson > world_900.geojson')


# read in the data
gdf = gpd.read_file('world_900.geojson')

# remove nameless countries
gdf = gdf[gdf.NAME.notnull()]

#  filter columns 
gdf = gdf[['NAME','geometry']]

# add summary column
def get_summary(row):

    ''' A function to download the summary from wikipedia '''

    details = ''

    try: details = wk.summary(row.NAME)
    except wk.DisambiguationError:# some items are ambiguous
        try: details =  wk.summary(row.NAME + ' area')
        except wk.PageError: pass
    except: pass

    return re.sub('\([^\)]+\) ','' ,details)


gdf['summary'] = gdf.apply(get_summary, axis=1)

gdf.to_file('processed_data.geojson', driver='GeoJSON')
