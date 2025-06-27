import os, subprocess

bo2_path = r"BO2_PATH"
oat_path = r"OAT_PATH"

oat_unlinker = os.path.join(oat_path, "Unlinker.exe")

zone_path = os.path.join(bo2_path, "zone")
zones = [f for f in os.listdir(zone_path) if os.path.isdir(os.path.join(zone_path, f))]

for zone in zones:
    current_zone = os.path.join(zone_path, zone)
    print(f"Current Zone: {zone}")
    files = [f for f in os.listdir(current_zone) if f.endswith(".ff")]
    for i, fil in enumerate(files):
        os.system(f"title Unlinking {fil}... // {i + 1} out of {len(files)} // Zone: {zone}")
        subprocess.run([oat_unlinker, os.path.join(zone_path, fil)], shell=True)