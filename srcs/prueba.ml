(* ASI SE PONEN LOS ARGUMENTOS *)
let usage_msg = "usage: ft_turing [-h] jsonfile input\n\npositional arguments:\n	jsonfile : json description of the machine\n\n	input : input of the machine\n\noptional arguments:\n"

let verbose = ref false

let input_files = ref []

let output_file = ref ""

let anon_fun filename =
  input_files := filename :: !input_files

let show_help () =
	Printf.printf "usage: ft_turing [-h] jsonfile input\n\npositional arguments:\n\tjsonfile : json description of the machine\n\n\tinput : input of the machine\n\noptional arguments:\n";
	Printf.printf "  -h, --help  Display this list of options\n";
	exit 0
  
(* \npositional arguments:\n	jsonfile json description of the machine\n\n	input input of the machine\n\noptional arguments:\n	-h, --help show this help message and exit\n *)
let speclist =
	[
	  ("-h", Arg.Unit show_help, "Display this list of options");
	  ("--help", Arg.Unit show_help, "Display this list of options")
	]

  
(* 
let getNextLine ic =
	try
		input_line ic  (* Devuelve la línea leída del archivo *)
	with e ->
		close_in_noerr ic;  (* Cierra el canal en caso de error *)
		raise e  (*Relanza la excepción *)
*)
	
let process_file json_file =
	let ic = open_in json_file in
	try
		while true do
			let line = getNextLine.getNextLine ic in
			print_endline line;  (* Imprime la línea leída *)
			flush stdout;  (* Asegura que la salida se escriba en el dispositivo de salida *)
		done
	with End_of_file ->
		close_in ic  (* Cierra el archivo *)
	
		

	let () =
		Arg.parse speclist anon_fun usage_msg;
		(* Printf.printf "VERBOSE ? %b \n" !verbose; *)
		
		(* Arg.parse speclist anon_fun usage_msg *)
	  (* let argc = Array.length Sys.argv in *)
		(* Printf.printf "Leido %d\n" argc; *)
	   (* if argc <= 2 || argc > 3 then *)
		(*

			(* Printf.printf "Argumento solo: '%s'\n" Sys.argv.(1); *)
			(* print_endline "usage: ft_turing [-h] jsonfile input"; *)
			Printf.printf "usage: ft_turing [-h] jsonfile input\n";
			if Sys.argv.(1) = "--help" || Sys.argv.(1) = "-h" then
				(

					Printf.printf "\npositional arguments:\n	jsonfile json description of the machine\n\n	input input of the machine\n\noptional arguments:\n	-h, --help show this help message and exit\n";
				)
			
			
		)
		else if argc > 3 then
			print_endline "no mas de dos" *)
	  (* else ( *)
		
		(* ) *)


	  	let json_file = Sys.argv.(1) in
			let usage = Sys.argv.(2) in
			(* Mostrar los argumentos *)
			Printf.printf "Argumento 1: %s\n" json_file;
			Printf.printf "Argumento 2: %s\n" usage;
			
			(* process_file json_file; *)
	