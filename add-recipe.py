import sys
import os

def make_template(name: str):
    """
    Creates template for new recipe
    """
    return \
        "# " +\
        name +\
        "\n\n" \
        "![Zdjęcie dania](../template.jpg)" \
        "\n\n" \
        "### Składniki" \
        "\n\n\n" \
        "### Przygotowanie" \
        "\n\n\n" \
        "### Gotowanie" \
        "\n\n\n" \
        "### Uwagi" \
        "\n\n" \

def main():
    # Get arguments
    category: str = sys.argv[1]
    name: str = sys.argv[2]

    # Create translating utility to replace diacritics and special characters
    to_replace = "ĄąĆćĘęŁłŃńÓóŚśŹźŻż '"
    repl_with  = "AaCcEeLlNnOoSsZzZz_-"
    translator = str.maketrans(to_replace, repl_with)
    
    # Construct path to recipe, raise error if it already exists
    file_name = category + "/" + name.translate(translator) + ".md"
    if os.path.exists(file_name):
        raise AssertionError("Recipe already exists")

    # Translate category to one in main page, raise error if category is not supported
    category_name: str
    match category:
        case "desserts":
            category_name = "Desery"
        case "meats":
            category_name = "Dania mięsne"
        case "preserves":
            category_name = "Przetwory"
        case "sides":
            category_name = "Dodatki"
        case "soups":
            category_name = "Zupy"
        case "starters":
            category_name = "Przystawki"
        case "vegs":
            category_name = "Dania bezmięsne"
        case _:
            raise AssertionError("Unknown category")
            
    # Create file for recipe using template
    with open(file_name, "w", encoding="utf8") as recipe_file:
        recipe_file.write(make_template(name))

    # Read all lines in README.md
    readme: list[str]
    with open("README.md", "r", encoding="utf8") as readme_file:
        readme = readme_file.readlines()

    # Find position of category
    category_position = [readme.index(ln) for ln in readme if category_name in ln][0]

    # Find position of next empty line in category listing, offset accordingly
    offset_readme = readme[category_position:]
    inserting_position = [offset_readme.index(ln) for ln in offset_readme if ln == "\n"][0]
    inserting_position += category_position
    
    # Insert URL to new recipe and table row in TODO table
    readme.insert(inserting_position, f"- <img src='not-done.thumbnail.jpg' style='height: 1em;'> [{name}]({file_name})\n")
    readme.append(f"|  |  |  | {name} |\n")

    # Replace README.md with new one
    with open("README.md", "w", encoding="utf8") as readme_file:
        readme_file.write("".join(readme))


if __name__ == "__main__": main()
