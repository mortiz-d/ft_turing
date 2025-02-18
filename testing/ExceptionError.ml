let id_42 n = if n <> 42 then raise (Failure "AAAAAAAAAAAAa") else n;;
(* val id_42 : int -> int = <fun> *)

id_42 42;;
(* - : int = 42 *)

id_42 12;;
(* Exception: Failure "Sorry". *)