## 2022-11-13

converting to Quarto

## 2021-12-20
Running log of steps used 
Each time you do some work enter the date on a new line
Then one line per statement thereafter
https://python-poetry.org/docs/basic-usage/

set up poetry
```sh
poetry new uclhal
poetry add nikola
poetry shell
```

git
```sh
git init
git branch -m main
```

https://getnikola.com/getting-started.html
conflicts if you run the set up command from the root of the poetry project
maybe something to do with their being a toml file there already?
instead I did the install from a clean (naked) subdirectory
site at ./uclhal/uclhal

?prob will need to publish the site from that subdirectoy if I wish to use github



## 2021-12-21
set up pylsp in sublime

updated pyproject.toml
```toml
[tool.poetry.dev-dependencies]
pytest = "^5.2"
python-lsp-server = "^1.3.1"
python-lsp-black = "^1.0.0"
mypy-ls = "^0.5.1"
pyls-isort = "^0.2.2"
```
then
```sh
poetry update
```

then
copied settings from dashRep into uclhal.sublime-project
used `which pylsp` to find the path to pylsp
```json
	"settings": {
        "LSP": {
            "pylsp": {
                "enabled": true,
                "command": [
                    "/Users/steve/Library/Caches/pypoetry/virtualenvs/uclhal-XMZ_bNmG-py3.9/bin/pylsp",
                ],
                "settings": {
                    "pylsp.plugins.flake8.executable": "/Users/steve/Library/Caches/pypoetry/virtualenvs/uclhal-XMZ_bNmG-py3.9/bin/flake8",
                },
            },
        },
    },
```


deploy to github
uses the following tool
https://github.com/c-w/ghp-import

> Inside your repository just run ghp-import $DOCS_DIR where $DOCS_DIR is the path to the built documentation. This will write a commit to your gh-pages branch with the current documents in it.


to build
```sh
cd ./uclhal/uclhal
nikola build
```

to deploy
```sh
cd ./uclhal/uclhal
nikola github_deploy
```

2021-12-21t11:02:53
Woo hoo!
Site up, running and deployed!

## 2021-12-22
Look into github actions for automatic deploy
I don't think it will work b/c the blog lives in a subdir
hence made a symlink
then edited the github actions file at
https://github.com/docsteveharris/nikola-action/releases/tag/v3.1.0-alpha

... I think in the end this might have worked
But was confused b/c failed b/c could not find path `src` but maybe b/c I was working from a feature branch
So abandoned (?prematurely)
And moved all blog files to top level
and reset to the default github actions yml file rather than my fork
this worked *only* when I pushed from the `src` branch

but staying with this approach 'cos seems cleaner anyway


## 2021-12-29
just getting my bearings back
serving from port 8000
from command line

```sh
nikola build && nikola serve
```

useful pages
themes
https://themes.getnikola.com/v8/zen/
restructured text
https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#indirect-hyperlink-targets
nikola
https://getnikola.com/handbook.html#indexes

others work
https://paulomarconi.github.io/blog/Nikola-guide/
http://louistiao.me/posts/how-i-customized-my-nikola-powered-site/
https://www.brainsorting.dev/posts/create-a-blog-with-nikola/
http://hannahbarton.org.uk/pages/handbook/

old websites
https://github.com/docsteveharris/harris-data-lab/blob/main/content/authors/finn-catling/_index.md

canterville
images served from files/images using url images/name_of_image
e.g. placed the blog log there


lots of fiddling with the logo
now only displays correctly on the landing page
tried to set up separate pages for each lab member
prob easier? just to introduce each person via blog post with an appropriate category?
then use the category to index individuals


## 2022-01-04
just added a bunch of pages for each lab member
still do the HYLODE team


