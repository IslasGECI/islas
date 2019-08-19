import json
import os

from geoambiental import Polygon

from .RegionID import RegionID


class Region(Polygon):
    """
    Clase que representa una región. Estas se construyen a partir de un RegionID.

    Parámetros
    ----------
    `region : RegionID`
        Id de la región que se quiere construir.

    Atributos
    ----------
    `id : string`
        Regresa una cadena con el id del RegionID que se usó para crearla

    `name : string`
        Regresa una cadena con el nombre del RegionID que se usó para crearla

    [Atributos heredados de geoambiental.Polygon]

    
    Métodos
    -------
    [Métodos heredados de geoambiental.Polygon]
    
    Notas
    -----
    Ninguna
    
    Ejemplos
    --------
    Crear la región adeliaida
    >>> region = islas.Region(islas.RegionID.adelaida)
    >>> region.id == islas.RegionID.adelaida.name
    True
    """
    def __init__(self, region: RegionID):
        self._construct_from_poligonosjson(region)

    def _construct_from_poligonosjson(self, region: RegionID):
        datos_islas = self._read_poligonos_json()
        isla = [isla for isla in datos_islas if isla["id"] == region.name][0]
        self._id = isla["id"]
        self._name = isla["nombre"]
        self._lon = isla["Geopoligono"]["lon"]
        self._lat = isla["Geopoligono"]["lat"]

    def _read_poligonos_json(self):
        directorio_actual, _ = os.path.split(__file__)
        direccion_archivo = os.path.join(directorio_actual, "data", "poligonos.json")
        with open(direccion_archivo) as archivo_json:
            datos_islas = json.load(archivo_json)
        return datos_islas

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
