"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    import pandas as pd
    import os

    archivo_entrada = "files/input/solicitudes_de_credito.csv"
    archivo_salida = "files/output/solicitudes_de_credito.csv"

    datos = pd.read_csv(archivo_entrada, sep=";")

    datos = datos.dropna()
    datos["sexo"] = datos["sexo"].str.lower()
    datos["tipo_de_emprendimiento"] = datos["tipo_de_emprendimiento"].str.lower()

    datos["idea_negocio"] = (
        datos["idea_negocio"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
        .str.strip()
    )

    datos["barrio"] = (
        datos["barrio"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
    )

    def normalizar_fecha(fecha):
        partes = fecha.split("/")
        if len(partes[0]) == 4:
            return f"{partes[2]}/{partes[1]}/{partes[0]}"
        return fecha

    datos["fecha_de_beneficio"] = datos["fecha_de_beneficio"].apply(normalizar_fecha)

    datos["monto_del_credito"] = (
        datos["monto_del_credito"]
        .str.replace(" ", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    datos["línea_credito"] = (
        datos["línea_credito"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
    )

    columnas_unicas = [
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "estrato",
        "comuna_ciudadano",
        "fecha_de_beneficio",
        "monto_del_credito",
        "línea_credito"
    ]
    datos = datos.drop_duplicates(subset=columnas_unicas)

    os.makedirs(os.path.dirname(archivo_salida), exist_ok=True)
    datos.to_csv(archivo_salida, sep=";", index=False)

pregunta_01()
