#!/usr/bin/clisp

(defun fsum (n)
  (defun f-inner (a b c y)
	(if (< y 3)
	    a
		(f-inner (+ a (* b 2) (* c 3)) a b (1- y))))
  (if (< n 3)
	  n
	  (f-inner 2 1 0 n)))

(defun prompt-read (prompt)
  (format *query-io* "~d:" prompt)
  (force-output *query-io*)
  (read-line *query-io*))

;; (format t "~a:" (prompt-read "seq"))
(format t "~d~%" (fsum (parse-integer (prompt-read "n"))))
