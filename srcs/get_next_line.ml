let getNextLine ic =
	try
		input_line ic  (* Devuelve la línea leída del archivo *)
	with e ->
		close_in_noerr ic;  (* Cierra el canal en caso de error *)
		raise e  (* Relanza la excepción *)