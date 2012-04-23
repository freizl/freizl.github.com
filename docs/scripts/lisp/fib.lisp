#!/usr/bin/clisp

(defun fib (seq)
  (if (<= seq 1)
      seq
      (+ (fib (1- seq)) (fib (- seq 2)) )))

(defun prompt-read (prompt)
  (format *query-io* "~d:" prompt)
  (force-output *query-io*)
  (read-line *query-io*))

;; (format t "~a:" (prompt-read "seq"))
(format t "~d~%" (fib (parse-integer (prompt-read "seq"))))
