#!/usr/bin/clisp

(defun fib (seq)
  (loop repeat seq
	for x = 0 then y
	and y = 1 then (+ x y)
	collect y))

(defun prompt-read (prompt)
  (format *query-io* "~d:" prompt)
  (force-output *query-io*)
  (read-line *query-io*))

;; (format t "~a:" (prompt-read "seq"))
(format t "~d~%" (last (fib (parse-integer (prompt-read "seq")))))
