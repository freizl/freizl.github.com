PD=pandoc

.PHONY: slides

default: rebuild

###
### build the tool
###

rebuild:
	cabal clean
	cabal v2-build

build:
	cabal v2-build


###
### generates site
###
freizl:
	cabal v2-exec freizl --  build

watch:
	cabal v2-exec freizl --  watch

refreizl:
	cabal v2-exec freizl --  rebuild

########## Mirror to github

deploy: refreizl
	cp -r _site/* ../

########## Compile slides

## just being lazy not to cut off md file ext.
slides:
	for f in `ls -1 slides/*.md`; do \
	$(PD) -t dzslides -s "$$f" -o "$$f".html; \
	done;
