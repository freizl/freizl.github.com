#!/usr/bin/clisp

(defun fast-exp (x n)
  (defun fast-exp-inner (x n)
	(cond 
	  ((= 0 n) 1)
	  ((even? n) (fast-exp-inner (* x x) (/ n 2)))
	  (t (* x (fast-exp-inner x (1- n))))))
  (fast-exp-inner x n))

(defun even? (n)
  (= (rem n 2) 0))

(defun prompt-read (prompt)
  (format *query-io* "~d:" prompt)
  (force-output *query-io*)
  (read-line *query-io*))

(format t "~d~%" (fast-exp 3 (parse-integer (prompt-read "n"))))
