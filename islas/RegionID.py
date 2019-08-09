from enum import Enum, auto

class RegionID(Enum):
    """
    Clase que enumera las regiones previamente definidas en el archivo poligonos.json

    Parámetros
    ----------
    No se necesitan parámetros

    Atributos
    ----------
    Ninguno

    
    Métodos
    -------
    Ninguno
    
    Notas
    -----
    Ninguna
    
    Ejemplos
    --------
    Guardamos el ID en una variable y comparamos su valor    
    >>> id_adelaida = islas.RegionID.adelaida
    >>> id_adelaida == islas.RegionID.adelaida
    True
    >>> id_adelaida == islas.RegionID.guadalupe
    False
    """
    adelaida  = auto()
    alacranes  = auto()
    alcatraz  = auto()
    alijos  = auto()
    angeldelaguarda  = auto()
    animassanlorenzo  = auto()
    asuncion  = auto()
    carmen  = auto()
    cedros  = auto()
    chinchorro  = auto()
    choyudodatil  = auto()
    clarion  = auto()
    coronado  = auto()
    coronadomedio  = auto()
    coronadonorte  = auto()
    coronadosur  = auto()
    cozumel  = auto()
    espiritusanto  = auto()
    estanque  = auto()
    farallondesanignacio  = auto()
    grandesislas  = auto()
    guadalupe  = auto()
    guadalupemorroprieto  = auto()
    guadalupepuntasur  = auto()
    guadalupezapato  = auto()
    holbox  = auto()
    ippbc  = auto()
    ipbccentro  = auto()
    ipbcnorte  = auto()
    ipbcsur  = auto()
    isabel  = auto()
    laal  = auto()
    loreto  = auto()
    loretocarmen  = auto()
    loretocoronado  = auto()
    loretodanzante  = auto()
    loretomonserrat  = auto()
    loretosantacatalina  = auto()
    magdalena  = auto()
    magdalenacreciente  = auto()
    magdalenamaria  = auto()
    magdalenapajaros  = auto()
    magdalenapauquino  = auto()
    magdalenasangil  = auto()
    magdalenasantodomingo  = auto()
    mariacleofas  = auto()
    mariamadre  = auto()
    mariamagdalena  = auto()
    marias  = auto()
    marietas  = auto()
    marietaslarga  = auto()
    marietasredonda  = auto()
    montroseluckenbach  = auto()
    mujeres  = auto()
    natividad  = auto()
    partida  = auto()
    rasa  = auto()
    revillagigedo  = auto()
    salsipuedessanlorenzo  = auto()
    sanbenedicto  = auto()
    sanbenito  = auto()
    sanbenitoeste  = auto()
    sanbenitomedio  = auto()
    sanbenitooeste  = auto()
    sanjeronimo  = auto()
    sanjuanico  = auto()
    sanlorenzo  = auto()
    sanlorenzosanlorenzo  = auto()
    sanmartin  = auto()
    sanpedromartir  = auto()
    sanroque  = auto()
    socorro  = auto()
    tiburon  = auto()
    todossantos  = auto()
    todossantosnorte  = auto()
    todossantossur  = auto()
