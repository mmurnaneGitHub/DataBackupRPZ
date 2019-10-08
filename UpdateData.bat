:: *****************************************************************************
:: UpdateData.bat  3/21/2019 
:: Summary: Tacoma RPZ Vote Data Backup
::
:: Description: 
::   
:: Scheduled Task: Every day @ 5:00 am 
::
:: Path: \\Geobase-win\CED\GADS\R2019\R013\UpdateData\UpdateData.bat
:: *****************************************************************************

Echo Downloading data ... 
    "C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" \\Geobase-win\CED\GADS\R2019\R013\DataBackup\DataBackup.py

::pause
 
