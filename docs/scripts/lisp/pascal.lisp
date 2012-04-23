#!/usr/bin/clisp

;; both row and column start from 0

(defun pascal (row column)
  (cond
    ((< row column) 'error)
    ((= column 0) 1)
    ((= row column) 1)
    (t (+
	    (pascal (1- row) (1- column))
	    (pascal (1- row) column)))))

(format t "~d" (pascal 4 2))
