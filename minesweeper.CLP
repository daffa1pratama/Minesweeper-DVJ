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
  (assert (user 0 0 0))
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

(defrule explore-1
	(b_size ?size)
	(user ?x ?y 0)
	(test (< (+ ?x 1) (- ?size 1)))
	(test (< (+ ?y 1) (- ?size 1)))
	(test (>= (- ?x 1) 0))
	(test (>= (- ?y 1) 0))
	(tile ?z1 ?y ?val1)
	(test (= ?z1 (+ ?x 1)))
	(tile ?x ?z2 ?val2)
	(test (= ?z2 (+ ?y 1)))
	(tile ?z3 ?y ?val3)
	(test (= ?z3 (- ?x 1)))
	(tile ?x ?z4 ?val4)
	(test (= ?z4 (- ?y 1)))
	(tile ?z5 ?v5 ?val5)
	(test (= ?z5 (+ ?x 1)))
	(test (= ?v5 (+ ?y 1)))
	(tile ?z6 ?v6 ?val6)
	(test (= ?z6 (+ ?x 1)))
	(test (= ?v6 (- ?y 1)))	
	(tile ?z7 ?v7 ?val7)
	(test (= ?z7 (- ?x 1)))
	(test (= ?v7 (+ ?y 1)))
	(tile ?z8 ?v8 ?val8)
	(test (= ?z8 (- ?x 1)))
	(test (= ?v8 (- ?y 1)))
	=>
	(assert (user (+ ?x 1) ?y ?val1))
	(assert (user ?x (+ ?y 1) ?val2))
	(assert (user (- ?x 1) ?y ?val3))
	(assert (user ?x (- ?y 1) ?val4))
	(assert (user (+ ?x 1) (+ ?y 1) ?val5))
	(assert (user (+ ?x 1) (- ?y 1) ?val6))	
	(assert (user (- ?x 1) (+ ?y 1) ?val7))
	(assert (user (- ?x 1) (- ?y 1) ?val8))
)


