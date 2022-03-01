import datetime
import functools
import pandas as pd

def load(station, var):
    df = pd.read_csv(f"./data/ghcnd/{station}_{var}.csv", parse_dates = ['date'])
    df[var] = df[var] / 10
    return df[['date', var]].set_index('date').interpolate('time')

def combine(station):
    try:
        tavg = load(station, 'tavg').rename(columns={'tavg': 'Tavg'})
    except FileNotFoundError:
        tmax = load(station, 'tmax')
        tmin = load(station, 'tmin')
        df = pd.concat([tmin, tmax], axis=1)
        tavg = ((df['tmax'] + df['tmin']) / 2).to_frame('Tavg')
    return tavg

def _extrapolate(df, year):
    tf0 = datetime.date(year - 10, 1, 1)
    tf1 = datetime.date(year - 1, 12, 31)
    rdf = df[tf0:tf1].reset_index()
    rdf['doy'] = rdf.apply(lambda x: int(datetime.datetime.strftime(x.date, '%j')), axis=1)
    ddf = rdf.set_index('date')
    gdf = ddf.groupby('doy').mean().reset_index()
    gdf['date'] = gdf.apply(lambda x: datetime.datetime.strptime(f"{year}-{int(x.doy)}", "%Y-%j"), axis=1)
    tt0 = datetime.datetime(year, 1, 1)
    tt1 = datetime.datetime(year, 12, 31)
    edf = gdf.set_index('date')[tt0:tt1].drop('doy', axis=1)
    ndf = pd.concat([df, edf])
    return ndf.reset_index().drop_duplicates('date').set_index('date')

def extrapolate(df):
    return functools.reduce(_extrapolate, range(2022, 2032), df)

extrapolate(combine('washingtondc')).to_csv('./data/ghcnd/washingtondc.csv')
extrapolate(combine('liestal')).to_csv('./data/ghcnd/liestal.csv')
extrapolate(combine('kyoto')).to_csv('./data/ghcnd/kyoto.csv')
extrapolate(combine('vancouver')).to_csv('./data/ghcnd/vancouver.csv')
