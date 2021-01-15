HTMLBOOK:=book_output/coalescent-simulation.html

RMDFILES:=index.Rmd $(shell find chapters -type f -name '*.Rmd')

all: ${HTMLBOOK}

clean:
	rm -rf ${HTMLBOOK} fwdpy11_recipes.Rmd book_output/* 

# NOTE: the html output depends on the pdf being built
# because we have some hacky things involving msprime's DemographyDebugger,
# and I worry about overwriting files if the two render steps executed at the
# same time via a "make -j x" command.
${HTMLBOOK}: ${RMDFILES}
	RETICULATE_PYTHON=`which python3` PYTHONPATH=.. r -e 'bookdown::render_book("index.Rmd","bookdown::gitbook",clean=T)'

