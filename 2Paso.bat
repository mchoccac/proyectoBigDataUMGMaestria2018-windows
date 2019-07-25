::usaremos una jaula para realizar una instalacion donde nos indicara todas las depencias.
@ECHO OFF
echo "Iniciando configuracion de entorno"
cd /
mkdir proyecto
cd proyecto 
pip install virtualenv
virtualenv env
call C:\\proyecto\\env\\Scripts\\activate.bat
echo "Instalando depencias"
::instalar estas depencias hasta en este punto te saldra (env) c:\proyecto
pip install numpy
pip install pandas
pip install scikit-learn
pip install matplotlib==1.5.1
pip install scipy
pip install nltk
pip install networkx==1.11
pip install tweepy==3.3.0
pip install Pillow
pip install opencv-python
pip install seaborn
pip install shapely
pip install pysal
pip install Fiona
pip install descartes
pip install basemap
pip install textblob
pip install ggplot
pip install folium
pip install plotly
pip install arrow
echo "Terminado"
call cmd
pause
