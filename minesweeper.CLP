(deftemplate bomb
 (slot x_loc (type INTEGER) (default ?DERIVE))
 (slot y_loc (type INTEGER) (default ?DERIVE))
)

(defrule startup
 =>
  (printout t "Masukkan ukuran board: ")
  (assert (b_size (read)))
  (printout t "Masukkan jumlah bomb: ")
  (assert (bomb_count (read)))
)

(defrule print-output
 (b_size ?x)
 (bomb_count ?y)
 =>
  (printout t ?x crlf)
  (printout t ?y crlf)
)

(defrule define-bomb
 (bomb_count ?x)
 =>
  (while (> ?x 0)
   (assert (bomb (x_loc (read)) (y_loc (read))))
   (bind ?x (- ?x 1))
  )
)

(defrule print-board
 (b_size ?x)
 =>
  (bind ?size ?x)
  (bind ?y ?x)
  (while (> ?x 0)
   (while (> ?y 0)
    (printout t "X ")
    (bind ?y (- ?y 1))
   )
   (printout t crlf)
   (bind ?x (- ?x 1))
   (bind ?y ?size)
  )
)