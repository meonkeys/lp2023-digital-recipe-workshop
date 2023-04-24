#!/usr/bin/python3

# md-recipe-to-json.py - convert Markdown recipe to JSON
# Copyright (C) 2023 Adam Monsen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json
import re
import sys

# Very brittle Markdown to schema.org Recipe JSON converter.

def parse_recipe(recipe_text):
    recipe_dict = {}
    sections = re.split(r'#+\s+(.+)\n+$', recipe_text, flags=re.MULTILINE)
    recipe_dict['name'] = sections[1]
    recipe_dict['description'] = sections[4].strip()
    ingredients_section = sections[6]
    ingredients_list = re.findall(r'\* (.+)', ingredients_section)
    recipe_dict['recipeIngredient'] = [ing.strip() for ing in ingredients_list]
    directions_section = sections[8]
    directions_list = re.findall(r'\d+\.\s+(.+)', directions_section)
    recipe_dict['recipeInstructions'] = [dir.strip() for dir in directions_list]
    return recipe_dict

with open(sys.argv[1]) as fh:
    recipe_text = fh.read()
    recipe_dict = parse_recipe(recipe_text)
    recipe_dict["@context"] = "http://schema.org"
    recipe_dict["@type"] = "Recipe"
    print(json.dumps(recipe_dict))
