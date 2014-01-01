SB=.cabal-sandbox
PD=$(SB)/bin/pandoc

PROG  = $(SB)/bin/freizl

.PHONY: slides

default: install

clean:
	rm -rf dist

build:
	cabal configure
	cabal build

install: slides
	cabal install

run:
	$(PROG) clean
	$(PROG) build

p:
	$(PROG) preview

ir: install run


########## Mirror to github

deploy: install run
	cp -r _site/* ../

########## Compile slides

## just being lazy not to cut off md file ext.
slides:
	for f in `ls -1 slides/*.md`; do \
	$(PD) -t dzslides -s "$$f" -o "$$f".html; \
	done;
