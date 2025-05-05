import os
import yaml

BASE_INPUT_MODELS = "modellen"
BASE_OUTPUT_MODELS = os.path.join("docs", "_modellen")

os.makedirs(BASE_OUTPUT_MODELS, exist_ok=True)

def get_model_metadata(yaml_path):
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    name = data.get("title") or data.get("name")
    version = data.get("version", os.path.basename(os.path.dirname(yaml_path)))
    return name, version

# Itereer over categorieën (zoals 'registers', 'datadiensten')
for category_dir in sorted(os.listdir(BASE_INPUT_MODELS)):
    category_path = os.path.join(BASE_INPUT_MODELS, category_dir)
    if not os.path.isdir(category_path):
        continue

    category_output_dir = os.path.join(BASE_OUTPUT_MODELS, category_dir)
    os.makedirs(category_output_dir, exist_ok=True)

    # Genereer docs/_modellen/<categorie>/index.md
    category_index_path = os.path.join(category_output_dir, "index.md")
    with open(category_index_path, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f'title: "{category_dir.capitalize()}"\n')
        f.write("---\n\n")
        f.write(f"# {category_dir.capitalize()}\n")

    # Itereer over modellen binnen de categorie
    for model_dir in sorted(os.listdir(category_path)):
        model_path = os.path.join(category_path, model_dir)
        if not os.path.isdir(model_path):
            continue

        model_name = model_dir  # fallback
        for version in sorted(os.listdir(model_path), reverse=True):
            yaml_path = os.path.join(model_path, version, "model.yaml")
            gen_md_path = os.path.join(BASE_OUTPUT_MODELS, category_dir, model_dir, version, "index.md")

            if not os.path.exists(yaml_path):
                print(f"Missing YAML: {yaml_path}")
                continue
            if not os.path.exists(gen_md_path):
                print(f"Missing index.md: {gen_md_path}")
                continue

            model_name, _ = get_model_metadata(yaml_path)
            break  # één versie is genoeg voor de naam

        # Genereer docs/_modellen/<categorie>/<modelnaam>/index.md
        model_output_dir = os.path.join(BASE_OUTPUT_MODELS, category_dir, model_dir)
        os.makedirs(model_output_dir, exist_ok=True)

        model_index_path = os.path.join(model_output_dir, "index.md")
        with open(model_index_path, "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(f'title: "{model_name}"\n')
            f.write(f'parent: "{category_dir.capitalize()}"\n')
            f.write("---\n\n")
            f.write(f"# {model_name}\n")
