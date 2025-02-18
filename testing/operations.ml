(* Esto es una expresion *)
50 * 50;;
(* The above example says, “50 * 50 is an expression that has type int (integer) and evaluates to 2500.” Since it is an anonymous  *)
(* - : int = 2500 *)

(* Otros ejemplos de expresiones anonimas *)
6.28;;
(* - : float = 6.28 *)

"This is really disco!";;
(* - : string = "This is really disco!" *)

'a';; (* Note the single quotes *)
(* - : char = 'a' *)

true;;
(* - : bool = true *)


(* Podemos establecer variables con 'let' *)
(* Asi establecemos listas [1;2;3;4] *)
let num_list = [1; 2; 3; 4];;
(* val num_list : int list = [1; 2; 3; 4] *)

["this"; "is"; "mambo"];;
(* - : string list = ["this"; "is"; "mambo"] *)

(* Asi añadimos un valor a la lista *)
9 :: num_list;;
(* - : int list = [9; 1; 2; 3; 4] *)
