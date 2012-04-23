# Tools

~~~~~~{.sh}

apt-get install libpcre3 libpcre3-dev libssl-dev
hakyll server depend snap-server ll ../
~~~~~~

# Latex

## install latex

apt-get install texlive-latex-base texlive-latex-extra
apt-get install texlive-fonts-extra
getnonfreefonts-sys garamond

## FAQ

  - ** 'wrapfig.sty' not found \
    try `apt-cache search wrapfig` which indicate texlive-latex-extra need to be install

# wx
~~~~~~{.sh}
apt-get install libglu1-mesa-dev mesa-common-dev g++ libwxgtk2.8-dev libwxgtk2.8-dbg
cabal install wx-0.12.1.6
~~~~~~
