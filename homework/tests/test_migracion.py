import os

from ..src.wordcount import main


def test_migracion():

    main()

    if not os.path.exists("data/output/results.tsv"):
        raise FileNotFoundError("El archivo results.tsv no existe.")

    results = {}
    with open("data/output/results.tsv", "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        key, value = line.strip().split("\t")
        results[key] = value

    assert results.get("computational", 0) == "3"
    assert results.get("analytics", 0) == "5"


"""
    Pruebas para la función de migración de datos.
    Verifica que el archivo results.tsv se crea correctamente
    y contiene los conteos esperados para palabras específicas.
    """
