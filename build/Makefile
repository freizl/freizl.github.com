SB=.cabal-sandbox
PD=$(SB)/bin/pandoc

PROG  = $(SB)/bin/freizl

.PHONY: slides

default: install

clean:
	rm -rf dist
	rm -rf _site

build:
	cabal configure
	cabal build

install: build slides
	cabal install

run:
	$(PROG) clean
	$(PROG) build

p:
	$(PROG) watch


########## Mirror to github

deploy:
	stack exec freizl build
	cp -r _site/* ../

########## Compile slides

## just being lazy not to cut off md file ext.
slides:
	for f in `ls -1 slides/*.md`; do \
	$(PD) -t dzslides -s "$$f" -o "$$f".html; \
	done;
