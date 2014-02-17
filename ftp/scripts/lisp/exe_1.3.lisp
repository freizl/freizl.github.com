#!/usr/bin/clisp

(defun sum-squa (x1 x2 x3)
  (- (+ (square x1) (square x2) (square x3)) (square (min x1 x2 x3))))

(defun square (x) (* x x))

(defun sum-square-max (x1 x2 x3)
  (let* ((x (if (> x1 x2) x1 x2)) 
	 (y (if (< x1 x2) x1 x2)) 
	 (z (if (> y x3) y x3)))
    (+ (* x x) (* z z))))

((lambda (x1 x2 x3)
  (format t "~d~%" (sum-squa x1 x2 x3))
  (format t "~d" (sum-square-max x1 x2 x3))) 5 3 4)
