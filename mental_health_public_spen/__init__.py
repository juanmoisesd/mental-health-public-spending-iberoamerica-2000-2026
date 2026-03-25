"""Gasto Público en Salud Mental en Iberoamérica (2000-2026): Base de Datos por Paí
DOI:https://github.com/juanmoisesd/mental-health-public-spending-iberoamerica-2000-2026"""
__version__="1.0.0"
import pandas as pd,io,requests
def load_data(f=None):
  rid="https://github.com/juanmoisesd/mental-health-public-spending-iberoamerica-2000-2026".split(".")[-1];m=requests.get("https://zenodo.org/api/records/"+rid,timeout=30).json();csvs=[x for x in m.get("files",[]) if x["key"].endswith(".csv")]
  if not csvs:raise ValueError("No CSV")
  tgt=next((x for x in csvs if f and x["key"]==f),csvs[0]);return pd.read_csv(io.StringIO(requests.get(tgt["links"]["self"],timeout=60).text))
def cite():return "de la Serna, Juan Moisés (2025). Gasto Público en Salud Mental en Iberoamérica (2000-2026): B"
def info():print("DOI: https://github.com/juanmoisesd/mental-health-public-spending-iberoamerica-2000-2026\nGitHub: https://github.com/juanmoisesd/mental-health-public-spending-iberoamerica-2000-2026")
