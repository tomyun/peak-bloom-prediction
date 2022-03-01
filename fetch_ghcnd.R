library(rnoaa)

fetch_ghcnd <- function (stationid, var, filename) {
  df <- ghcnd_search(stationid = stationid, var = var,
                     date_min = "1900-01-01", date_max = "2022-02-28")[[1]]
  write.csv(df, filename)
}

# use USW00013743 (Reagan Airport) instead of USW00013743 (National Arboretum)
#fetch_ghcnd("USW00013743", "tavg", "data/ghcnd/washingtondc_tavg.csv")
fetch_ghcnd("USW00013743", "tmax", "data/ghcnd/washingtondc_tmax.csv")
fetch_ghcnd("USW00013743", "tmin", "data/ghcnd/washingtondc_tmin.csv")

#fetch_ghcnd("GME00127786", "tavg", "data/ghcnd/liestal_tavg.csv")
fetch_ghcnd("GME00127786", "tmax", "data/ghcnd/liestal_tmax.csv")
fetch_ghcnd("GME00127786", "tmin", "data/ghcnd/liestal_tmin.csv")

fetch_ghcnd("JA000047759", "tavg", "data/ghcnd/kyoto_tavg.csv")
fetch_ghcnd("JA000047759", "tmax", "data/ghcnd/kyoto_tmax.csv")
fetch_ghcnd("JA000047759", "tmin", "data/ghcnd/kyoto_tmin.csv")

fetch_ghcnd("CA001108395", "tavg", "data/ghcnd/vancouver_tavg.csv")
fetch_ghcnd("CA001108395", "tmax", "data/ghcnd/vancouver_tmax.csv")
fetch_ghcnd("CA001108395", "tmin", "data/ghcnd/vancouver_tmin.csv")
