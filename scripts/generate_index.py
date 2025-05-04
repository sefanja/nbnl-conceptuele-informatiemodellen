import os
import yaml

BASE_DOCS = "docs"
BASE_MODELLEN = "modellen"
PAGES_DIR = os.path.join(BASE_DOCS, "_pages")

os.makedirs(PAGES_DIR, exist_ok=True)

index_lines = [
    "---",
    "layout: default",
    "title: Startpagina",
    "nav_order: 1",
    "---",
    "",
    "# Conceptuele informatiemodellen",
    "",
    "Een overzicht van alle beschikbare modellen:"
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

    model_versions = []
    model_name = model_dir  # fallback

    for version in sorted(os.listdir(model_path), reverse=True):
        yaml_path = os.path.join(model_path, version, "model.yaml")
        gen_md_path = os.path.join(PAGES_DIR, model_dir, version, "index.md")

        if not os.path.exists(yaml_path) or not os.path.exists(gen_md_path):
            continue

        name, version_in_yaml = get_model_metadata(yaml_path)
        model_name = name
        is_draft = version != version_in_yaml
        model_versions.append((version, is_draft))

    # Alleen doorgaan als er geldige versies zijn
    if not model_versions:
        continue

    # Tussenpagina voor dit model (alleen navigatiecontainer)
    model_page_dir = os.path.join(PAGES_DIR, model_dir)
    os.makedirs(model_page_dir, exist_ok=True)
    with open(os.path.join(model_page_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write(f"""---
title: {model_name}
parent: Modellen
has_children: true
nav_order: 1
---

<!-- Navigatiecontainer voor {model_name} -->
""")

    # Linkjes in centrale index
    index_lines.append(f"\n## {model_name}")
    for version, is_draft in model_versions:
        label = " 🚧" if is_draft else ""
        url = f"{model_dir}/{version}/"
        index_lines.append(f"- [v{version}]({url}){label}")

# Centrale indexpagina schrijven
with open(os.path.join(BASE_DOCS, "index.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(index_lines))
