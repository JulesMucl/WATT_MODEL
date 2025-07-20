import xml.etree.ElementTree as ET
from datetime import datetime
from typing import List, Tuple, Optional
import matplotlib.pyplot as plt


def read_tcx_trackpoints(filepath: str) -> List[dict]:
    """
    Extrait tous les trackpoints d'un fichier TCX sous forme de dictionnaire :
    {'altitude': ..., 'time': ...}

    :param filepath: Chemin du fichier TCX
    :return: Liste de dicts contenant 'altitude' (float) et 'time' (datetime)
    """
    ns = {'tcx': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'}
    
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
    except (ET.ParseError, FileNotFoundError) as e:
        print(f"Erreur lors de la lecture du fichier TCX : {e}")
        return []

    trackpoints = []
    for tp in root.findall('.//tcx:Trackpoint', ns):
        ele = tp.find('tcx:AltitudeMeters', ns)
        time = tp.find('tcx:Time', ns)

        if ele is not None and ele.text and time is not None and time.text:
            try:
                trackpoints.append({
                    "altitude": float(ele.text),
                    "time": datetime.fromisoformat(time.text.replace("Z", "+00:00"))
                })
            except ValueError:
                continue

    return trackpoints


def compute_dplus(altitudes: List[float]) -> float:
    """
    Calcule le dénivelé positif total (D+).

    :param altitudes: Liste d'altitudes
    :return: D+ total en mètres
    """
    dplus = sum(max(altitudes[i] - altitudes[i - 1], 0) for i in range(1, len(altitudes)))
    return round(dplus, 1)


def plot_elevation(trackpoints: List[dict]):
    """
    Affiche un graphique altitude vs temps.

    :param trackpoints: Liste de dicts contenant 'altitude' et 'time'
    """
    if not trackpoints:
        print("Aucun point à tracer.")
        return

    altitudes = [tp["altitude"] for tp in trackpoints]
    times = [tp["time"] for tp in trackpoints]
    t0 = times[0]
    elapsed_minutes = [(t - t0).total_seconds() / 60 for t in times]

    plt.figure(figsize=(12, 5))
    plt.plot(elapsed_minutes, altitudes, linewidth=1.5)
    plt.title("Profil altimétrique")
    plt.xlabel("Temps écoulé (min)")
    plt.ylabel("Altitude (m)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
