# Workshop 🍲

The Immortal Cookbook. By Adam Monsen.

LibrePlanet 2023 Workshop.

Presented Monday, April 24, 2023.

## Roll call 🎙️

* Confirm everyone can see/hear/be heard.
* Thank you LibrePlanet staff and volunteers!
* Participant self-intros.

## Fine print ⚖️

This workshop is Copyright ©2023 Adam Monsen, available for use and reuse under the following license(s):

* [GNU Free Documentation License v1.3 or any later version](https://www.gnu.org/licenses/fdl-1.3.html)
* [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)

Any and all original code associated with this workshop is availble under the following license(s):

* [GNU Affero General Public License v3 or any later version](https://www.gnu.org/licenses/agpl-3.0.html)

Some full license texts are available under `licenses/`.

## Setup 🗃️

I hope you're hungry, this is going to be delicious!

* We will walk through this `workshop.md` file together.
    * We'll leave it periodically to focus on coding or another task, and return to it.
    * I may edit it during the workshop.
* Focus on data storage, software, some text conversion.
* Table of contents on left.
* Workshop plan:
    * 15min welcome, lead-in to [Data](#data)
    * 15min for [Data](#data)
    * 15min for [Software](#software)
    * 5min break
    * 15min for [Converter](#converter)
    * remaining time for [Discussion](#discussion)
* Try to focus near my cursor and ignore the rest.
    * This entire workshop is free, libre, and yours.
    * All material will be posted online.
* Work along, if you like.
    * I chose only widely-available free/libre prequisites.
    * minimum: text editor, python3, a command line shell
* Ask questions / make suggestions at any time during the workshop.
    * Something I could or should add? Say so.
    * Should I repeat, slow down, or speed up?
    * It's OK if we disagree.
    * If I feel like the workshop is veering off-topic or grinding to a halt I'll initiate a pause in questions or suggestions.
    * I'll be asking _you_ questions, too!

I hope you like fried pickles! 🥒

## Goals 📈

Focus on cooking fun/healthy/simple meals for and with others, not tech. Tech only enables cooking. To cook we need recipes and practice.

1. Immortal - readable and editable, always and forever.
2. Share-able - close second since cooking with and for others is better.

## Non-goals 📉

These are certainly fun, useful, nice to have, exercises for later.

* Convert between imperial and metric measurements.
* Double or halve recipe yield / servings.
* Auto-generate shopping list.
* Auto-generate nutrition info.
* Beautiful style.
    * Instead, rely on consistent structure.
    * There are plenty of free/libre tools that can help you pretty-print recipes.
    * Some are around today, more will appear tomorrow.
* Convert between different recipe formats (e.g. MealMaster).
* Printable cookbook.
* Capture every possible aspect of every recipe.
* Beautiful food photos.

## Data 📋

Our MLP (Minimum Lovable Recipe):

1. Description
1. Ingredients
1. Instructions

Everything else is "nice to have".

Start with human-readable [plain text](https://en.wikipedia.org/wiki/Plain_text).

(using paper is outside the scope of this workshop)

Add structure thoughtfully, as it becomes useful.

Structure allows integration with software.

Examples:

### Plain text 📰

`src/fried-pickles.md`

```markdown
# Fried Pickles

## Description

These fried pickles are a delicious disaster. I dare you to eat just one.

## Ingredients

* dill hamburger pickle chips
* 1 cup vegetable oil
* 1 cup corn meal
* 1 cup flour
* 1 teaspoon old bay seasoning
* ½ cup ranch dressing or preferred dipping sauce

## Directions

1. Preheat oil in a fryer or pan at medium-high heat. Use enough oil to cover the pickle chips as they fry.
1. Combine dry ingredients in a bowl, bag, or close-able container. Coat the pickle chips and place in the hot oil.
1. Fry until batter is lightly browned and crispy. Drain and let cool for a few minutes until warm and safe to eat.
1. Enjoy!
```

* 👍 Human readable.
* 👎 Unstructured; difficult to parse.

### JSON 🏗️

`src/fried-pickles.json`

```json
{
  "name": "Fried Pickles",
  "description": "These fried pickles are a delicious disaster. I dare you to eat just one.",
  "recipeIngredient": [
    "dill hamburger pickle chips",
    "1 cup vegetable oil",
    "1 cup corn meal",
    "1 cup flour",
    "1 teaspoon old bay seasoning",
    "½ cup ranch dressing or preferred dipping sauce"
  ],
  "recipeInstructions": [
    "Preheat oil in a fryer or pan at medium-high heat. Use enough oil to cover the pickle chips as they fry.",
    "Combine dry ingredients in a bowl, bag, or close-able container. Coat the pickle chips and place in the hot oil.",
    "Fry until batter is lightly browned and crispy. Drain and let cool for a few minutes until warm and safe to eat.",
    "Enjoy!"
  ],
  "@context": "http://schema.org",
  "@type": "Recipe"
}
```

* 👍 Easiest format to work with from code.
* 👎 Not very human readable.

### MealMaster 📟

`src/fried-pickles.mm`

```text
MMMMM----------------Meal-Master recipe exported by AnyMeal-----------------

      Title: Fried Pickles
 Categories: appetizer
      Yield: 4 servings

           dill hamburger pickle chips
      1 c  vegetable oil
      1 c  corn meal
      1 c  flour
      1 ts old bay seasoning
    1/2 c  ranch dressing or preferred
           -dipping sauce

  Preheat oil in a fryer or pan at medium-high heat. Use enough oil to cover
  the pickle chips as they fry.

  Combine dry ingredients in a bowl, bag, or close-able container. Coat the
  pickle chips and place in the hot oil.

  Fry until batter is lightly browned and crispy. Drain and let cool for a
  few minutes until warm and safe to eat.

  Enjoy!

MMMMM
```

* 👍 Human readable.
* 👎 Difficult to parse.

### GNOME Recipes 🍖

<https://wiki.gnome.org/Apps/Recipes>

Primary storage is SQLite databases.

Exports to INI files.

* 👍 Easy to work with from code.
* 👎 Not human readable.

## Software 🖱️

Required: free/libre code and data.

### AnyMeal 🗒️

Many free recipes available. Prints well.

* 👍 Tons of existing recipes available.
* 👍 Cross-platform desktop app. Fast!
* 👎 No mobile apps.
* 👎 Old UI.

Exercise: import `src/fried-pickles.mm`.

### Nextcloud 🌏

Smart data format, many UI choices. Prints poorly.

* 👍 Useful web and mobile apps.
* 👍 Standard, simple, structured data storage format.
* 👎 Slow.
* 👎 Poor search (although filtering works).

Exercise: import `src/fried-pickles.html`.

### GNOME Recipes 🍽️

Great-looking desktop app. Prints well.

* 👍 Looks beautiful. Definitely lots of work spent on UI.
* 👍 Integrated online recipe community.
* 👎 Unit entry bugs ("1½ cups" becomes "1 cup, 1/10 teaspoon")
* 👎 Written in C. No recent development activity.

Exercise: show Fried Pickles recipe.

## Converter ⚙️

Convert a Markdown recipe to JSON.

See `src/md-recipe-to-json.py`. First arg is a Markdown recipe.

This is for inspiration only. It depends on a very specific Markdown format:

* octothorpe headings
* first h1 is recipe title/name
* first h2 above one-line description
* second h2 above asterisk-unordered list of ingredients
* third h2 above numeric-ordered list of ingredients
* UNIX line endings might also be required

This could be more robustly implemented as a [pandoc filter](https://pandoc.org/filters.html). Pandoc parses Markdown into an abstract syntax tree (AST). This AST is much easier to work with from code.

## Discussion 🗣️

* What ideas did you get today for things you might try?
    * in software
    * in the kitchen
    * both
* What other free/libre recipe management software have you used or written?
* What digital recipe tools do you find most useful for:
    * cooking
    * sharing
    * collaborating
* Are you cooking for one, a few, or many?
* When you go to cook, how do you actually find and use the recipe you need?
* What features do you want/need in recipe management software?

## Resources 🛠️

* [workshop blog post at adammonsen.com](https://adammonsen.com/post/2046/)
    * includes all relevant links to workshop content and code
* [event page at fsf.org](https://www.fsf.org/events/libreplanet-workshop-april-24-the-immortal-cookbook-by-adam-monsen)
* presentation tech tools
    * [Vim text editor](https://www.vim.org/)
    * GNU/Linux operating system
    * Python 3 programming language
    * vim-markdown plugin (optional)
    * command-line shell (I used Bash)
    * jq (optional)
    * latest stable Nextcloud (v26 aka "Hub 4") with [cookbook app](https://apps.nextcloud.com/apps/cookbook)
* [JSON recipe schema](https://schema.org/Recipe)
* [email Adam](mailto:haircut+immortalcookbook@gmail.com)
* [AnyMeal free/libre recipe management software](https://wedesoft.github.io/anymeal/)
* [MealMaster format analysis](https://www.wedesoft.de/software/2020/07/07/mealmaster/)
* Free recipes in MealMaster format
    * <https://thehoseys.org/buster/recipes.html>
    * <https://www.ffts.com/recipes.htm>
    * <https://www.grassrootsrecipes.com/links.html>

<!--
vim: conceallevel=2 linebreak number wrap
-->
