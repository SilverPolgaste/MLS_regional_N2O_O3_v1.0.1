# Dynamics-of-stratospheric-N2O-in-lower-stratosphere-based-on-the-Aura-satellite-data
Repository for code used in the data analysis of the article mentioned in the repository title.

Includes descriptions for code used in the article mentioned in the title in the processing and analysis of N2O and O3 data.

Additional information: [Silver Põlgaste](mailto:silver.polgaste@ut.ee)

Nitrous oxide data from [MLS/Aura Level 2 Nitrous Oxide (N2O) Mixing Ratio V005 (ML2N2O)](https://disc.gsfc.nasa.gov/datasets/ML2N2O_005/summary?keywords=aura%20n2o)

Ozone data from [MLS/Aura Level 2 Ozone (O3) Mixing Ratio V005 (ML2O3)](https://disc.gsfc.nasa.gov/datasets/ML2O3_005/summary?keywords=aura%20o3)

Data from 2005-2021
## Descriptions of files and data included


The names of the location identifiers in the code differ from Table S1, the following table includes the corresponding loctations:

| Index | Location                  | Center latitude | Center longitude | Latitude zone | Code identifier    |
| ----- | ------------------------- | --------------- | ---------------- | ------------- | ------------------ |
| 1     | Bashkortostan             | 55.5            | 55.8             | NH            | `bashkortostan`    |
| 2     | California                | 38              | -121.7           | NH            | `california`       |
| 3     | Colombia                  | 6.67            | -75.67           | Tropics       | `colombia`         |
| 4     | Congo                     | 1.35            | 17.46            | Tropics       | `kongo`            |
| 5     | Estonia                   | 58.4            | 26.5             | NH            | `estonia`          |
| 6     | Finland                   | 68              | 24.2             | NH            | `finland`          |
| 7     | Florida                   | 26.4            | -81.65           | Tropics       | `florida`          |
| 8     | France                    | 47.3            | 2.2              | NH            | `france`           |
| 9     | French Guiana             | 5.05            | -52.55           | Tropics       | `french_guiana`    |
| 10    | French Pyrenees/Catalonia | 42.7            | 1                | NH            | `catalonia`        |
| 11    | Iceland E                 | 64.3            | -15.48           | NH            | `iceland_e`        |
| 12    | Iceland W                 | 64.8            | -22.9            | NH            | `iceland_w`        |
| 13    | Kalimantan                | 5.32            | 115.66           | Tropics       | `brunei`           |
| 14    | Khabarovsk                | 48.5            | 135.4            | NH            | `khabarovsk`       |
| 15    | Kyrgyzstan                | 41.85           | 75.4             | NH            | `kyrgyzstan`       |
| 16    | Montana                   | 45.55           | -111.3           | NH            | `bozeman`          |
| 17    | Morocco                   | 35.22           | -5.7             | NH            | `morocco`          |
| 18    | Mukhrino                  | 60.9            | 68.72            | NH            | `mukhrino`         |
| 19    | Myanmar                   | 20.63           | 96.9             | Tropics       | `myanmar`          |
| 20    | New Zealand N             | -37.4           | 175.55           | SH            | `nz_n`             |
| 21    | New Zealand S             | -46.55          | 168.43           | SH            | `nz_s`             |
| 22    | Pantanal                  | -16.5           | -56.73           | Tropics       | `pantanal`         |
| 23    | Peruvian Amazon           | -3.85           | -73.35           | Tropics       | `quistococha`      |
| 24    | Romania                   | 47.25           | 25.35            | NH            | `romania`          |
| 25    | Santa Catarina            | -28.55          | -48.81           | Tropics       | `florianopolis`    |
| 26    | Southern Québec           | 45.12           | -74.2            | NH            | `huntingdon`       |
| 27    | Taiwan                    | 22.2            | 120.85           | Tropics       | `taiwan`           |
| 28    | Tarapoto                  | -6.47           | -76.38           | Tropics       | `tarapoto`         |
| 29    | Tasmania                  | -41.5           | 145.5            | SH            | `tasmania`         |
| 30    | Tierra del Fuego          | -54.74          | -67.87           | SH            | `tierra_del_fuego` |
| 31    | Uganda 1                  | 1.2             | 29.95            | Tropics       | `uganda_n`         |
| 32    | Uganda 2                  | -1.2            | 29.95            | Tropics       | `uganda_s`         |
| 33    | Uganda 3                  | 0.93            | 34               | Tropics       | `uganda_e`         |
| 34    | Wales                     | 53              | -3.8             | NH            | `wales`            |
| 35    | Xochimilco, Mexico City   | 19.3            | -99.1            | Tropics       | `mexico`           |

**latitude_spreads.ipynb** - includes code for calculating the mean N2O and O3 concentrations and their 95% CIs per location for the entire study period and plotting the data (as seen in Fig. 1 of the paper)

**seasonal.ipynb** - detrends per-site N2O and O3 time series, then computes and plots seasonal cycles (monthly means ± 95% CI) for each latitude zone and altitude (Fig. 3 of the paper).

**single_locations.ipynb** - similar process to **seasonal.ipynb**, but plots seasonal cycles for each location separately (as seen on Figs. S2-S4)


Descriptions by folder

### correlations

Includes data and code for evaluating and plotting the relationship of concurrently measured N2O and O3 concentrations

*correlations.ipynb* - combines N2O and O3 data (found in the **data** folder's subfolders), calculates Pearson's r2 and p-values; plots the data along with trendlines as seen in Figs. 4 and S5-S7.

#### data

**code_examples** includes examples of python scripts used to produce the data found in the **data_n2o** and **data_o3** folders used in the *correlations.ipynb* Jupyter Notebook. Level 2 satellite data not included as an upload, accessible through the links close to the readme's beginning.


### trends

Code and data for finding long-term trends in N2O and O3 concentrations. 

**data_cleaning.ipynb** - Jupyter Notebook for cleaning csv files derived from MLS data. Note that the files under the **data** folder **have already been processed** in this way

**lat_zones.ipynb** - calculates the zonal (defined in the artice) mean monthly N2O and O3 concentrations at each altitude and plots them on a timeline. Also includes Mann-Kendall tests for each case.

**monthly_averages.ipynb** - Jupyter Notebook for calculating the mean monthly concentrations of each location's N2O/O3 data and combining them into single files per gas/altitude combination. Combined files available under the **monthly_averages** subfolder.



#### monthly_averages

Includes csv files with the per location monthly average N2O and O3 concentrations. One file for each gas/altitude combination. 

#### data_processing 
Folder includes example files used for initial data extraction from Level 2 MLS data
