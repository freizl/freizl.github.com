---
title: Export a OrgMode doc in Chinese to PDF
author: Haisheng, Wu
tags: emacs, latex
---

# Introduction

OrgMode is really cool and export context to latex then processed to
PDF is quite straightforwards.
However when working with Chinese characters, I need additional
packages.

First of all, install the following packages. (I already
install the texlive package)

~~~~~~
apt-get install latex-cjk-chinese latex-cjk-xcjk texlive-xetex
~~~~~~

# First solution

Then in the org file, add the following latex options.

~~~~~~
#+LaTeX_HEADER: \usepackage{CJK}
#+LaTeX_HEADER: \begin{CJK}{UTF8}{gbsn}
~~~~~~

A littel drawback here is the `\begin{CJK}` is added as a header
option whice due to it will not be closed when I checked with the tex
output.

People suggest to change to `#+LaTeX: \begin{CJK}{UTF8}{gbsn}`
and append `#+LaTex: \end{CJK}` to the end of document.

It all works out OK except the title which is Chinese characters as
well can not display at all.

# Second solution

Well, it is XeLaTex which has better support for UTF8. Actually I did
not figure how to make it work with orgmode until a guy from orgmode
mail list point out [[http://thread.gmane.org/gmane.emacs.orgmode/51914][another thread]].

All I need to do is adding following option to the org document.

~~~~~~
#+LATEX_HEADER: \usepackage{xltxtra}
#+LATEX_HEADER: \setmainfont{WenQuanYi Micro Hei}
~~~~~~

Also need to customize emacs latex to pdf process.

~~~~~~
(setq org-latex-to-pdf-process
      '("xelatex -interaction nonstopmode -output-directory %o %f"
        "xelatex -interaction nonstopmode -output-directory %o %f"
        "xelatex -interaction nonstopmode -output-directory %o %f"))
~~~~~~

**PS: The main font has been setted may be vary among different systems.
How I find a proper font under ubuntu is via command `fc-list`.**
