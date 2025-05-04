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
        version_path = os.path.join(model_path, version)
        yaml_path = os.path.join(version_path, "model.yaml")

        if not os.path.exists(yaml_path):
            continue

        name, version_in_yaml = get_model_metadata(yaml_path)
        model_name = name
        is_draft = version != version_in_yaml
        model_versions.append((version, is_draft))

        # Pad voor versiepagina
        output_dir = os.path.join(PAGES_DIR, model_dir, version)
        os.makedirs(output_dir, exist_ok=True)

        # Bestandspad
        md_path = os.path.join(output_dir, "index.md")

        # SVG pad relatief vanaf pagina
        svg_path = "model.drawio.svg"
        has_svg = os.path.exists(os.path.join(BASE_MODELLEN, model_dir, version, "model.drawio.svg"))

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"""---
title: {model_name} {version}
parent: {model_name}
grand_parent: Modellen
nav_order: 1
---

# {model_name} {version}

| Eigenschap | Waarde |
|------------|--------|
| Naam       | {model_name} |
| Versie     | {version} |
| Status     | {"🚧 concept" if is_draft else "✅ stabiel"} |

""")
            if has_svg:
                f.write(f"\n![Diagram]({svg_path})\n")

    if model_versions:
        index_lines.append(f"\n## {model_name}")
        for version, is_draft in model_versions:
            label = "🚧" if is_draft else "✅"
            url = f"/{model_dir}/{version}/"
            index_lines.append(f"- {label} [Versie {version}]({url})")

# Schrijf centrale index
with open(os.path.join(BASE_DOCS, "index.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(index_lines))
