::usaremos una jaula para realizar una instalacion donde nos indicara todas las depencias.
@ECHO OFF
echo "Iniciando configuracion de entorno"
cd /
cd proyecto 
call C:\\proyecto\\env\\Scripts\\activate.bat
call cmd
echo "entorno cargado"
