RMDFILES:=index.Rmd $(shell find chapters -type f -name '*.Rmd')
RECIPES:=$(shell find recipes -type f -name '*.py')
HTMLBOOK:=book_output

all: ${HTMLBOOK}

clean:
	rm -rf ${HTMLBOOK} fwdpy11_recipes.Rmd book_output/ _bookdown_files/

${HTMLBOOK}: ${RMDFILES} ${RECIPES} style.css
	RETICULATE_PYTHON=`which python3` R --no-save -e 'bookdown::render_book("index.Rmd","bookdown::gitbook",clean=T)'
