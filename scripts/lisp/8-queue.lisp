;;; (?) diff between MAP and MAPCAR in Common Lisp
;;;
;;;
;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(defun myappend (list1 list2)
  (if (null? list1)
      list2
      (cons (car list1) (myappend (cdr list1) list2))))

(defun square-scale-tree (tree)
  (cond ((null tree) nil)
        ((not (consp tree)) (* tree tree))
        (t (cons (square-scale-tree (car tree))
                    (square-scale-tree (cdr tree))))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defun accumulate (op initial sequence)
  (if (null sequence)
      initial
      (funcall op 
		       (car sequence)
               (accumulate op initial (cdr sequence)))))

(defun flatmap (proc seq)
  (accumulate 'append nil (mapcar proc seq)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defun test-accu ()
  (let (
		(arg0 (list (list 1 2) (list 3 4) (list (list 5 6) (list 7 8))))
		)
        (format t "~s~%" arg0)
        (format t "~s~%" (accumulate 'append nil arg0))))

(defun test-square-scale-tree () 
  (let (
		(arg0 (list (list 1 2) (list 3 4) (list (list 5 6) (list 7 8))))
		)
        (format t "~s~%" arg0)
        (format t "~s~%" (square-scale-tree arg0))))

(defun test-flatmap () 
  (let (
		(arg0 (list (list (list 1 2) (list 3 4)) (list (list 5 6) (list 7 8))))
		)
        (format t "~s~%" arg0)
        (format t "~s~%" (flatmap 'square-scale-tree arg0))))

(defun test-map ()
  (defun double (x)
	(* x x))
  (mapcar 'double (list 3 4 5)))

(test-accu)
(test-flatmap)
;(test-square-scale-tree)
(format t " ~s~%" (test-map))
