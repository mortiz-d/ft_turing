(* Asi declaramos una funcion *)
let square x = x * x;;
(* val square : int -> int = <fun> *)

square 50;;
(* - : int = 2500 *)

Printf.printf "Resultado de funcion square: %d\n" (square 50);;

(* Asi se declara una funcion anonima *)
fun x -> x * x;;
(* - : int -> int = <fun> *)
Printf.printf "Resultado de funcion anonima: %d\n" ((fun x -> x * x) 50);;


(* Funcion con multiples parametros *)
let cat a b = a ^ " " ^ b;;
(* val cat : string -> string -> string = <fun> *)
Printf.printf "Resultado de funcion con multiples parametros: '%s'\n" (cat "hola" "mundo");;

(* Funcion que tiene un argumento predefinido *)
let cat_hola = cat "hola";;
(* val cat_hi : string -> string = <fun> *)
Printf.printf "Resultado de funcion con argumento predefinido: '%s'\n" (cat_hola "mundo");;


(* Funcion de orden superior *)
List.map;;
(* - : ('a -> 'b) -> 'a list -> 'b list = <fun> *)

List.map (fun x -> x * x);;
(* - : int list -> int list = <fun> *)

List.map (fun x -> x * x) [0; 1; 2; 3; 4; 5];;
(* - : int list = [0; 1; 4; 9; 16; 25] *)
 Printf.printf "Resultado de funcion de orden superior: '%s'\n" 
  (String.concat ", " (List.map (fun x -> string_of_int (x * x)) [0; 1; 2; 3; 4; 5]));;

