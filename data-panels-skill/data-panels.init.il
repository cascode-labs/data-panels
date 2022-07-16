printf("Initializing data-panels\n")

; Load Maestro SRR extension functions
let((file_path dir_path)
	file_path = simplifyFilename(get_filename(piport))
	dir_path = strcat("/" buildString(reverse(cdr(reverse(parseString(file_path "/")))) "/"))
	loadi(strcat( dir_path "/DpRun.il"))
	; loadi(strcat( dir_path "/ExportSimFiles" "/ExportCallback.il"))
	; loadi(strcat( dir_path "/ExportSimFiles" "/ExportCellImage.ils"))
	; loadi(strcat( dir_path "/ExportSimFiles" "/ExportCornersSDB.ils"))
	; loadi(strcat( dir_path "/ExportSimFiles" "/ExportFileFactory.ils"))
	; loadi(strcat( dir_path "/ExportSimFiles" "/ExportMaestroOutputResultsCSV.ils"))
	; loadi(strcat( dir_path "/ExportSimFiles" "/ExportMaestroOutputsCSV.ils"))
	; loadi(strcat( dir_path "/ExportSimFiles" "/ExportTestInfo.ils"))
)

printf("  Done, Initialized data-panels\n")
