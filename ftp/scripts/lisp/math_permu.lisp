#!/usr/bin/clisp

(defun prompt-read (prompt)
  (format *query-io* "~d:" prompt)
  (force-output *query-io*)
  (read-line *query-io*))

(defun permutations (items &aux result)
   (if items
       (dolist (item items result)
        (dolist (permutation (permutations (remove item items)))
          (push (cons item permutation) result)))
       '(nil)))

(defvar *count* 0)

(defun calculate (sym1 sym2 x1 x2 x3)
  (format t "~d ~s ~d ~s ~d = ~d ~%" x1 sym1 x2 sym2 x3 (apply sym2 (list (apply sym1 (list x1 x2)) x3)))
  (incf *count*))

;;(calculate #'+ #'- 2 3 4)

(dolist (n (permutations (list 2 3 4)))
  (format t "~s ~%" n))
;;(format t "~s" (permutations (list #'+ #'- #'* #'/)))