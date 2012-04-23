(defun man-or-boy (x)
 (man-or-boy-func x (lambda () 1) (lambda () -1)
                    (lambda () -1) (lambda () 1)
                    (lambda () 0)))

(defun man-or-boy-func (k-param x1 x2 x3 x4 x5)
 (let*
   ((k k-param)
    (b
     (lambda ()
       (progn
         (setq k (- k 1))
         (man-or-boy-func k b x1 x2 x3 x4)))))
   (if (<= k 0)
       (+ (funcall x4) (funcall x5))
;       1)))
       (funcall b))))

(format t " ~s~%" (man-or-boy 1))
