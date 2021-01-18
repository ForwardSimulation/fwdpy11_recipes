MDFILES:=$(shell find book -type f -name '*.md')
RSTFILES:=$(shell find book -type f -name '*.rst')
RECIPES:=$(shell find recipes -type f -name '*.py')
HTMLBOOK:=_build

all: ${HTMLBOOK}

clean:
	rm -rf _build

${HTMLBOOK}: ${MDFILES} ${RSTFILES} ${RECIPES} 
	jupyter-book build --path-output . book
