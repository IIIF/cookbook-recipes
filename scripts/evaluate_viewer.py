import sys
import frontmatter
import subprocess
import os
from viewerTests import findFilesToValidate, loadYAML

# - [ ] [🔗 0004 canvas-size](https://preview.iiif.io/cookbook/feature/curation-viewer/recipe/0004-canvas-size/)
if __name__ == "__main__":
    # pass in a argument for the viewer to review
    if len(sys.argv) < 2:
        print("Usage: python evaluate_viewer.py <viewer>")
        sys.exit(1)
    
    # project dir: get the directory above the directory of the script
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    viewer = sys.argv[1]

    files = findFilesToValidate(f"{project_dir}/recipe", ".md")
    ignore = [f"{project_dir}/recipe/index.md", f"{project_dir}/recipe/matrix.md", f"{project_dir}/recipe/all.md", f"{project_dir}/recipe/code.md"]
    
    ignoreFromViewerMatrix = loadYAML(f"{project_dir}/_data/viewer_ignore.yml")
    filename="uv.csv"

    # get git branch and store it in branch
    branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode("utf-8").strip()

    print(f"## Evaluating {viewer}")
    print(f"[Viewer matrix](https://preview.iiif.io/cookbook/{branch}/recipe/matrix/)")
    print()
    print("Checklist:")
    # order by recipe id which is the first part of the filename
    files.sort(key=lambda x: x.split("/")[-2].split("-")[0])
    for recipepath in files:
        # get recipe name from path
        if recipepath not in ignore:
            #print (f"Processing {recipepath}")
            recipe_name = recipepath.split("/")[-2]
            recipe = frontmatter.load(recipepath)

            recipe_id = recipe_name.split("-")[0]

            if recipe.get('viewers', []) is not None and viewer in recipe.get('viewers', []):
                print(f" - [ ] [🔗 {recipe_id} - {recipe.get('title')}](https://preview.iiif.io/cookbook/{branch}/recipe/{recipe_name}/)")