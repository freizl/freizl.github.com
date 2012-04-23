#!/usr/bin/clisp

(defun fsum (a b)
  (funcall (if (> b 0) '+ '-) a b))

(format t "~d~%" (fsum 3 -3))
