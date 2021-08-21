#!/usr/bin/clisp

(loop repeat 3
      for r = '(1) then (mapcar #'+ (cons 0 r) (append r '(0)))
      ;;do (format t "~{~6D~^,~}~%" 'r))
      do (format t "~s~%" r))
