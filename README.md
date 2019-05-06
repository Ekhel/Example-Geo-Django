# GeoDjango + Postgis
Python Django Dengan Postgre and Postgis Topology + Sample Data Spatial.

TOOLS YANG DIBUTUHKAN :
1. install Python 3.7 dari (https://www.python.org/downloads/)
2. install PosgreSQL dan Postgis dari (https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
   catatan : Saya Menggunakan Postgre dan Postgis 9.6.12
3. install psycopg2 (untuk menghubungkan Django dan Postgis)
4. install OsGeo dari (https://trac.osgeo.org/osgeo4w/) Pilih yang windowns instaler 32 / 64 bit

-------------------------------------------------------------------------------------------------------------

SETTING 
1. Pull Repository ini.
2. setelah install OsGeo, Pastikan Settingan file settings.py dalam folder project sama dengan Path OsGeo yang kamu install di komputermu 
   OSGEO4W = r"C:\OSGeo4W"
    if '64' in platform.architecture()[0]:
        OSGEO4W += "64"
    assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
    os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
    os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']
 3. buat migrasi DB dengan (python manage.py migrate)
 4. pakai migration dengan (python manage.py makemigrations)
 5. Cek run project (python manage.py runserver)
 
 ---------------------------------------------------------------------------------------------------------------
 
 #DEBUG
 
 1. Jika terjadi debug Periksa Path OsGeo di file settings.py
 2. Cek DB apakah postgis sudah memiliki extension postgis_topology
 
 Regards Michael
