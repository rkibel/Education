alphabet: {0, 1, x, y}
start: q0
q0 (0 -> x, R q1) (_ -> _, R accept)
q1 ({0, y} -> ., R q1) (1 -> y, L q2)
q2 (y -> y, L q2) (x -> x, R q3) (0 -> 0, L q4)
q3 (y -> y, R q3) (_ -> _, R accept) (1 -> 1, S q6)
q4 (0 -> 0, L q4) (x -> x, R q5)
q5 (0 -> x, R q1)
q6 (x -> 0, R q7)
q7 ({x, y} -> ., R q7) (1 -> y, L q8)
q8 (y -> y, L q8) (0 -> 0, R q11) (x -> x, L q9)
q9 (x -> x, L q9) (0 -> 0, R q10)
q10 (x -> 0, R q7)
q11 (y -> y, R q11) (_ -> _, R accept) (1 -> 1, S q0)