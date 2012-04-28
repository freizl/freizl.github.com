#!/usr/bin/clisp

;;; ? how to make it work in clisp?
(defun a-plus-abs-b (a b)
  ((if (> b 0) + -) a b))

  ;;(format t "~d~%" (sum-squa x1 x2 x3))
