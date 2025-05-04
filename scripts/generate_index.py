import os
import yaml

BASE_DOCS = "docs"
BASE_MODELLEN = "modellen"

index_lines = ["---\n"]
index_lines = ["title: Conceptuele informatiemodellen\n"]
index_lines = ["---\n"]
index_lines = ["\n"]
index_lines = ["# Conceptuele informatiemodellen\n"]

def get_model_metadata(yaml_path):
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    name = data.get("name", os.path.basename(os.path.dirname(os.path.dirname(yaml_path))))
    version = data.get("version", os.path.basename(os.path.dirname(yaml_path)))
    return name, version

for docs_path in sorted(os.listdir(BASE_DOCS)):
    model_docs_path = os.path.join(BASE_DOCS, docs_path)
    if not os.path.isdir(model_docs_path):
        continue

    model_path = os.path.join(BASE_MODELLEN, docs_path)
    if not os.path.exists(model_path):
        continue

    versions = sorted(os.listdir(model_docs_path), reverse=True)
    model_versions = []

    model_name = docs_path  # fallback

    for version_in_path in versions:
        model_yaml_path = os.path.join(model_path, version_in_path, "model.yaml")
        doc_index_path = os.path.join(model_docs_path, version_in_path, "index.md")

        if not os.path.exists(doc_index_path):
            continue

        if os.path.exists(model_yaml_path):
            name, version_in_yaml = get_model_metadata(model_yaml_path)
            model_name = name

            model_versions.append((version_in_path, version_in_path != version_in_yaml)) ## aanname: versie in YAML eindigt bv. op '-draft'
        else:
            model_versions.append((version_in_path, True))

    if not model_versions:
        continue

    index_lines.append(f"### {model_name}\n")
    for v, is_draft in model_versions:
        label = "🚧" if is_draft else "✅"
        index_lines.append(f"- {label} [{v}](./{docs_path}/{v}/)\n")

# Write index.md
index_path = os.path.join(BASE_DOCS, "index.md")
with open(index_path, "w", encoding="utf-8") as f:
    f.write("\n".join(index_lines))
