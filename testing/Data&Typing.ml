(* OCaml has floating-point values of type float. *)
(*To add floats, one must use +. instead of +: *)

2.0 +. 2.0;;
(* - : float = 4. *)

(* 1 + 2.5;; *)
(* Error: This expression has type float but an expression was expected of type int *)

(* In OCaml you need to explicitly convert the integer to a floating point number using the float_of_int function: *)
float_of_int 1 +. 2.5;;
(* - : float = 3.5 *)

(* LIST *)
(* Lists may be the most common data type in OCaml. 
They are ordered collections of values having the same type. 
Here are a few examples. *)
[];;
(* - : 'a list = [] *)

[1; 2; 3];;
(* - : int list = [1; 2; 3] *)

[false; false; true];;
(* - : bool list = [false; false; true] *)

[[1; 2]; [3]; [4; 5; 6]];;
(* - : int list list = [[1; 2]; [3]; [4; 5; 6]] *)