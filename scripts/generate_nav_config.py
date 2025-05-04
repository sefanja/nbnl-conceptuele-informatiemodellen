import os
import yaml

BASE_MODELLEN = "modellen"
DOC_PAGES = "docs/_pages/modellen"
CONFIG_PATH = "docs/_config.yml"

nav_structure = [
    {"Startpagina": "index.md"},
    {"Modellen": []}
]

def get_model_metadata(yaml_path):
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    name = data.get("name", os.path.basename(os.path.dirname(os.path.dirname(yaml_path))))
    version = data.get("version", os.path.basename(os.path.dirname(yaml_path)))
    return name, version

for model_dir in sorted(os.listdir(BASE_MODELLEN)):
    model_path = os.path.join(BASE_MODELLEN, model_dir)
    if not os.path.isdir(model_path):
        continue

    versions = []
    model_name = model_dir  # fallback

    for version in sorted(os.listdir(model_path)):
        yaml_path = os.path.join(model_path, version, "model.yaml")
        gen_doc_path = os.path.join(DOC_PAGES, model_dir, version, "index.md")

        if not os.path.exists(yaml_path) or not os.path.exists(gen_doc_path):
            continue

        name, version_in_yaml = get_model_metadata(yaml_path)
        model_name = name
        versions.append({f"v{version}": f"modellen/{model_dir}/{version}/index.md"})

    if versions:
        nav_structure[1]["Modellen"].append({model_name: versions})

# Bouw de volledige _config.yml met theme en nav
config_data = {
    "title": "NBNL Conceptuele Informatiemodellen",
    "theme": "just-the-docs",
    "baseurl": "/nbnl-conceptuele-informatiemodellen",
    "collections": {
        "pages": {
            "output": true,
            "permalink": "/:path/"
        },
    },
    "include": ["**/*.svg"],
    "nav": nav_structure
}

with open(CONFIG_PATH, "w", encoding="utf-8") as f:
    yaml.dump(config_data, f, sort_keys=False, allow_unicode=True)
