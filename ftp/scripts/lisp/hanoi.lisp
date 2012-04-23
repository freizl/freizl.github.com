#!/usr/bin/clisp

(defun prompt-read (prompt)
  (format *query-io* "~d:" prompt)
  (force-output *query-io*)
  (read-line *query-io*))

(defun hanio (amount from to tail) 
  (defvar *steps* 0)
  (format t "mission: move ~d disks from tower ~a to tower ~a ~%" amount from to)
  (defun dohanio (amount from to tail)
    (cond
    (
      (> amount 0)
      (dohanio (1- amount) from tail to)
      (format t "move from ~a to ~a ~%" from to) 
      (incf *steps*)
      (dohanio (1- amount) tail to from)
     ))
  )
  (dohanio amount from to tail)
  (format t "steps: ~d ~%" *steps*))

(hanio (parse-integer (prompt-read "n")) "A" "B" "C")
