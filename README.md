# Shapefile to KML Converter

Este projeto é um conversor de arquivos Shapefile (.shp) para KML (.kml) usando Python, visado principalmente nas bases criadas do SICAR. O código lê um arquivo Shapefile e converte suas geometrias em um formato KML, que pode ser utilizado em aplicações como Google Earth.

## Funcionalidades

- Lê arquivos Shapefile, incluindo os arquivos .shp, .shx, e .dbf.
- Converte geometrias de Shapefile em KML.
- Gera um arquivo KML que pode ser utilizado em software de visualização de mapas.

## Requisitos

Antes de executar o código, você precisa ter o Python 3 instalado. Além disso, você deve instalar as bibliotecas necessárias. As bibliotecas utilizadas são:

- `lxml`: Para manipulação de XML.
- `pykml`: Para criação e manipulação de arquivos KML.
- `pyshp`: Para leitura de arquivos Shapefile.

## Uso 

``python shp2kml.py <caminho_para_o_arquivo.shp> [<caminho_para_o_arquivo.prj>]
``