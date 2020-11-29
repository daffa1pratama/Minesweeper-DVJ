; (deftemplate bomb
;  (slot x_loc (type INTEGER) (default ?DERIVE))
;  (slot y_loc (type INTEGER) (default ?DERIVE))
; )

; (defrule startup
;  =>
;   (printout t "Masukkan ukuran board: ")
;   (assert (b_size (read)))
;   (printout t "Masukkan jumlah bomb: ")
;   (assert (bomb_count (read)))
;   (assert (user 0 0 0))
; )

; (defrule print-output
;  (b_size ?x)
;  (bomb_count ?y)
;  =>
;   (printout t ?x crlf)
;   (printout t ?y crlf)
; )

; (defrule define-bomb
;  (bomb_count ?x)
;  =>
;   (while (> ?x 0)
;    (assert (bomb (x_loc (read)) (y_loc (read))))
;    (bind ?x (- ?x 1))
;   )
; )

; (defrule print-board
;  (b_size ?x)
;  =>
;   (bind ?size ?x)
;   (bind ?y ?x)
;   (while (> ?x 0)
;    (while (> ?y 0)
;     (printout t "X ")
;     (bind ?y (- ?y 1))
;    )
;    (printout t crlf)
;    (bind ?x (- ?x 1))
;    (bind ?y ?size)
;   )
; )

(defrule startup
	=>
	(assert(b_size 4))
	(assert(bomb_count 4))
	(assert(bomb 2 3))
	(assert(bomb 3 2))
	(assert(bomb 0 3))
	(assert(bomb 1 3))
	(assert(tile 0 0 0))
	(assert(tile 0 1 0))
	(assert(tile 0 2 2))
	(assert(tile 1 0 0))
	(assert(tile 1 1 0))
	(assert(tile 1 2 3))
	(assert(tile 2 0 0))
	(assert(tile 2 1 1))
	(assert(tile 2 2 3))
	(assert(tile 3 0 0))
	(assert(tile 3 1 1))
	(assert(tile 3 3 2))
	(assert(user 1 1 0))
)

(defrule explore-1
	(b_size ?size)
	(user ?x ?y 0)
	(test (< (+ ?x 1) ?size))
	(test (< (+ ?y 1) ?size))
	(test (>= (- ?x 1) 0))
	(test (>= (- ?y 1) 0))
	(tile ?z1 ?y ?val1)
	(tile ?x ?z2 ?val2)
	(tile ?z3 ?y ?val3)
	(tile ?x ?z4 ?val4)
	(tile ?z1 ?z2 ?val5)
	(tile ?z1 ?z4 ?val6)	
	(tile ?z3 ?z2 ?val7)
	(tile ?z3 ?z4 ?val8)
	(test (= ?z1 (+ ?x 1)))
	(test (= ?z2 (+ ?y 1)))
	(test (= ?z3 (- ?x 1)))
	(test (= ?z4 (- ?y 1)))
	=>
	(assert (batasrule baru))
	(assert (user (+ ?x 1) ?y ?val1))
	(assert (user ?x (+ ?y 1) ?val2))
	(assert (user (- ?x 1) ?y ?val3))
	(assert (user ?x (- ?y 1) ?val4))
	(assert (user (+ ?x 1) (+ ?y 1) ?val5))
	(assert (user (+ ?x 1) (- ?y 1) ?val6))	
	(assert (user (- ?x 1) (+ ?y 1) ?val7))
	(assert (user (- ?x 1) (- ?y 1) ?val8))
)


