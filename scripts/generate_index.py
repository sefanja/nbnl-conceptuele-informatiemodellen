import os
import yaml

BASE_INPUT_MODELS = "modellen"
BASE_DOCS = "docs"
BASE_OUTPUT_MODELS = os.path.join(BASE_DOCS, "_modellen")

os.makedirs(BASE_OUTPUT_MODELS, exist_ok=True)

index_lines = [
    "---",
    "layout: default",
    "title: Startpagina",
    "---",
    "",
    "# Conceptuele informatiemodellen"
]

def get_model_metadata(yaml_path):
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if "title" in data:
        name = data["title"]
    else:
        name = data["name"]

    version = data.get("version", os.path.basename(os.path.dirname(yaml_path)))

    return name, version


for input_model_dir in sorted(os.listdir(BASE_INPUT_MODELS)):
    input_model_path = os.path.join(BASE_INPUT_MODELS, input_model_dir)
    if not os.path.isdir(input_model_path):
        continue

    model_versions = []
    model_name = input_model_dir  # fallback

    for version in sorted(os.listdir(input_model_path), reverse=True):
        yaml_path = os.path.join(input_model_path, version, "model.yaml")
        gen_md_path = os.path.join(BASE_OUTPUT_MODELS, input_model_dir, version, "index.md")

        if not os.path.exists(yaml_path):
            print(f"Missing YAML: {yaml_path}")
            continue
        if not os.path.exists(gen_md_path):
            print(f"Missing index.md: {gen_md_path}")
            continue

        name, version_in_yaml = get_model_metadata(yaml_path)
        model_name = name

        # Genereer docs/_modellen/<modelnaam>/index.md
        model_dir_path = os.path.join(BASE_OUTPUT_MODELS, input_model_dir)
        os.makedirs(model_dir_path, exist_ok=True)

        model_index_path = os.path.join(model_dir_path, "index.md")
        with open(model_index_path, "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(f'title: "{model_name}"\n')
            f.write("---\n\n")

# Centrale homepage-index schrijven
with open(os.path.join(BASE_DOCS, "index.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(index_lines))
