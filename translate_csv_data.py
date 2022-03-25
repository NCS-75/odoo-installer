# Small script to create i18n_extra/fr.po file with french translations for CSV data
# in listed MODULES
import pathlib
import pyexcel

CURRENT_DIR = pathlib.Path(__file__).resolve().parent
PREFIX = "__installer__."
MODULES = ["crm_installer"]

for module in MODULES:
    all_data = {}
    data_dir = CURRENT_DIR / module / "data"
    i18n_extra_dir= CURRENT_DIR / module / "i18n_extra"
    i18n_extra_dir.mkdir(parents=True, exist_ok=True)
    fr_po_path = i18n_extra_dir / "fr.po"

    for file in data_dir.iterdir():
        if not file.is_file() or file.suffix != ".csv":
            continue
        model = file.stem.split("_data")[0].replace("_", ".")
        data = pyexcel.get_records(file_name=str(file))
        all_data[model] = data

    with open(fr_po_path, "w", newline="") as fr_po:
        # Erase content
        fr_po.seek(0)
        fr_po.truncate()
        # Add content
        for model, data in all_data.items():
            for d in data:
                text = f"""
#. module: {module}
#: model:{model},name:{PREFIX}{d["xmlid"]}
msgid "{d["name"]}"
msgstr ""
"""
                fr_po.write(text)
