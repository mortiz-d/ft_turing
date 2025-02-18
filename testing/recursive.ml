(* A recursive function calls itself in its own body. 
Such functions must be declared using let rec … = … instead of just let. 
Recursion is not the only means to perform iterative computation on OCaml. 
Loops such as for and while are available, but they are meant to be used when 
writing imperative OCaml in conjunction with mutable data. Otherwise, 
recursive functions should be preferred. *)
let rec range lo hi =
  if lo > hi then
    []
  else
    lo :: range (lo + 1) hi;;
(* val range : int -> int -> int list = <fun> *)

range 2 5;;
(* - : int list = [2; 3; 4; 5] *)
Printf.printf "Resultado de funcion de orden superior: '%s'\n" 
  (String.concat ", " (List.map string_of_int (range 1 5)));;
