###################################################
# SampleMiner v1.0 (Date 08-07-2022 / dd-mm-yyyy) #
###################################################

'''

Instructions, version notes and templates at the end of the code.

'''

###################
##               ##
##  THE PROGRAM  ##
##               ##
###################

# Program start up: imports core modules and declares global variables

import os, os.path, getpass, subprocess, sys, ast, shutil, ctypes

OperatingSystem = os.name
CurrentUser = getpass.getuser()
CurrentUserRootDir = str("/Users/") + str(CurrentUser)
SampleMinerDataDir = ''
DatabasesTsvFilesDir = ''
DatabasesDictionariesDir = ''
DefaultDirectoryRoot = ''
CustomDirectoryRoot = ''
CustomDirectory =''
MinedSamplesDir = ''
SamplesAccessionNumbersDir = ''
SamplesMetadataDir = ''
ReportsDir = ''
DownloadedSequencesDir = ''
PatricContents = []
EnterobaseContents = []
PatricCollection = []
EnterobaseCollection = []
Collection = []

# Program loop: shows opening screen w/h main menu, criates working directories and handles program execution

def Start():
	
	global PatricContents, EnterobaseContents, PatricCollection, EnterobaseCollection, Collection
	
	Default_directory_set_up()
	
	Terminal_set_up()
		
	Clear_screen(OperatingSystem)
	
	choice = ""
	
	while choice not in ("1", "2", "3", "4", "5", "6", "7", "8","10", "20", "30", "40", "50", "t"):
		
		Clear_screen(OperatingSystem)
		
		print ("\n>>>> SampleMiner v1.0 <<<<\n\n\n")
		
		Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot)
		
		print ("\n\nMAIN MENU\n\n(0) Set working directory\n\n(1) Import Patric tsv file\n(2) Browse Patric with keywords\n(3) Browse Patric with field specific keywords\n(4) Fetch Patric isolates’ metadata with keywords\n(5) Fetch Patric isolates’ metadata with field specific keywords\n(6) Exclude / Reinclude Patric isolates’ from sample\n(7) Describe Patrick sample with tables\n(8) Describe Patrick sample with graphics\n\n(9) Import Enterobase tsv file\n(10) Browse Enterobase with keywords\n(11) Browse Enterobase with field specific keywords\n(12) Fetch Enterobase isolates’ metadata with keywords\n(13) Fetch Enterobase isolates’ metadata with field specific keywords\n(14) Exclude / Reinclude Enterobase isolates’ from sample\n(15) Describe Enterobase sample with tables\n(16) Describe Enterobase sample with graphics\n\n(40) Fetch sample isolates’ DNA sequences from NCBI\n\n(50) Quit\n")
		
		choice = input("Please, enter your choice from above list: ")
		
		print ()
		
		if choice == "":
			pass
			
		# (0) Set working directory
		
		elif choice == "0":
			
			CustomDirectory = input('\n\n\nPlease, enter working directory: ')
			CustomDirectory = CustomDirectory.lower()
			
			Custom_directories_set_up(CustomDirectory)
			
			choice = ""
			Clear_screen(OperatingSystem)
			
		# (1) Import Patric tsv file
		
		elif choice == "1":
			
			Clear_screen(OperatingSystem)
			
			print('You are using Patric.\n')
			
			input_file = DatabasesTsvFilesDir + "PATRIC_E coli_Complete genome_Metadata.tsv"
			
			File_checking_result = File_checking(input_file)
			
			if File_checking_result == True:
			
				result = Tsv_to_list_dicts(input_file)
				
				output_file = DatabasesDictionariesDir + "PATRIC_E coli_Complete genome_Metadata_list.txt"
				
				f = open(output_file, "w", encoding='utf-8')
				f.write(str(result))
				f.close()
			
			else:
				
				print(f'\n\n\n\nFile not found:\n\n{input_file}\n\n\n')
				option = 1
				Press_a_key(OperatingSystem, option)
			
			choice = ""
			Clear_screen(OperatingSystem)
		
		# (2) Browse Patric with keywords
		
		elif choice == "2":
			
			Clear_screen(OperatingSystem)
			
			print('You are using Patric.\n\n\n\n\n')
			
			print('Uploading Patric database to memory...\n\n')
			
			input_file = DatabasesDictionariesDir + "PATRIC_E coli_Complete genome_Metadata_list.txt"
			
			File_checking_result = File_checking(input_file)
			
			if File_checking_result == True:
			
				if PatricCollection == []:
					f = open(input_file, "r", encoding='utf-8')
					contents = f.read()
					f.close()
					PatricCollection = ast.literal_eval(contents)
				else:
					pass
				
				Collection = PatricCollection
				
				Clear_screen(OperatingSystem)
				
				database = "Patric"
				
				Data_mining(database, Collection, DefaultDirectoryRoot, CustomDirectoryRoot)
			
			else:
				
				print(f'\n\n\n\nFile not found:\n\n{input_file}\n\n\n')
			
			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
			
		# (3) Browse Patric with field specific keywords
		
		elif choice == "3":
			
			Clear_screen(OperatingSystem)
			
			print('You are using Patric.\n\n\n\n\n')
			
			print('Uploading Patric database to memory...\n\n')
			
			input_file = DatabasesDictionariesDir + "PATRIC_E coli_Complete genome_Metadata_list.txt"
			
			File_checking_result = File_checking(input_file)
			
			if File_checking_result == True:
				
				if PatricCollection == []:
					f = open(input_file, "r", encoding='utf-8')
					contents = f.read()
					f.close()
					PatricCollection = ast.literal_eval(contents)
				else:
					pass
				
				Collection = PatricCollection
				
				Clear_screen(OperatingSystem)
				
				database = "Patric"
				
				dict_key_options_tuple = ('genome name', 'isolation country', 'host name', 'isolation source', 'serovar', 'pathovar', 'mlst')
				dict_key_options_menu = ('(1) species\n(2) Isolation Country\n(3) Host Name\n(4) Isolation Source\n(5) Serovar\n(6) Pathovar\n(7) MLST')
				options = ('1','2','3','4','5','6','7')
				
				Data_mining_searching_dict_keys(database, Collection, dict_key_options_tuple, dict_key_options_menu, options, DefaultDirectoryRoot, CustomDirectoryRoot)
			
			else:
				
				print(f'\n\n\n\nFile not found:\n\n{input_file}\n\n\n')
			
			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
			
		# (4) Fetch Patric isolates’ metadata with keywords
		
		elif choice == "4":
			
			Clear_screen(OperatingSystem)
			
			print('You are using Patric.\n\n\n\n\n')
			
			print('Uploading Patric database to memory...\n\n')
			
			input_file = DatabasesDictionariesDir + "PATRIC_E coli_Complete genome_Metadata_list.txt"
			
			File_checking_result = File_checking(input_file)
			
			if File_checking_result == True:
				
				if PatricCollection == []:
					f = open(input_file, "r", encoding='utf-8')
					contents = f.read()
					f.close()
					PatricCollection = ast.literal_eval(contents)
				else:
					pass
				
				Collection = PatricCollection
				
				database = 'Patric'
				accession_number_field = 'biosample accession'
				
				keep_entry_key = 'keep entry'
				keep_entry_val = 'y'
	
				species_key = 'organism name'
				isolate_name_key = 'genome name'
				isolation_country_key = 'isolation country'
				host_key = 'host name'
				isolation_source_key = 'isolation source'
				serovar_key = 'serovar'
				pathovar_1_key = 'pathovar'
				st_type_key = 'mlst'
				assembly_id_key = 'genome id'
				genome_quality_key = 'genome quality'
				
				isolates_metadata_keys = (accession_number_field, isolate_name_key, species_key, isolation_country_key, host_key, isolation_source_key, serovar_key, pathovar_1_key, st_type_key, assembly_id_key, genome_quality_key)
								
				metadata_file = SamplesMetadataDir + 'Patric isolates metadata.txt'
				metadata_csv_file = SamplesMetadataDir + 'Patric isolates metadata.csv'
				
				metadata_csv_file_headers = ('Biosample accession' + ',' + 'Isolate name' + ',' + 'Species' + ',' + 'Isolation country' + ',' + 'Host' + ',' + 'Isolation source' + ',' + 'Serovar' + ',' + 'Pathovar' + ',' + 'MLST' + ',' + 'Assembly id' + ',' + 'Genome quality' + ',' + 'Keep entry?' + '\n')
				
				statistics_file = SamplesMetadataDir + 'Patric isolates metadata statistics.txt'
				statistics_csv_file = SamplesMetadataDir + 'Patric isolates metadata statistics.csv'
				
				sampling_report_file = ReportsDir + 'Patric sampling report.txt'
				
				Clear_screen(OperatingSystem)
				
				Fetch_accession_numbers(Collection, database, accession_number_field, keep_entry_key, keep_entry_val, isolates_metadata_keys, metadata_file, metadata_csv_file, metadata_csv_file_headers, statistics_file, statistics_csv_file, sampling_report_file, DefaultDirectoryRoot, CustomDirectoryRoot)
				
			else:
				
				print(f'\n\n\n\nFile not found:\n\n{input_file}\n\n\n')
			
			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
			
		# (5) Fetch Patric isolates’ metadata with field specific keywords
		
		elif choice == "5":
			
			Clear_screen(OperatingSystem)
			
			print('You are using Patric.\n\n\n\n\n')
			
			print('Uploading Patric database to memory...\n\n')
			
			input_file = DatabasesDictionariesDir + "PATRIC_E coli_Complete genome_Metadata_list.txt"
			
			File_checking_result = File_checking(input_file)
			
			if File_checking_result == True:
				
				if PatricCollection == []:
					f = open(input_file, "r", encoding='utf-8')
					contents = f.read()
					f.close()
					PatricCollection = ast.literal_eval(contents)
				else:
					pass
				
				Collection = PatricCollection
				
				database = 'Patric'
				accession_number_field = 'biosample accession'
				
				keep_entry_key = 'keep entry'
				keep_entry_val = 'y'
				
				species_key = 'organism name'
				isolate_name_key = 'genome name'
				isolation_country_key = 'isolation country'
				host_key = 'host name'
				isolation_source_key = 'isolation source'
				serovar_key = 'serovar'
				pathovar_1_key = 'pathovar'
				st_type_key = 'mlst'
				assembly_id_key = 'genome id'
				genome_quality_key = 'genome quality'
				
				isolates_metadata_keys = (accession_number_field, isolate_name_key, species_key, isolation_country_key, host_key, isolation_source_key, serovar_key, pathovar_1_key, st_type_key, assembly_id_key, genome_quality_key)
				
				metadata_file = SamplesMetadataDir + 'Patric isolates metadata.txt'
				metadata_csv_file = SamplesMetadataDir + 'Patric isolates metadata.csv'
				
				metadata_csv_file_headers = ('Biosample accession' + ',' + 'Isolate name' + ',' + 'Species' + ',' + 'Isolation country' + ',' + 'Host' + ',' + 'Isolation source' + ',' + 'Serovar' + ',' + 'Pathovar' + ',' + 'MLST' + ',' + 'Assembly id' + ',' + 'Genome quality' + ',' + 'Keep entry?' + '\n')
				
				statistics_file = SamplesMetadataDir + 'Patric isolates metadata statistics.txt'
				statistics_csv_file = SamplesMetadataDir + 'Patric isolates metadata statistics.csv'
				
				sampling_report_file = ReportsDir + 'Patric sampling report.txt'
				
				dict_key_options_tuple = ('genome name', 'isolation country', 'host name', 'isolation source', 'serovar', 'pathovar', 'mlst')
				dict_key_options_menu = ('(1) species\n(2) Isolation Country\n(3) Host Name\n(4) Isolation Source\n(5) Serovar\n(6) Pathovar\n(7) MLST')
				options = ('1','2','3','4','5','6','7')
				
				Clear_screen(OperatingSystem)
				
				Fetch_accession_numbers_searching_dict_keys(Collection, database, accession_number_field, keep_entry_key, keep_entry_val, isolates_metadata_keys, metadata_file, metadata_csv_file, metadata_csv_file_headers, statistics_file, statistics_csv_file, sampling_report_file, dict_key_options_tuple, dict_key_options_menu, options, DefaultDirectoryRoot, CustomDirectoryRoot)

			else:
				
				print(f'\n\n\n\nFile not found:\n\n{input_file}\n\n\n')

			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
		
		# (6) Exclude / Reinclude Patric isolates’ from sample
		
		elif choice == "6":
			
			Clear_screen(OperatingSystem)
			
			print('You are using Patric.\n')
			
			accession_number_field = 'biosample accession'
			
			metadata_csv_file = SamplesMetadataDir + 'Patric isolates metadata.csv'
			accession_numbers_file = SamplesAccessionNumbersDir + 'Patric_accession numbers.txt'
			accession_numbers_BU_file = SamplesAccessionNumbersDir + 'Patric_accession numbers_BU.txt'
			removed_accession_numbers_file = SamplesAccessionNumbersDir + 'Patric_accession numbers_RM.txt'
			
			File_checking_result = File_checking(metadata_csv_file)
			file1 = File_checking_result
			File_checking_result = File_checking(accession_numbers_file)
			file2 = File_checking_result
			
			if file1 == True and file2 == True:
			
				Clear_screen(OperatingSystem)
				
				Edit_accession_numbers_list(accession_number_field, metadata_csv_file, accession_numbers_file, accession_numbers_BU_file, removed_accession_numbers_file, DefaultDirectoryRoot, CustomDirectoryRoot)
			
			else:
				
				print(f'\n\n\n\nFile(s) not found:\n\n{metadata_csv_file}\n\nand / or\n\n{accession_numbers_file}\n\n\n')
				option = 1
				Press_a_key(OperatingSystem, option)
			
			choice = ""
			Clear_screen(OperatingSystem)
		
		# (7) Describe Patrick sample with tables
		
		elif choice == "7":
			
			Clear_screen(OperatingSystem)
			
			print('You are using Patric.\n')
			
			database = 'Patric'
			graphics_option = 'n'
			
			species_key = 'Species'
			isolation_country_key = 'Isolation country'
			pathovar_1_key = 'Pathovar'
			serovar_key = 'Serovar'
			st_type_key = 'MLST'
			host_key = 'Host'
			
			isolates_metadata_keys = (species_key, isolation_country_key, pathovar_1_key, serovar_key, st_type_key, host_key)
			
			statistics_csv_file = SamplesMetadataDir + 'Patric isolates metadata statistics.csv'
			sample_summary_file = SamplesMetadataDir + 'Patric isolates metadata summary.txt'

			File_checking_result = File_checking(statistics_csv_file)
			
			if File_checking_result == True:
		
				Clear_screen(OperatingSystem)
				
				Summarize(graphics_option, isolates_metadata_keys, statistics_csv_file, database, sample_summary_file, DefaultDirectoryRoot, CustomDirectoryRoot)
			
			else:
				
				print(f'\n\n\n\nFile(s) not found:\n\n{statistics_csv_file}\n\nand / or\n\n{sample_summary_file}\n\n\n')
			
			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
		
		# (8) Describe Patrick sample with graphics
		
		elif choice == "8":
			
			Clear_screen(OperatingSystem)
			
			print('You are using Patric.\n')
			
			database = 'Patric'
			graphics_option = 'y'
			
			species_key = 'Species'
			isolation_country_key = 'Isolation country'
			pathovar_1_key = 'Pathovar'
			serovar_key = 'Serovar'
			st_type_key = 'MLST'
			host_key = 'Host'
			
			isolates_metadata_keys = (species_key, isolation_country_key, pathovar_1_key, serovar_key, st_type_key, host_key)
			
			statistics_csv_file = SamplesMetadataDir + 'Patric isolates metadata statistics.csv'
			sample_summary_file = SamplesMetadataDir + 'Enterobase isolates metadata summary.txt'
			
			File_checking_result = File_checking(statistics_csv_file)
			
			if File_checking_result == True:
			
				Clear_screen(OperatingSystem)
				
				Summarize(graphics_option, isolates_metadata_keys, statistics_csv_file, database, sample_summary_file, DefaultDirectoryRoot, CustomDirectoryRoot)
			
			else:
				
				print(f'\n\n\n\nFile(s) not found:\n\n{statistics_csv_file}\n\nand / or\n\n{sample_summary_file}\n\n\n')

			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
		
		# (9) Import Enterobase tsv file
		
		elif choice == "9":
			
			Clear_screen(OperatingSystem)

			print('You are using Enterobase.\n\n')
			print('The four tsv files will first be imported as Python dictionaries\n\n')
			print('Starting importations...\n\n')
			
			input_file_1 = DatabasesTsvFilesDir + "Enterobase_E coli_Complete genome_Metadata_1.tsv"
			input_file_2 = DatabasesTsvFilesDir + "Enterobase_E coli_Complete genome_Metadata_2.tsv"
			input_file_3 = DatabasesTsvFilesDir + "Enterobase_E coli_Complete genome_Metadata_3.tsv"
			input_file_4 = DatabasesTsvFilesDir + "Enterobase_E coli_Complete genome_Metadata_4.tsv"
			
			File_checking_result = File_checking(input_file_1)
			file1 = File_checking_result
			File_checking_result = File_checking(input_file_2)
			file2 = File_checking_result
			File_checking_result = File_checking(input_file_3)
			file3 = File_checking_result
			File_checking_result = File_checking(input_file_4)
			file4 = File_checking_result
			
			if file1 == True and file2 == True and file3 == True and file4 == True:
			
				result = Tsv_to_list_dicts(input_file_1)
				output_file_1 = DatabasesDictionariesDir + "Enterobase_E coli_Complete genome_Metadata_list_1.txt"
				f = open(output_file_1, "w", encoding='utf-8')
				f.write(str(result))
				f.close()
				
				result = Tsv_to_list_dicts(input_file_2)
				output_file_2 = DatabasesDictionariesDir + "Enterobase_E coli_Complete genome_Metadata_list_2.txt"
				f = open(output_file_2, "w", encoding='utf-8')
				f.write(str(result))
				f.close()
				
				result = Tsv_to_list_dicts(input_file_3)
				output_file_3 = DatabasesDictionariesDir + "Enterobase_E coli_Complete genome_Metadata_list_3.txt"
				f = open(output_file_3, "w", encoding='utf-8')
				f.write(str(result))
				f.close()
				
				result = Tsv_to_list_dicts(input_file_4)
				output_file_4 = DatabasesDictionariesDir + "Enterobase_E coli_Complete genome_Metadata_list_4.txt"
				f = open(output_file_4, "w", encoding='utf-8')
				f.write(str(result))
				f.close()
				
				f = open(output_file_1, "r", encoding='utf-8')
				contents = f.read()
				f.close()
				dictionaries_list_1 = ast.literal_eval(contents)
				print('Major tsv file imported')
				
				f = open(output_file_2, "r", encoding='utf-8')
				contents = f.read()
				f.close()
				dictionaries_list_2 = ast.literal_eval(contents)
				print('MLST tsv file imported')
				
				f = open(output_file_3, "r", encoding='utf-8')
				contents = f.read()
				f.close()
				dictionaries_list_3 = ast.literal_eval(contents)
				print('Phylotyping tsv file imported')
				
				f = open(output_file_4, "r", encoding='utf-8')
				contents = f.read()
				f.close()
				dictionaries_list_4 = ast.literal_eval(contents)
				print('Serotyping tsv file imported')
				
				index = 'Uberstrain'
				
				dictionaries_list = Dictionaries_merger(dictionaries_list_1, dictionaries_list_2, dictionaries_list_3, dictionaries_list_4, index)
				
				output_file = DatabasesDictionariesDir + "Enterobase_E coli_Complete genome_Metadata_list.txt"
				f = open(output_file, "w", encoding='utf-8')
				f.write(str(dictionaries_list))
				f.close()
			
			else:
				print(f'\n\n\n\nFile(s) not found:\n\n{input_file_1}\n\nand / or\n\n{input_file_2}\n\nand / or\n\n {input_file_3}\n\nand / or\n\n{input_file_4}\n\n\n')
				option = 1
				Press_a_key(OperatingSystem, option)
			
			choice = ""
			Clear_screen(OperatingSystem)
			
		# (10) Browse Enterobase with keywords
		
		elif choice == "10":
			
			Clear_screen(OperatingSystem)
			
			print('You are using Enterobase.\n\n\n\n\n')
			
			print('Uploading Enterobase database to memory...')
			
			input_file = DatabasesDictionariesDir + "Enterobase_E coli_Complete genome_Metadata_list.txt"
			
			File_checking_result = File_checking(input_file)
			
			if File_checking_result == True:
			
				if EnterobaseCollection == []:
					f = open(input_file, "r", encoding='utf-8')
					contents = f.read()
					f.close()
					EnterobaseCollection = ast.literal_eval(contents)
				else:
					pass
				
				Collection = EnterobaseCollection
				
				Clear_screen(OperatingSystem)
				
				database = "Enterobase"
				
				Data_mining(database, Collection, DefaultDirectoryRoot, CustomDirectoryRoot)
			
			else:
				
				print(f'\n\n\n\nFile not found:\n\n{input_file}\n\n\n')
			
			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
			
		# (11) Browse Enterobase with field specific keywords
		
		elif choice == "11":
			
			Clear_screen(OperatingSystem)
			
			print('You are using Enterobase.\n\n\n\n\n')
			
			print('Uploading Enterobase database to memory...')
			
			input_file = DatabasesDictionariesDir + "Enterobase_E coli_Complete genome_Metadata_list.txt"
			
			File_checking_result = File_checking(input_file)
			
			if File_checking_result == True:
				
				if EnterobaseCollection == []:
					f = open(input_file, "r", encoding='utf-8')
					contents = f.read()
					f.close()
					EnterobaseCollection = ast.literal_eval(contents)
				else:
					pass
				
				Collection = EnterobaseCollection
				
				Clear_screen(OperatingSystem)
				
				database = "Enterobase"
				
				dict_key_options_tuple = ('species','collection year', 'collection month', 'country', 'source type', 'source niche', 'source details', 'serotype', 'simple patho', 'pathovar', 'stx1', 'stx2', 'ipah', 'pinv', 'st', 'lt', 'eae', 'clermont type (clermontyping)', 'clermont type (ezclermont)', 'fimh (fimtyper)', 'o antigen', 'h antigen', 'mlst st', 'mlst st complex', 'lineage', 'subspecies', 'adk', 'fumc', 'gyrb', 'icd', 'mdh', 'pura', 'reca')
				dict_key_options_menu = ('(1) Species\t\t(18) Clermont Type (ClermonTyping)\n(2) Collection Year\t(19) Clermont Type (EzClermont)\n(3) Collection Month\t(20) fimH (fimTyper)\n(4) Country\t\t(21) O Antigen\n(5) Source Type\t\t(22) H Antigen\n(6) Source Niche\t(23) MLST ST\n(7) Source Details\t(24) MLST ST Complex\n(8) Serotype\t\t(25) Lineage\n(9) Simple Patho\t(26) Subspecies\n(10) Pathovar\t\t(27) adk\n(11) Stx1\t\t(28) fumC\n(12) Stx2\t\t(29) gyrB\n(13) ipaH\t\t(30) icd\n(14) pInv\t\t(31) mdh\n(15) ST\t\t\t(32) purA\n(16) LT\t\t\t(33) recA\n(17) eae\n')
				options = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33')
				
				Data_mining_searching_dict_keys(database, Collection, dict_key_options_tuple, dict_key_options_menu, options, DefaultDirectoryRoot, CustomDirectoryRoot)
			
			else:
				
				print(f'\n\n\n\nFile not found:\n\n{input_file}\n\n\n')
			
			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
			
		# (12) Fetch Enterobase isolates’ metadata with keywords
		
		elif choice == "12":
			
			Clear_screen(OperatingSystem)
			
			print('You are using Enterobase.\n\n\n\n\n')
			
			print('Uploading Enterobase database to memory...')
			
			input_file = DatabasesDictionariesDir + "Enterobase_E coli_Complete genome_Metadata_list.txt"
			
			File_checking_result = File_checking(input_file)
			
			if File_checking_result == True:
				
				if EnterobaseCollection == []:
					f = open(input_file, "r", encoding='utf-8')
					contents = f.read()
					f.close()
					EnterobaseCollection = ast.literal_eval(contents)
				else:
					pass
				
				Collection = EnterobaseCollection
				
				database = 'Enterobase'
				accession_number_field = 'sample id'
				
				keep_entry_key = 'keep entry'
				keep_entry_val = 'y'
				
				isolate_name_key = 'uberstrain'
				species_key = 'species'
				Collection_year_key = 'collection year'
				Collection_month_key = 'collection month'
				isolation_country_key = 'country'
				source_type_key = 'source type'
				source_niche_key = 'source niche'
				source_details_key = 'source details'
				serovar_key = 'serotype'
				pathovar_1_key = 'simple patho'
				pathovar_2_key = 'pathovar'
				virulence_profile_stx1_key = 'stx1'
				virulence_profile_stx2_key = 'stx2'
				virulence_profile_ipah_key = 'ipah'
				virulence_profile_pinv_key = 'pinv'
				virulence_profile_st_key = 'st'
				virulence_profile_lt_key = 'lt'
				virulence_profile_eae_key = 'eae'
				clermont_type_1_key = 'clermont type (clermontyping)'
				clermont_type_2_key = 'clermont type (ezclermont)'
				fimh_type_key = 'fimh (fimtyper)'
				serogroup_key = 'o antigen'
				serotype_key = 'h antigen'
				st_type_key = 'mlst st'
				st_complex_key = 'mlst st complex'
				lineage_key = 'lineage'
				subspecies_key = 'subspecies'
				adk_key = 'adk'
				fumC_key = 'fumc'
				gyrB_key = 'gyrb'
				icd_key = 'icd'
				mdh_key = 'mdh'
				purA_key = 'pura'
				recA_key = 'reca'
				assembly_id_key = 'assembly barcode'
				genome_quality_key = 'status'
				
				isolates_metadata_keys = (isolate_name_key, accession_number_field, species_key, Collection_year_key, Collection_month_key, isolation_country_key, source_type_key, source_niche_key, source_details_key, serovar_key, pathovar_1_key, pathovar_2_key, virulence_profile_stx1_key, virulence_profile_stx2_key, virulence_profile_ipah_key, virulence_profile_pinv_key, virulence_profile_st_key, virulence_profile_lt_key, virulence_profile_eae_key, clermont_type_1_key, clermont_type_2_key, fimh_type_key, serogroup_key, serotype_key, st_type_key, st_complex_key, lineage_key, subspecies_key, adk_key, fumC_key, gyrB_key, icd_key, mdh_key, purA_key, recA_key, assembly_id_key, genome_quality_key)
		
				metadata_file = SamplesMetadataDir + 'Enterobase isolates metadata.txt'
				metadata_csv_file = SamplesMetadataDir + 'Enterobase isolates metadata.csv'
				
				metadata_csv_file_headers = ('Isolate name' + ',' + 'Biosample accession' + ',' + 'Species' + ',' + 'Collection year' + ',' + 'Collection month' + ',' + 'Isolation country' + ',' + 'Isolation source type' + ',' + 'Source niche' + ',' + 'Source details' + ',' + 'Serovar' + ',' + 'Pathovar 1' + ',' + 'Pathovar 2' + ',' +  'Stx1' + ',' + 'Stx2' + ',' + 'ipaH' + ',' + 'pInv' + ',' + 'ST' + ',' + 'LT' + ',' + 'eae' + ',' + 'Clermont type' + ',' + 'Ez Clermont type' + ',' + 'FimH type' + ',' + 'O Antigen' + ',' + 'H Antigen' + ',' + 'MLST ST' + ',' + 'MLST ST Complex' + ',' + 'Lineage' + ',' + 'Subspecies' + ',' + 'adk' + ',' + 'fumC' + ',' + 'gyrB' + ',' + 'icd' + ',' + 'mdh' + ',' + 'purA' + ',' + 'recA' + ',' + 'Assembly id' + ',' + 'Genome quality' + ',' + 'Keep entry?' + '\n')
	
				statistics_file = SamplesMetadataDir + 'Enterobase isolates metadata for statistics.txt'
				statistics_csv_file = SamplesMetadataDir + 'Enterobase isolates metadata for statistics.csv'
				
				sampling_report_file = ReportsDir + 'Enterobase sampling report.txt'
				
				Clear_screen(OperatingSystem)
				
				Fetch_accession_numbers(Collection, database, accession_number_field, keep_entry_key, keep_entry_val, isolates_metadata_keys, metadata_file, metadata_csv_file, metadata_csv_file_headers, statistics_file, statistics_csv_file, sampling_report_file, DefaultDirectoryRoot, CustomDirectoryRoot)
			
			else:
				
				print(f'\n\n\n\nFile not found:\n\n{input_file}\n\n\n')
			
			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)

		# (13) Fetch Enterobase isolates’ metadata with field specific keywords
		
		elif choice == "13":
			
			Clear_screen(OperatingSystem)
			
			print('You are using Enterobase.\n\n\n\n\n')
			
			print('Uploading Enterobase database to memory...')
			
			input_file = DatabasesDictionariesDir + "Enterobase_E coli_Complete genome_Metadata_list.txt"
			
			File_checking_result = File_checking(input_file)
			
			if File_checking_result == True:
				
				if EnterobaseCollection == []:
					f = open(input_file, "r", encoding='utf-8')
					contents = f.read()
					f.close()
					EnterobaseCollection = ast.literal_eval(contents)
				else:
					pass
				
				Collection = EnterobaseCollection
				
				database = 'Enterobase'
				accession_number_field = 'sample id'
				
				keep_entry_key = 'keep entry'
				keep_entry_val = 'y'
				
				isolate_name_key = 'uberstrain'
				species_key = 'species'
				Collection_year_key = 'collection year'
				Collection_month_key = 'collection month'
				isolation_country_key = 'country'
				source_type_key = 'source type'
				source_niche_key = 'source niche'
				source_details_key = 'source details'
				serovar_key = 'serotype'
				pathovar_1_key = 'simple patho'
				pathovar_2_key = 'pathovar'
				virulence_profile_stx1_key = 'stx1'
				virulence_profile_stx2_key = 'stx2'
				virulence_profile_ipah_key = 'ipah'
				virulence_profile_pinv_key = 'pinv'
				virulence_profile_st_key = 'st'
				virulence_profile_lt_key = 'lt'
				virulence_profile_eae_key = 'eae'
				clermont_type_1_key = 'clermont type (clermontyping)'
				clermont_type_2_key = 'clermont type (ezclermont)'
				fimh_type_key = 'fimh (fimtyper)'
				serogroup_key = 'o antigen'
				serotype_key = 'h antigen'
				st_type_key = 'mlst st'
				st_complex_key = 'mlst st complex'
				lineage_key = 'lineage'
				subspecies_key = 'subspecies'
				adk_key = 'adk'
				fumC_key = 'fumc'
				gyrB_key = 'gyrb'
				icd_key = 'icd'
				mdh_key = 'mdh'
				purA_key = 'pura'
				recA_key = 'reca'
				assembly_id_key = 'assembly barcode'
				genome_quality_key = 'status'
				
				isolates_metadata_keys = (isolate_name_key, accession_number_field, species_key, Collection_year_key, Collection_month_key, isolation_country_key, source_type_key, source_niche_key, source_details_key, serovar_key, pathovar_1_key, pathovar_2_key, virulence_profile_stx1_key, virulence_profile_stx2_key, virulence_profile_ipah_key, virulence_profile_pinv_key, virulence_profile_st_key, virulence_profile_lt_key, virulence_profile_eae_key, clermont_type_1_key, clermont_type_2_key, fimh_type_key, serogroup_key, serotype_key, st_type_key, st_complex_key, lineage_key, subspecies_key, adk_key, fumC_key, gyrB_key, icd_key, mdh_key, purA_key, recA_key, assembly_id_key, genome_quality_key)
				
				metadata_file = SamplesMetadataDir + 'Enterobase isolates metadata.txt'
				metadata_csv_file = SamplesMetadataDir + 'Enterobase isolates metadata.csv'
				
				metadata_csv_file_headers = ('Isolate name' + ',' + 'Biosample accession' + ',' + 'Species' + ',' + 'Collection year' + ',' + 'Collection month' + ',' + 'Isolation country' + ',' + 'Isolation source type' + ',' + 'Source niche' + ',' + 'Source details' + ',' + 'Serovar' + ',' + 'Pathovar 1' + ',' + 'Pathovar 2' + ',' +  'Stx1' + ',' + 'Stx2' + ',' + 'ipaH' + ',' + 'pInv' + ',' + 'ST' + ',' + 'LT' + ',' + 'eae' + ',' + 'Clermont type' + ',' + 'Ez Clermont type' + ',' + 'FimH type' + ',' + 'O Antigen' + ',' + 'H Antigen' + ',' + 'MLST ST' + ',' + 'MLST ST Complex' + ',' + 'Lineage' + ',' + 'Subspecies' + ',' + 'adk' + ',' + 'fumC' + ',' + 'gyrB' + ',' + 'icd' + ',' + 'mdh' + ',' + 'purA' + ',' + 'recA' + ',' + 'Assembly id' + ',' + 'Genome quality' + ',' + 'Keep entry?' + '\n')
				
				statistics_file = SamplesMetadataDir + 'Enterobase isolates metadata for statistics.txt'
				statistics_csv_file = SamplesMetadataDir + 'Enterobase isolates metadata for statistics.csv'
				
				sampling_report_file = ReportsDir + 'Enterobase sampling report.txt'
				
				dict_key_options_tuple = ('species','collection year', 'collection month', 'country', 'source type', 'source niche', 'source details', 'serotype', 'simple patho', 'pathovar', 'stx1', 'stx2', 'ipah', 'pinv', 'st', 'lt', 'eae', 'clermont type (clermontyping)', 'clermont type (ezclermont)', 'fimh (fimtyper)', 'o antigen', 'h antigen', 'mlst st', 'mlst st complex', 'lineage', 'subspecies', 'adk', 'fumc', 'gyrb', 'icd', 'mdh', 'pura', 'reca')
				dict_key_options_menu = ('(1) Species\t\t\t(18) Clermont Type (ClermonTyping)\n(2) Collection Year\t\t(19) Clermont Type (EzClermont)\n(3) Collection Month\t\t(20) fimH (fimTyper)\n(4) Country\t\t\t(21) O Antigen\n(5) Source Type\t\t\t(22) H Antigen\n(6) Source Niche\t\t(23) MLST ST\n(7) Source Details\t\t(24) MLST ST Complex\n(8) Serotype\t\t\t(25) Lineage\n(9) Simple Patho\t\t(26) Subspecies\n(10) Pathovar\t\t\t(27) adk\n(11) Stx1\t\t\t(28) fumC\n(12) Stx2\t\t\t(29) gyrB\n(13) ipaH\t\t\t(30) icd\n(14) pInv\t\t\t(31) mdh\n(15) ST\t\t\t\t(32) purA\n(16) LT\t\t\t\t(33) recA\n(17) eae\n')
				options = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33')
				
				Clear_screen(OperatingSystem)
	
				Fetch_accession_numbers_searching_dict_keys(Collection, database, accession_number_field, keep_entry_key, keep_entry_val, isolates_metadata_keys, metadata_file, metadata_csv_file, metadata_csv_file_headers, statistics_file, statistics_csv_file, sampling_report_file, dict_key_options_tuple, dict_key_options_menu, options, DefaultDirectoryRoot, CustomDirectoryRoot)
			
			else:
				
				print(f'\n\n\n\nFile not found:\n\n{input_file}\n\n\n')
			
			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
			
		# (14) Exclude / Reinclude Enterobase isolates’ from sample
		
		elif choice == "14":
			
			Clear_screen(OperatingSystem)
			
			print('You are using Enterobase.\n')
			
			accession_number_field = 'biosample accession'
			
			metadata_csv_file = SamplesMetadataDir + 'Enterobase isolates metadata.csv'
			accession_numbers_file = SamplesAccessionNumbersDir + 'Enterobase_accession numbers.txt'
			accession_numbers_BU_file = SamplesAccessionNumbersDir + 'Enterobase_accession numbers_BU.txt'
			removed_accession_numbers_file = SamplesAccessionNumbersDir + 'Enterobase_accession numbers_RM.txt'
			
			File_checking_result = File_checking(metadata_csv_file)
			file1 = File_checking_result
			File_checking_result = File_checking(accession_numbers_file)
			file2 = File_checking_result
			
			if file1 == True and file2 == True:
				
				Clear_screen(OperatingSystem)
				
				Edit_accession_numbers_list(accession_number_field, metadata_csv_file, accession_numbers_file, accession_numbers_BU_file, removed_accession_numbers_file, DefaultDirectoryRoot, CustomDirectoryRoot)
				
			else:
				
				print(f'\n\n\n\nFile(s) not found:\n\n{metadata_csv_file}\n\nand / or\n\n{accession_numbers_file}not found!\n\n\n')
				option = 1
				Press_a_key(OperatingSystem, option)
			
			choice = ""
			Clear_screen(OperatingSystem)
		
		# (15) Describe Enterobase sample with tables
		
		elif choice == "15":
			
			Clear_screen(OperatingSystem)
			
			print('You are using Enterobase.\n\n\n\n\n')
			
			database = 'Enterobase'
			graphics_option = 'n'
			
			species_key = 'Species'
			Collection_year_key = 'Collection year'
			isolation_country_key = 'Isolation country'
			pathovar_2_key = 'Pathovar 2'
			serogroup_key = 'O Antigen'
			serotype_key = 'H Antigen'
			st_type_key = 'MLST ST'
			st_complex_key = 'MLST ST Complex'
			source_type_key = 'Isolation source type'
			
			isolates_metadata_keys = (species_key, Collection_year_key, isolation_country_key, pathovar_2_key, serogroup_key, serotype_key, st_type_key, st_complex_key, source_type_key)
			
			statistics_csv_file = SamplesMetadataDir + 'Enterobase isolates metadata for statistics.csv'
			sample_summary_file = SamplesMetadataDir + 'Enterobase isolates metadata summary.txt'
			
			File_checking_result = File_checking(statistics_csv_file)
			
			if File_checking_result == True:
				
				Clear_screen(OperatingSystem)
				
				Summarize(graphics_option, isolates_metadata_keys, statistics_csv_file, database, sample_summary_file, DefaultDirectoryRoot, CustomDirectoryRoot)
			
			else:
				
				print(f'\n\n\n\nFile(s) not found:\n\n{statistics_csv_file}\n\nand / or\n\n{sample_summary_file}\n\n\n')
			
			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
		
		# (16) Describe Enterobase sample with graphics
		
		elif choice == "16":
			
			Clear_screen(OperatingSystem)
			
			print('You are using Enterobase.\n\n\n\n\n')
			
			database = 'Enterobase'
			graphics_option = 'y'
			
			species_key = 'Species'
			Collection_year_key = 'Collection year'
			isolation_country_key = 'Isolation country'
			pathovar_2_key = 'Pathovar 2'
			serogroup_key = 'O Antigen'
			serotype_key = 'H Antigen'
			st_type_key = 'MLST ST'
			st_complex_key = 'MLST ST Complex'
			source_type_key = 'Isolation source type'
			
			isolates_metadata_keys = (species_key, Collection_year_key, isolation_country_key, pathovar_2_key, serogroup_key, serotype_key, st_type_key, st_complex_key, source_type_key)
			
			statistics_csv_file = SamplesMetadataDir + 'Enterobase isolates metadata for statistics.csv'
			sample_summary_file = SamplesMetadataDir + 'Enterobase isolates metadata summary.txt'
			
			File_checking_result = File_checking(statistics_csv_file)
			
			if File_checking_result == True:
			
				Clear_screen(OperatingSystem)
				
				Summarize(graphics_option, isolates_metadata_keys, statistics_csv_file, database, sample_summary_file, DefaultDirectoryRoot, CustomDirectoryRoot)
			
			else:
				
				print(f'\n\n\n\nFile(s) not found:\n\n{statistics_csv_file}\n\nand / or\n\n{sample_summary_file}\n\n\n')
			
			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
		
		# (40) Fetch sample isolates’ DNA sequences from NCBI
		
		elif choice == "40":
			
			Clear_screen(OperatingSystem)
			
			input_file = str(SamplesAccessionNumbersDir)+'accession numbers.txt'
			output_file_root = str(DownloadedSequencesDir)
			report_file = ReportsDir + 'sequences download report.txt'
			fasta_headers_file = ReportsDir + 'fasta headers.txt'
			
			NCBI_sequence_download(input_file,output_file_root, report_file, fasta_headers_file, DefaultDirectoryRoot, CustomDirectoryRoot)
			
			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
			
		# (50) Quit
		
		elif choice == "50":
			
			Clear_screen(OperatingSystem)
			
			Bye()
		
		# (t - hidden) Routine under testing
		
		elif choice == "t":
			
			Clear_screen(OperatingSystem)
			
			# Add new code here
			
		else:
			
			print ('\nI didn\'t understand your \'input\': you must enter 0 to 16, 40 or 50!\n')
			
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
	
###############################
##                           ##
##  OPERATIONAL SUBROUTINES  ##
##                           ##
###############################
	
# Directories set up routine
			
def Default_directory_set_up():
	
	global SampleMinerDataDir, DefaultDirectoryRoot, DatabasesTsvFilesDir, DatabasesDictionariesDir, MinedSamplesDir, SamplesAccessionNumbersDir, DownloadedSequencesDir, ReportsDir, SamplesMetadataDir
	
	SampleMinerDataDir = str(CurrentUserRootDir) + str("/Documents/SampleMiner/")
	MinedSamplesDir = str(CurrentUserRootDir) + str("/Documents/SampleMiner/mined samples/")
	DefaultDirectoryRoot = str(CurrentUserRootDir) + str("/Documents/SampleMiner/mined samples/default/")
	DatabasesTsvFilesDir = str(CurrentUserRootDir) + str("/Documents/SampleMiner/databases tsv files/")
	DatabasesDictionariesDir = str(CurrentUserRootDir) + str("/Documents/SampleMiner/databases dictionaries/")
	SamplesAccessionNumbersDir = str(CurrentUserRootDir) + str("/Documents/SampleMiner/mined samples/default/samples accession numbers/")
	DownloadedSequencesDir = str(CurrentUserRootDir) + str("/Documents/SampleMiner/mined samples/default/downloaded sequences/")
	ReportsDir = str(CurrentUserRootDir) + str("/Documents/SampleMiner/mined samples/default/reports/")
	SamplesMetadataDir = str(CurrentUserRootDir) + str("/Documents/SampleMiner/mined samples/default/samples metadata/")
	
	Check_directory(SampleMinerDataDir)
	Check_directory(MinedSamplesDir)
	Check_directory(DefaultDirectoryRoot)
	Check_directory(DatabasesTsvFilesDir)
	Check_directory(DatabasesDictionariesDir)
	Check_directory(SamplesAccessionNumbersDir)
	Check_directory(DownloadedSequencesDir)
	Check_directory(ReportsDir)
	Check_directory(SamplesMetadataDir)
	
# Custom directories set up routine

def Custom_directories_set_up(CustomDirectory):
	
	global CustomDirectoryRoot, SamplesAccessionNumbersDir, DownloadedSequencesDir, ReportsDir, SamplesMetadataDir
	
	CustomDirectoryRoot = str(CurrentUserRootDir) + '/Documents/SampleMiner/mined samples/' + str(CustomDirectory)
	SamplesAccessionNumbersDir = str(CurrentUserRootDir) + '/Documents/SampleMiner/mined samples/' + str(CustomDirectory) + '/samples accession numbers/'
	DownloadedSequencesDir = str(CurrentUserRootDir) + '/Documents/SampleMiner/mined samples/' + str(CustomDirectory) + '/downloaded sequences/'
	ReportsDir = str(CurrentUserRootDir) + '/Documents/SampleMiner/mined samples/' + str(CustomDirectory) + '/reports/'
	SamplesMetadataDir = str(CurrentUserRootDir) + '/Documents/SampleMiner/mined samples/' + str(CustomDirectory) + '/samples metadata/'
	
	Check_directory(CustomDirectoryRoot)
	Check_directory(SamplesAccessionNumbersDir)
	Check_directory(DownloadedSequencesDir)
	Check_directory(ReportsDir)
	Check_directory(SamplesMetadataDir)

# TSV file to list of dictionaries importation routine

def Tsv_to_list_dicts(input_file):
	
	f = open(input_file, "r", encoding='utf-8')
	keys = [val.replace('"','').replace('\'','').replace(';',' / ').replace(',',' / ').strip().lower() for val in f.readline().split("\t")]
	result = []
	
	for line in f:
		line = [val.replace('"','').replace('\'','').replace(';',' / ').replace(',',' / ').strip().lower() for val in line.split("\t")]
		result.append({key: val for key, val in zip(keys, line)})
	f.close()
	
	return result

# CSV file to list of dictionaries importation routine

def Csv_to_list_dicts(input_file):
	
	f = open(input_file, "r", encoding='utf-8')
	keys = [val.replace('"','').replace('\'','').replace(',',' / ').strip().lower() for val in f.readline().split(";")]
	result = []
	
	for line in f:
		line = [val.replace('"','').replace('\'','').strip().lower() for val in line.split(";")]
		result.append({key: val for key, val in zip(keys, line)})
	f.close()
	
	return result

# Dictionaries merge routine

def Dictionaries_merger(dictionaries_list_1, dictionaries_list_2, dictionaries_list_3, dictionaries_list_4, index):
	
	dictionaries_list = []
	
	dictionaries_list_1_length = len(dictionaries_list_1)
	total_dictionaries = 4 * dictionaries_list_1_length
	
	print(f'\n\nStarting merge of {total_dictionaries} into {dictionaries_list_1_length} dictionaries\n\n')
	
	for dictionary in range(len(dictionaries_list_1)):
		
		appended_dictionary = {}
		
		val_key1_dict_1 = dictionaries_list_1[dictionary].get(index)
		val_key1_dict_2 = dictionaries_list_2[dictionary].get(index)
		val_key1_dict_3 = dictionaries_list_3[dictionary].get(index)
		val_key1_dict_4 = dictionaries_list_4[dictionary].get(index)
		
		for key in dictionaries_list_1[dictionary]:
			k = key
			v = dictionaries_list_1[dictionary].get(k)
			appended_dictionary.update({k:v})
			
		if val_key1_dict_1 == val_key1_dict_2:
			
			for key in dictionaries_list_2[dictionary]:
				k = key
				v = dictionaries_list_2[dictionary].get(k)
				appended_dictionary.update({k:v})
				
		else:
			
			for item in dictionaries_list_2:
				
				if val_key1_dict_1 in item.values():
					
					for key in item:
						k = key
						v = item.get(k)
						appended_dictionary.update({k:v})
						
					break
				
		if val_key1_dict_1 == val_key1_dict_3:
			
			for key in dictionaries_list_3[dictionary]:
				k = key
				v = dictionaries_list_3[dictionary].get(k)
				appended_dictionary.update({k:v})
				
		else:
			
			for item in dictionaries_list_3:
				
				if val_key1_dict_1 in item.values():
					
					for key in item:
						k = key
						v = item.get(k)
						appended_dictionary.update({k:v})
						
					break
				
		if val_key1_dict_1 == val_key1_dict_4:
			
			for key in dictionaries_list_4[dictionary]:
				k = key
				v = dictionaries_list_4[dictionary].get(k)
				appended_dictionary.update({k:v})
				
		else:
			
			for item in dictionaries_list_4:
				
				if val_key1_dict_1 in item.values():
					
					for key in item:
						k = key
						v = item.get(k)
						appended_dictionary.update({k:v})
						
					break
				
		dictionaries_list.append(appended_dictionary)
		
		counter = dictionary + 1
		
		print(f'Number of dictionaries appended to list: {counter} (from a total of {dictionaries_list_1_length})\n')
		
	return dictionaries_list

# Free input database browsing routine

def Data_mining(database, Collection, DefaultDirectoryRoot, CustomDirectoryRoot):
	
	Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot)
	
	print(f'\n\nYou are using {database}.\n\n\n')
	
	print('Enter one keyword at a time then just enter:\n\n\t"-" to conclude current set of keywords\n\n\t"--" to conclude all keyword sets\n\n\n\n')
	
	keyword = ''
	keywords = []
	keywords_set = {}
	isolate = {}
	lower_case_isolate = {}
	
	keywords_set_count = 0
	while keyword != '--':
		keywords = []
		keyword = ''
		keywords_set_count = keywords_set_count + 1
		keyword_count = 0
		print(f'Keywords set {keywords_set_count}')
		while keyword != '-' and keyword != '--':
			keyword_count = keyword_count + 1
			keyword = input(f'Please, enter keyword {keyword_count}:')
			if keyword == '-' and keyword_count == 1:
				keywords_set_count = keywords_set_count -1
			if keyword == '-' or keyword == '--':
				break
			keywords.append(keyword.lower())
			item = {keywords_set_count : keywords}
			keywords_set.update(item)
	
	if keywords_set != {}:
	
		Clear_screen(OperatingSystem)
		
		Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot)
		
		print(f'\n\nYou are using {database}.\n')
		
		keywords_set_count = 0
		print('\n\nThese are the keywords you entered:')
		for keywords in keywords_set.values():
			keywords_set_count = keywords_set_count + 1
			print(f'\nKeywords set {keywords_set_count}')
			for i in range(len(keywords)):
				print(f'Keyword {i + 1} = ', keywords[i])
		
		n = len(Collection)
		
		print (f"\n\nThe Collection has {n} isolates\n")
		
		print ('\nSearching...\n')
		
		positive_isolate_count = 0
		positive_isolate_count_stratified = []
		
		for i in range(len(keywords_set)):
			positive_isolate_count_stratified.append(0)
		
		for isolate in Collection:
				
			for item_key in keywords_set:
				keywords = keywords_set[item_key]
				record = ''
				
				for value in isolate.values():
					record = record + str(value)
					
				for keyword in keywords:
					if record.find(keyword) < 0:
						break
					elif keywords.index(keyword) + 1 == len(keywords):
						positive_isolate_count = positive_isolate_count + 1
						a = positive_isolate_count_stratified[item_key - 1]
						a = a + 1
						positive_isolate_count_stratified[item_key - 1] = a
						break
	
		Clear_screen(OperatingSystem)
		
		Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot)
		
		print(f'\n\nYou are using {database}.')
		print (f"\n\n\nThe Collection has {n} isolates.")
		print(f"\nThere are {positive_isolate_count} isolates that satisfy the entered sets of keywords.")
		print('\nBelow is the stratification per Keyword set:')
		
		for item_key in keywords_set:
			print(f'\nKeywords set {item_key}')
			keywords = keywords_set[item_key]
			for i in range(len(keywords)):
				print(f'Keyword {i + 1} = ', keywords[i])
			print('Total hits = ', positive_isolate_count_stratified[item_key - 1])
	
	else:
		pass
		
# Dictionary keys specific database browsing routine
		
def Data_mining_searching_dict_keys(database, Collection, dict_key_options_tuple, dict_key_options_menu, options, DefaultDirectoryRoot, CustomDirectoryRoot):
	
	Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot)
	
	print(f'\n\nYou are using {database}.\n\n\n')
	
	dictionary_key = ''
	keyword = ''
	keywords = {}
	keywords_set = {}
	isolate = {}
	lower_case_isolate = {}
	
	keywords_set_count = 0
	while dictionary_key != '--':
		
		dictionary_key = ''
		keywords = {}
		keyword = ''
		keywords_set_count = keywords_set_count + 1
		keyword_count = 0
		
		Clear_screen(OperatingSystem)
		
		Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot)
		
		print(f'\n\nYou are using {database}.')
		print(f'\n\n\nThese are {database} field options:\n\n{dict_key_options_menu}')
		print('\n\n\nEnter one pair of field / keyword at a time then just enter:\n\n\t"-" to conclude current set of keywords\n\n\t"--" to conclude all keyword sets\n\n\n')
		print(f'Keywords set {keywords_set_count}')
		
		while True:
			keyword_count = keyword_count + 1
			dictionary_key = ''
			while not dictionary_key in options[0:] and not dictionary_key in ('-','--'):
				dictionary_key = str(input(f'Please, enter field {keyword_count}:'))
			if dictionary_key == '-' and keyword_count == 1:
				keywords_set_count = keywords_set_count -1
			if dictionary_key == '-' or dictionary_key == '--':
				break
			keyword = input(f'Please, enter field {keyword_count}\'s keyword:')
			keyword = keyword.lower()
			entry = {dict_key_options_tuple[int(dictionary_key) - 1]:keyword}
			keywords.update(entry)
			item = {keywords_set_count : keywords}
			keywords_set.update(item)
			
	if keywords_set != {}:
		
		Clear_screen(OperatingSystem)
		
		Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot)
		
		print(f'\n\nYou are using {database}.\n')
		
		print('\n\nThese are the fields / keywords pairs you entered:')
		
		keywords_set_count = 0
		for keywords in keywords_set:
			kv_pairs = {}
			keywords_set_count = keywords_set_count + 1
			print(f'\nKeywords set {keywords_set_count}\n')
			kv_pairs.update(keywords_set[keywords_set_count])
			field = 0
			for i in kv_pairs:
				field = field + 1
				print(f'Field {field}: {i}\nKeyword: {kv_pairs[i]}\n')
				
		n = len(Collection)
		
		print (f"\n\nThe Collection has {n} isolates\n")
		
		print ('\nSearching...\n')
		
		positive_isolate_count = 0
		positive_isolate_count_stratified = []
		
		for i in range(len(keywords_set)):
			positive_isolate_count_stratified.append(0)

		for isolate in Collection:

			item_count = 0
			for item in keywords_set:
				item_count = item_count + 1
				kv_pairs = keywords_set[item]
				
				kv_count = 0
				for k in kv_pairs:
					kv_count = kv_count + 1
					lci_k = str(k)
					if not kv_pairs[k] in isolate[lci_k]:
						break
					elif kv_count == len(kv_pairs):
						positive_isolate_count = positive_isolate_count + 1
						a = positive_isolate_count_stratified[item_count - 1]
						a = a + 1
						positive_isolate_count_stratified[item_count - 1] = a
						break
					
		Clear_screen(OperatingSystem)
		
		Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot)
		
		print(f'\n\nYou are using {database}.')
		print (f"\n\n\nThe Collection has {n} isolates.")
		print(f"\nThere are {positive_isolate_count} isolates that satisfy the entered sets of keywords.")
		print('\nBelow is the stratification per Keyword set:')
		
		keywords_set_count = 0
		for keywords in keywords_set:
			kv_pairs = {}
			keywords_set_count = keywords_set_count + 1
			print(f'\nKeywords set {keywords_set_count}\n')
			kv_pairs.update(keywords_set[keywords_set_count])
			field = 0
			for i in kv_pairs:
				field = field + 1
				print(f'Field {field}: {i}\nKeyword: {kv_pairs[i]}\n')
			print('Total hits = ', positive_isolate_count_stratified[keywords - 1])
		
	else:
		pass
		
#  Free input database's NCBI-Biosample accession numbers fetching routine
			
def Fetch_accession_numbers(Collection, database, accession_number_field, keep_entry_key, keep_entry_val, isolates_metadata_keys, metadata_file, metadata_csv_file, metadata_csv_file_headers, statistics_file, statistics_csv_file, sampling_report_file, DefaultDirectoryRoot, CustomDirectoryRoot):
	
	Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot)
	
	srf = open(sampling_report_file, 'w', encoding='utf-8')
	
	print(f'\n\nYou are using {database}.\n\n')
	
	print('\nEnter one keyword at a time then just enter:\n\n\t"-"to conclude current set of keywords\n\n\t"--" to conclude all keyword sets\n\n\n\n')
	
	keyword = ''
	keywords = []
	keywords_set = {}
	isolate = {}
	lower_case_isolate = {}
	accession_number = ""
	accession_numbers_list = []
	accession_numbers_counts = 0
		
	keywords_set_count = 0
	while keyword != '--':
		keywords = []
		keyword = ''
		keywords_set_count = keywords_set_count + 1
		keyword_count = 0
		print(f'Keywords set {keywords_set_count}')
		while keyword != '-' and keyword != '--':
			keyword_count = keyword_count + 1
			keyword = input(f'Please, enter keyword {keyword_count}:')
			if keyword == '-' and keyword_count == 1:
				keywords_set_count = keywords_set_count -1
			if keyword == '-' or keyword == '--':
				break
			keywords.append(keyword.lower())
			item = {keywords_set_count : keywords}
			keywords_set.update(item)
	
	if keywords_set != {}:
	
		Clear_screen(OperatingSystem)
		
		Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot)
		
		print(f'\n\nYou are using {database}.\n\n')
		
		attribute = f'You are using {database}.\n\n\n'
		srf.write(attribute)
		
		keywords_set_count = 0
		
		print('\nThese are the keywords you entered:')
		attribute = 'These are the keywords you entered:\n\n'
		srf.write(attribute)
		
		for keywords in keywords_set.values():
			keywords_set_count = keywords_set_count + 1
			print(f'\nKeywords set {keywords_set_count}')
			attribute = f'Keywords set {keywords_set_count}\n'
			srf.write(attribute)
			
			for i in range(len(keywords)):
				print(f'Keyword {i + 1} = ', keywords[i])				
				attribute = f'Keyword {i + 1} = {keywords[i]}\n'
				srf.write(attribute)
				
		n = len(Collection)
		
		print (f"\n\nThe Collection has {n} isolates\n")
		
		print ('\nSearching...\n')
		
		positive_isolate_count = 0
		positive_isolate_count_stratified = []
		
		for i in range(len(keywords_set)):
			positive_isolate_count_stratified.append(0)
	
		im = open(metadata_file, 'w', encoding='utf-8')
		im.write('[\n')
		
		imcsv = open(metadata_csv_file, 'w', encoding='utf-8')
		imcsv.write(metadata_csv_file_headers)
	
		isolate_count = -1
		for isolate in Collection:
			
			isolate_count = isolate_count + 1
				
			for item_key in keywords_set:
				keywords = keywords_set[item_key]
				record = ''
				
				for value in isolate.values():
					record = record + ' \ ' + str(value)
				
				for keyword in keywords:
					if record.find(keyword) < 0:
						break
					elif keywords.index(keyword) + 1 == len(keywords):
						positive_isolate_count = positive_isolate_count + 1
						a = positive_isolate_count_stratified[item_key - 1]
						a = a + 1
						positive_isolate_count_stratified[item_key - 1] = a
						accession_number = isolate[accession_number_field]
						if accession_number != '' and not accession_number in accession_numbers_list:
							accession_numbers_list.append(accession_number)
							Metadata_retrieval_routine(Collection, isolate_count, accession_number_field, keep_entry_key, keep_entry_val, accession_number, isolates_metadata_keys, im, imcsv)
						else:
							pass
						break
			
		im.write(']')
		im.close()
		
		imcsv.close()
		
		statfile = shutil.copy2(metadata_file, statistics_file)
		statcsvfile = shutil.copy2(metadata_csv_file, statistics_csv_file)
		
		Clear_screen(OperatingSystem)
		
		Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot)
		
		print(f'\n\nYou are using {database}.')
		print (f"\n\n\nThe Collection has {n} isolates.")
		print(f"\nThere are {positive_isolate_count} isolates that satisfy the entered sets of keywords.")
		print('\nBelow is the stratification per Keyword set:')
		
		attribute = f"\n\nThe Collection has {n} isolates.\n\n"
		srf.write(attribute)
		attribute = f"There are {positive_isolate_count} isolates that satisfy the entered sets of keywords.\n\n"
		srf.write(attribute)
		attribute = 'Below is the stratification per Keyword set:\n\n'
		srf.write(attribute)
		
		for item_key in keywords_set:
			print(f'\nKeywords set {item_key}')
			attribute = f'Keywords set {item_key}\n\n'
			srf.write(attribute)
			
			keywords = keywords_set[item_key]
			
			for i in range(len(keywords)):
				print(f'Keyword {i + 1} = ', keywords[i])
				attribute = f'Keyword {i + 1} = {keywords[i]}\n'
				srf.write(attribute)
				
			print('Total hits = ', positive_isolate_count_stratified[item_key - 1])
			attribute = f'Total hits = {positive_isolate_count_stratified[item_key - 1]}\n\n'
			srf.write(attribute)
		
		f = open(str(SamplesAccessionNumbersDir) + str(database) + '_accession numbers.txt', "w", encoding='utf-8')
		contents = f.write(str(accession_numbers_list))
		f.close()
		
		accession_numbers_list = Consolidate_list(accession_numbers_list)
		
		accession_numbers_counts = len(accession_numbers_list)
		
		print(f'\nThe NCBI sequence accession numbers of {accession_numbers_counts} unique isolates could be retrieved.')
		print('\nThis is your list of accession numbers:\n\n',accession_numbers_list)
		print(f'\n\nYou can find your list of accession numbers in directory: \n\n\t"{SamplesAccessionNumbersDir}"')
		
		attribute = f'The NCBI sequence accession numbers of {accession_numbers_counts} unique isolates could be retrieved.\n\n'
		srf.write(attribute)
		attribute = f'This is your list of accession numbers:\n\n{accession_numbers_list}\n\n'
		srf.write(attribute)
		attribute = f'You can find your list of accession numbers in directory: \n\n\t"{SamplesAccessionNumbersDir}"'
		srf.write(attribute)

	else:
		pass
	
	srf.close()
		
# Dictionary keys specific database's NCBI-Biosample accession numbers fetching routine
		
def Fetch_accession_numbers_searching_dict_keys(Collection, database, accession_number_field, keep_entry_key, keep_entry_val, isolates_metadata_keys, metadata_file, metadata_csv_file, metadata_csv_file_headers, statistics_file, statistics_csv_file, sampling_report_file, dict_key_options_tuple, dict_key_options_menu, options, DefaultDirectoryRoot, CustomDirectoryRoot):
	
	Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot)
	
	srf = open(sampling_report_file, 'w', encoding='utf-8')
	
	print(f'\n\nYou are using {database}.\n\n\n')
		
	dictionary_key = ''
	keyword = ''
	keywords = {}
	keywords_set = {}
	isolate = {}
	lower_case_isolate = {}
	accession_number = ""
	accession_numbers_list = []
	accession_numbers_counts = 0
	
	keywords_set_count = 0
	while dictionary_key != '--':
		
		dictionary_key = ''
		keywords = {}
		keyword = ''
		keywords_set_count = keywords_set_count + 1
		keyword_count = 0
		
		Clear_screen(OperatingSystem)
		
		print(f'These are {database} field options:\n\n{dict_key_options_menu}\n\n')
		print('Enter one pair of field / keyword at a time then just enter:\n\n\t"-" to conclude current set of keywords\n\n\t"--" to conclude all keyword sets\n\n\n\n')
		print(f'Keywords set {keywords_set_count}')
		
		while True:
			keyword_count = keyword_count + 1
			dictionary_key = ''
			while not dictionary_key in options[0:] and not dictionary_key in ('-','--'):
				dictionary_key = str(input(f'Please, enter field {keyword_count}:'))
			if dictionary_key == '-' and keyword_count == 1:
				keywords_set_count = keywords_set_count -1
			if dictionary_key == '-' or dictionary_key == '--':
				break
			keyword = input(f'Please, enter field {keyword_count}\'s keyword:')
			keyword = keyword.lower()
			entry = {dict_key_options_tuple[int(dictionary_key) - 1]:keyword}
			keywords.update(entry)
			item = {keywords_set_count : keywords}
			keywords_set.update(item)
			
	if keywords_set != {}:
		
		Clear_screen(OperatingSystem)
		
		Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot)
		
		print(f'\n\nYou are using {database}.\n')
		print('\n\nThese are the fields / keywords pairs you entered:')
		
		attribute = f'You are using {database}.\n\n\n'
		srf.write(attribute)
		attribute = 'These are the fields / keywords pairs you entered:\n\n'
		srf.write(attribute)
		
		keywords_set_count = 0
		
		for keywords in keywords_set:
			kv_pairs = {}
			keywords_set_count = keywords_set_count + 1
			print(f'\nKeywords set {keywords_set_count}\n')
			attribute = f'Keywords set {keywords_set_count}\n'
			srf.write(attribute)
			kv_pairs.update(keywords_set[keywords_set_count])
			
			field = 0
			
			for i in kv_pairs:
				field = field + 1
				print(f'Field {field}: {i}\nKeyword: {kv_pairs[i]}\n')				
				attribute = f'Field {field}: {i}\nKeyword: {kv_pairs[i]}\n'
				srf.write(attribute)
				
		n = len(Collection)
		
		print (f"\n\nThe Collection has {n} isolates\n")
		print ('\nSearching...\n')
		
		positive_isolate_count = 0
		positive_isolate_count_stratified = []
		
		for i in range(len(keywords_set)):
			positive_isolate_count_stratified.append(0)
			
		im = open(metadata_file, 'w', encoding='utf-8')
		im.write('[\n')
		
		imcsv = open(metadata_csv_file, 'w', encoding='utf-8')
		imcsv.write(metadata_csv_file_headers)
		
		isolate_count = -1
		for isolate in Collection:
			
			isolate_count = isolate_count + 1
				
			item_count = 0
			for item in keywords_set:
				item_count = item_count + 1
				kv_pairs = keywords_set[item]
				
				kv_count = 0
				for k in kv_pairs:
					kv_count = kv_count + 1
					lci_k = str(k)
					
					if not kv_pairs[k] in isolate[lci_k]:
						break
					elif kv_count == len(kv_pairs):
						positive_isolate_count = positive_isolate_count + 1
						a = positive_isolate_count_stratified[item_count - 1]
						a = a + 1
						positive_isolate_count_stratified[item_count - 1] = a
						accession_number = isolate[accession_number_field]
						if accession_number != '' and not accession_number in accession_numbers_list:
							accession_numbers_list.append(accession_number)
							Metadata_retrieval_routine(Collection, isolate_count, accession_number_field, keep_entry_key, keep_entry_val, accession_number, isolates_metadata_keys, im, imcsv)
						else:
							pass
						break
		im.write(']')
		im.close()
		
		imcsv.close()
		
		statfile = shutil.copy2(metadata_file, statistics_file)
		statcsvfile = shutil.copy2(metadata_csv_file, statistics_csv_file)
		
		Clear_screen(OperatingSystem)
		
		Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot)
		
		print(f'\n\nYou are using {database}.')
		print (f"\n\n\nThe Collection has {n} isolates.")
		print(f"\nThere are {positive_isolate_count} isolates that satisfy the entered sets of keywords.")
		print('\nBelow is the stratification per Keyword set:')
		
		attribute = f"\n\nThe Collection has {n} isolates\n\n"
		srf.write(attribute)
		attribute = f"There are {positive_isolate_count} isolates that satisfy the entered sets of keywords.\n\n"
		srf.write(attribute)
		attribute = 'Below is the stratification per Keyword set:\n\n'
		srf.write(attribute)
		
		keywords_set_count = 0
		for keywords in keywords_set:
			kv_pairs = {}
			keywords_set_count = keywords_set_count + 1
			print(f'\nKeywords set {keywords_set_count}\n')
			attribute = f'Keywords set {keywords_set_count}\n'
			srf.write(attribute)
			kv_pairs.update(keywords_set[keywords_set_count])
			
			field = 0
			
			for i in kv_pairs:
				field = field + 1
				print(f'Field {field}: {i}\nKeyword: {kv_pairs[i]}\n')
				attribute = f'Field {field}: {i}\nKeyword: {kv_pairs[i]}\n'
				srf.write(attribute)
				
			print('Total hits = ', positive_isolate_count_stratified[keywords - 1])
			attribute = f'Total hits = {positive_isolate_count_stratified[keywords - 1]}\n\n'
			srf.write(attribute)
		
		f = open(str(SamplesAccessionNumbersDir) + str(database) + '_accession numbers.txt', "w", encoding='utf-8')
		contents = f.write(str(accession_numbers_list))
		f.close()
		
		accession_numbers_list = Consolidate_list(accession_numbers_list)
		
		accession_numbers_counts = len(accession_numbers_list)
		
		print(f'\nThe NCBI sequence accession numbers of {accession_numbers_counts} unique isolates could be retrieved.')
		print('\nThis is your list of accession numbers:\n\n',accession_numbers_list)
		print(f'\n\nYou can find your list of accession numbers in directory: \n\n\t"{SamplesAccessionNumbersDir}"')
		
		attribute = f'The NCBI sequence accession numbers of {accession_numbers_counts} unique isolates could be retrieved.\n\n'
		srf.write(attribute)
		attribute = f'This is your list of accession numbers:\n\n {accession_numbers_list}\n\n'
		srf.write(attribute)
		attribute = f'You can find your list of accession numbers in directory: \n\n\t"{SamplesAccessionNumbersDir}"'
		srf.write(attribute)
	
	else:
		pass
		
	srf.close()	
		
# Accession numbers lists sort and consolidation routine
		
def Consolidate_list(my_list):
	
	my_list.sort()
	
	if my_list != []:
		
		flag = True
		while flag == True:
			for item in range(len(my_list)):
				if item == len(my_list) - 1:
					flag = False
					break
				elif item < len(my_list) - 1 and my_list[item] == my_list[item + 1]:
					my_list.pop(item)
					flag = True
					break
				else:
					pass
					
	else:
		pass
		
	return my_list

# Isolates metadata fetching and archiving routine
		
def Metadata_retrieval_routine(Collection, isolate_count, accession_number_field, keep_entry_key, keep_entry_val, accession_number, isolates_metadata_keys, im, imcsv):
		
	dictionary = Collection[isolate_count]
	isolate_dictionary = {}
	
	biosample_accession = dictionary[accession_number_field]
	biosample_accession = biosample_accession.strip()
	
	if biosample_accession == accession_number:
		
		for key in isolates_metadata_keys:
			k = key
			v = dictionary[key]
			isolate_dictionary.update({k:v})
		
		isolate_dictionary.update({keep_entry_key:keep_entry_val})
		
		im.write(str(isolate_dictionary))
		im.write(',\n')
		
		attribute = ''
		counter = 0
		for key in isolate_dictionary:
			counter = counter + 1
			attribute = isolate_dictionary[key]
			imcsv.write(attribute)
			if counter < len(isolate_dictionary):
				imcsv.write(',')
			else:
				imcsv.write('\n')
				
# Accession numbers list editing routine

def Edit_accession_numbers_list(accession_number_field, metadata_csv_file, accession_numbers_file, accession_numbers_BU_file, removed_accession_numbers_file, DefaultDirectoryRoot, CustomDirectoryRoot):
	
	Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot)
	
	result = File_checking(accession_numbers_BU_file)
	
	if result == False:
		
		shutil.copy2(accession_numbers_file, accession_numbers_BU_file)
		
	else:
		
		pass
		
	anf = open(accession_numbers_file, 'w', encoding='utf-8')
	anf.write('[')
	ranf = open(removed_accession_numbers_file, 'w', encoding='utf-8')
	ranf.write('[')
	
	metadata_dictionaries_list = Csv_to_list_dicts(metadata_csv_file)
	
	for dictionary in metadata_dictionaries_list:
		
		if dictionary['keep entry?'] == 'y':
			
			accession_number = dictionary[accession_number_field]
			attribute = '\'' + str(accession_number) + '\','
			anf.write(attribute)
			
		else:
			
			accession_number = dictionary[accession_number_field]
			attribute = '\'' + str(accession_number) + '\','
			ranf.write(attribute)
			
	anf.write(']')
	ranf.write(']')
	
	anf.close()
	ranf.close()
	
# NCBI chromosome, plasmid sequences and assemblies download (Entrez esearch / efetch + Assemblies FTP) routines
		
def NCBI_sequence_download(input_file,output_file_route, report_file, fasta_headers_file, DefaultDirectoryRoot, CustomDirectoryRoot):

	import urllib.request, time
	from Bio import Entrez
	
	Entrez.email = "nab.schriefer@gmail.com"
	
	#Entrez.api_key = "MyAPIkey"
	
	accession_numbers_list = []
	accession_dictionary = {}
	inverted_chromosome_accession_dictionary = {}
	inverted_plasmid_accession_dictionary = {}
	chromosome_id_list = []
	chromosome_id_list_fasta = []
	plasmid_id_list = []
	plasmid_id_list_fasta = []
	
	Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot)
	
	Consolidate_accession_numbers_list_files(SamplesAccessionNumbersDir)
	
	ipt = open(input_file, 'r', encoding='utf-8')
	contents = ipt.read()
	ipt.close()
	accession_numbers_list = ast.literal_eval(contents)
	
	fh = open(fasta_headers_file, 'w', encoding='utf-8')
	fh.write('This is the list of fasta headers of the downloaded sequences\n\n')
	
	print('This is the list of accession numbers being downloaded: \n\n', accession_numbers_list, '\n')
		
	rf = open(report_file, 'w', encoding='utf-8')
	rf.write('This is the list of accession numbers being downloaded: \n\n')
	counter = 0
	for accession_number in accession_numbers_list:
		counter = counter + 1
		rf.write(accession_number)
		rf.write('\t')
		if counter == 4:
			rf.write('\n')
			counter = 0
	
	for accession_number in accession_numbers_list:
		
		if accession_number != '':
			
			print('\n----------//----------//----------//----------//----------\n')
			print('Accession number: ', accession_number, '\n')
			
			rf.write('\n----------//----------//----------//----------//----------//----------\n')
			argument = '\nAccession number: ' + accession_number + '\n'
			rf.write(argument)

			handle = Entrez.esearch(db="nucleotide", term=accession_number)
			search_record = Entrez.read(handle)
			handle.close()
			
			id_list = search_record['IdList']
			
			if id_list != []:
				
				for indx in range(len(id_list)):
					id_list[indx] = int(id_list[indx])
				
				id_list.sort()
				
				handle = Entrez.esummary(db="nucleotide", id=id_list[0], rettype="fasta")
				record = Entrez.read(handle, validate=False)#####
				fasta_header = record[0]["Title"]
				fasta_header = fasta_header.lower()
				handle.close()
				
				if 'shotgun' in fasta_header:
					NCBI_assembly_download(accession_number, fasta_header, fh, rf)
				
				else:
					NCBI_chromosome_plasmid_download(accession_number, id_list, fasta_header, fh, rf)
				
	fh.close()
	rf.close()

def NCBI_chromosome_plasmid_download(accession_number, id_list, fasta_header, fh, rf):
	
	import urllib.request, time
	from Bio import Entrez
	
	Entrez.email = "nab.schriefer@gmail.com"
	
	#Entrez.api_key = "MyAPIkey"
	
	accession_dictionary = {}
	inverted_chromosome_accession_dictionary = {}
	inverted_plasmid_accession_dictionary = {}
	chromosome_id_list = []
	chromosome_id_list_entry = 0
	chromosome_id_list_fasta = []
	plasmid_id_list = []
	plasmid_id_list_fasta = []
	
	print('Identified sequences with this accession number: \n')
	rf.write('\nIdentified sequences with this accession number: \n')
	
	for item in range(len(id_list)):
		count = item + 1
		print(f'Sequence identifier {count} = ', id_list[item])
		argument = f'\nSequence identifier {count} = ' + str(id_list[item])
		rf.write(argument)
		
	for sequence_id in id_list:
		handle = Entrez.esummary(db="nucleotide", id=sequence_id, rettype="fasta")
		record = Entrez.read(handle, validate=False)#####
		fasta_header = record[0]["Title"]
		fasta_header = fasta_header.lower()
		handle.close()
	
		if ',' in fasta_header:
			fasta_header = fasta_header[0:fasta_header.rindex(',')]
			
		sequence_length = str(record[0]['Length'])
		sequence_size = sequence_length.lstrip('IntegerElement(')
		sequence_size = sequence_size.rstrip(', attributes={})')
		sequence_size = int(sequence_size)
		
		if not 'chromosome' in str(fasta_header) and not 'plasmid' in str(fasta_header):
			if sequence_size >= 2500000:
				fasta_header = fasta_header + ' [ chromosome likely, added by SampleMiner ]'
			else:
				fasta_header = fasta_header + ' [ plasmid likely, added by SampleMiner ]'
				
		accession_dictionary[sequence_id] = fasta_header
		
		for key in accession_dictionary:
			
			if 'chromosome' in str(accession_dictionary[key]).lower():
				k = str(key)
				v = str(accession_dictionary[key])
				inverted_chromosome_accession_dictionary.update({v:k})
				
			if 'plasmid' in str(accession_dictionary[key]).lower():
				k = str(key)
				v = str(accession_dictionary[key])
				inverted_plasmid_accession_dictionary.update({v:k})
				
			else:
				pass
		
	for key in inverted_chromosome_accession_dictionary:
		chromosome_id_list.append(inverted_chromosome_accession_dictionary[key])
		chromosome_id_list_fasta.append(key)
		
	if len(chromosome_id_list) > 1:
		chromosome_id_list.sort(reverse = True)
		chromosome_id_list_entry = chromosome_id_list[0]
		chromosome_id_list = []
		chromosome_id_list.append(chromosome_id_list_entry)
		entry = int(chromosome_id_list_entry)
		chromosome_id_list_fasta.append(accession_dictionary[entry])
		
	else:
		pass
		
	if chromosome_id_list != []:
		chromosome_download = chromosome_id_list[0]
		print('\nChromosome sequence identifier: ', chromosome_download, '\n')
		argument = '\n\nChromosome sequence identifier: ' + chromosome_download + '\n'
		rf.write(argument)
		print('Downloading complete chromosome sequence ', chromosome_download, '...')
		argument = '\nDownloading complete chromosome sequence ' + chromosome_download + '...\n'
		rf.write(argument)
		
		fetch_handle = None
		for download_attempt in range(5):
			try:
				fetch_handle = Entrez.efetch(db="nucleotide", id=chromosome_download, rettype="fasta")
			except:
				time.sleep(1)
					
		if fetch_handle:
			time.sleep(1)
			fetch_record = fetch_handle.read()
			fetch_handle.close()
			
			if 'added by SampleMiner' in chromosome_id_list_fasta[0]:
				inference_string = '_inferred_by_SampleMiner'
			else:
				inference_string = ''
				
			chromosome_seq_file = DownloadedSequencesDir + accession_number + '_chromosome_sequence' + inference_string + '.fa'
			f = open(chromosome_seq_file, 'w', encoding='utf-8')
			f.write(fetch_record)
			f.close()
			
			fasta_header_attribute = chromosome_id_list_fasta[0]
			attribute = '\n' + accession_number + ' \ ' + chromosome_download + ': ' + fasta_header_attribute + '\n'
			fh.write(attribute)
			
		else:
			print(f'Could not download {chromosome_download}!')
			
	else:
		print('\nNo chromosome sequences found for this accession number.')
		rf.write('\n\nNo chromosome sequences found for this accession number.\n')
				
	for key in inverted_plasmid_accession_dictionary:
		plasmid_id_list.append(inverted_plasmid_accession_dictionary[key])
		plasmid_id_list_fasta.append(key)
		
	if plasmid_id_list != []:
		print('\nPlasmid(s) sequence identifier(s): \n')
		rf.write('\nPlasmid(s) sequence identifier(s): \n\n')
		
		for item in range(len(plasmid_id_list)):
			count = item + 1
			print(f'Sequence identifier {count} = ', plasmid_id_list[item])
			argument = f'Sequence identifier {count} = ' + plasmid_id_list[item]
			rf.write(argument)
			rf.write('\n')
			
		print()
		rf.write('\n')
		
		for item in range(len(plasmid_id_list)):
			print('Sequence identifier being downloaded = ', plasmid_id_list[item], ' ...')
			argument = 'Sequence identifier being downloaded = ' + plasmid_id_list[item] + ' ...\n'
			rf.write(argument)
			plasmid_download = plasmid_id_list[item]
			
			fetch_handle = None
			for download_attempt in range(5):
				try:
					fetch_handle = Entrez.efetch(db="nucleotide", rettype="fasta", id=plasmid_download)
				except:
						time.sleep(1)
			
			if fetch_handle:
				time.sleep(1)
			else:
				print(f'Could not download {plasmid_download}!')
				
			fetch_record = fetch_handle.read()
			fetch_handle.close()
			
			if 'added by SampleMiner' in plasmid_id_list_fasta[item]:
				inference_string = '_inferred_by_SampleMiner'
			else:
				inference_string = ''
				
			plasmid_seq_file = DownloadedSequencesDir + accession_number + '_plasmid_sequence_(' + plasmid_id_list[item] + ')' + inference_string + '.fa'
			f = open(plasmid_seq_file, 'w', encoding='utf-8')
			f.write(fetch_record)
			f.close()
			
			fasta_header_attribute = str(plasmid_id_list_fasta[item])
			attribute = '\n' + accession_number + ' \ ' + plasmid_download + ': ' + fasta_header_attribute + '\n'
			fh.write(attribute)
				
	else:
		print('\nNo plasmid sequences found for this accession number.')
		rf.write('\n\nNo plasmid sequences found for this accession number.\n')

def NCBI_assembly_download(accession_number, fasta_header, fh, rf):
	
	import urllib.request, time
	from Bio import Entrez
	
	Entrez.email = "nab.schriefer@gmail.com"
	
	#Entrez.api_key = "MyAPIkey"
	
	print(f'{accession_number} is a whole genome shotgun assembly.\n')
	argument = f'\n\n{accession_number} is a whole genome shotgun assembly.\n'
	rf.write(argument)
	
	print('Downloading WGS assembly compressed fasta file ...')
	argument = '\nDownloading WGS assembly compressed fasta file ...\n'
	rf.write(argument)
	
	attribute = '\n' + accession_number + ' \ ' + 'WGS assembly' + ': ' + fasta_header + '\n'
	fh.write(attribute)
	
	path = 'assemblies'
	
	handle = Entrez.esearch(db="assembly", term=accession_number)
	search_record = Entrez.read(handle, validate=False)
	handle.close()
	
	id_list = search_record['IdList']
	accession_number_id = id_list[0]
	
	esummary_handle = Entrez.esummary(db="assembly", id=accession_number_id, report="full")
	esummary_record = Entrez.read(esummary_handle, validate=False)
	esummary_handle.close()
	
	url = esummary_record['DocumentSummarySet']['DocumentSummary'][0]['FtpPath_GenBank']
	
	if url == '':
	
		print(f'Could not get the {accession_number} assembly!','\n\n')
		option = 1
		Press_a_key(OperatingSystem, option)
		Clear_screen(OperatingSystem)
		
	else:
		
		label = os.path.basename(url)
		link = os.path.join(url,label+'_genomic.fna.gz')
		assembly_file = DownloadedSequencesDir + accession_number + '_WGS_assembly' + '.fna.gz'
		urllib.request.urlretrieve(link, assembly_file)
	
# Accession numbers list files consolidation routine

def Consolidate_accession_numbers_list_files(SamplesAccessionNumbersDir):
	
	accession_numbers_file = SamplesAccessionNumbersDir + 'accession numbers.txt'
	databases_accession_numbers_files = []
	accession_numbers_list = []
	consolidated_accession_numbers_list = []
	new_file = ''
	
	databases_accession_numbers_files = [f for f in os.listdir(SamplesAccessionNumbersDir) if os.path.isfile(os.path.join(SamplesAccessionNumbersDir, f))]
	
	for accnumbfile in databases_accession_numbers_files:
		
		if accnumbfile != 'accession numbers.txt' and not '_BU' in accnumbfile and not '_RM' in accnumbfile:
			
			accnumbfile_path = SamplesAccessionNumbersDir + accnumbfile
			current_accession_numbers = open(accnumbfile_path, 'r', encoding='utf-8')
			can_list = current_accession_numbers.read()
			current_accession_numbers.close()
			
			accession_numbers_list = ast.literal_eval(can_list)
			consolidated_accession_numbers_list = consolidated_accession_numbers_list + accession_numbers_list
			
		else:
			
			pass
			
	consolidated_accession_numbers_list = Consolidate_list(consolidated_accession_numbers_list)
	consolidated_accession_numbers_list.sort()
	
	an = open(accession_numbers_file, 'w', encoding='utf-8')
	consolidated_accession_numbers_list_string = str(consolidated_accession_numbers_list)
	an.write(consolidated_accession_numbers_list_string)
	an.close()

# Sample summarizing routine
	
def Summarize(graphics_option, isolates_metadata_keys, statistics_csv_file, database, sample_summary_file, DefaultDirectoryRoot, CustomDirectoryRoot):
	
	import pandas
	import matplotlib.pyplot as plt
	
	Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot)
	
	print(f'\n\nYou are using {database}.\n\n\n')
	
	metadata_dataframe = pandas.read_csv(statistics_csv_file)
	
	if graphics_option == 'n':
		
		ssf = open(sample_summary_file, 'w', encoding='utf-8')
		
		print('Sample descriptive summary:\n\n')
		ssf.write('Sample descriptive summary:\n\n')
	
		counter = -1
		for item in isolates_metadata_keys:
			counter = counter + 1
			counts = metadata_dataframe[item].value_counts()
			print(f'{item}:\n{counts}\n\n')
			atribute = str(f'{item}:\n{counts}\n\n')
			ssf.write(atribute)
			
		counts = metadata_dataframe.groupby([isolates_metadata_keys[0], isolates_metadata_keys[1], isolates_metadata_keys[2], isolates_metadata_keys[3]]).size()
		atribute = str(counts)
		
		print('Summary table:\n\n,', counts)
		ssf.write(atribute)
		ssf.close()
	
	else:
		
		counter = -1
		for item in isolates_metadata_keys:
			
			counter = counter + 1
			
			df = metadata_dataframe[item].value_counts().rename_axis('Unique values').to_frame('counts')
			
			df.plot(kind='bar', title=isolates_metadata_keys[counter], xlabel='', ylabel=None, logy=True,fontsize=8, figsize=(15,5))
			fig = plt.gcf()
			fig.subplots_adjust(bottom=0.3)
			plt.show()
	
################################
##                            ##
##  HOUSEKEEPING SUBROUTINES  ##
##                            ##
################################

# Terminal screen sizing routine
			
def Terminal_set_up():

	if OperatingSystem == 'posix':
		sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=55, cols=90))
		
	elif OperatingSystem == 'nt':
		rows = 35
		cols = 95
		try:
			h_out = ctypes.windll.kernel32.GetStdHandle(-11)  # -11 is the standard output device
			if h_out is not None:
				coord = ctypes.wintypes._COORD(cols, rows)
				ctypes.windll.kernel32.SetConsoleScreenBufferSize(h_out, coord)
				rect = ctypes.wintypes.SMALL_RECT(0, 0, cols - 1, rows - 1)
				ctypes.windll.kernel32.SetConsoleWindowInfo(h_out, True, ctypes.byref(rect))
			else:
				print("Failed to get handle to console.")
		except Exception as e:
			print("Error resizing terminal:", e)
			
	else:
		pass
	
# Print working directory routine

def Print_working_directory(DefaultDirectoryRoot, CustomDirectoryRoot):
	
	if CustomDirectoryRoot != '':
		print(f'>> Working directory: {CustomDirectoryRoot} \n')
	else:
		print(f'>> Working directory: { DefaultDirectoryRoot} \n')


# Directories checking and creation routine
		
def Check_directory(directory):
	
	if not os.path.exists(directory):
		os.mkdir(directory)
		
	else:
		pass
		
# File checking routine

def File_checking(filename):
	
	if os.path.exists(filename) is True:
		File_checking_result = True
	else:
		File_checking_result = False
		
	return File_checking_result

# Clear terminal screen routine
		
def Clear_screen(OperatingSystem):
	
	if OperatingSystem == 'posix':
		os.system("clear")
		
	elif OperatingSystem == 'nt':
		os.system("cls")
		
	else:
		pass
		
# Press any key to continue routine
		
def Press_a_key(OperatingSystem, option):
	
	if OperatingSystem == 'posix' and option == 1:
		os.system('read -sn 1 -p "\n\n\n> Press any key to go back <"')
		
	elif OperatingSystem == 'posix' and option == 2:
		os.system('read -sn 1 -p "\n\n\n> Press any key to continue <"')
		
	elif OperatingSystem == 'nt' and option == 1:
		print("\n\n\n")
		os.system("pause")
		
	elif OperatingSystem == 'nt' and option == 2:
		print("\n\n\n")
		os.system("pause")
		
	else:
		pass
		
# Program termination
		
def Bye():
	
	print ("\n\n\n\n>> See you!!! <<\n\n\n\n\n")

	
if __name__ == '__main__':
	Start()

'''

INSTRUCTIONS

(A) Installing the program:

1- Create an Anaconda environment named SampleMiner, containing Python 3.8 or later, Biopython, Pandas and Matplotlib.

2- Optional step: Open a terminal window, go to Terminal>Preferences>Shell and in the pull down menu 'When exiting shell' choose
   'close shell if clean exit'. This allows the terminal window to close automatically once you quit SampleMiner.

3- Make a 'SampleMiner' folder within your local 'applications' directory.

4- Save the SampleMiner.py file to your local 'applications' directory within the 'SampleMiner' folder.

5- Add to the same folder the bash file below named 'SampleMiner.command'. This bash file opens the terminal screen,
   activates the SampleMiner Anaconda environment and runs SampleMiner.py within it.

	#!/bin/bash
	source /Users/.../opt/anaconda3/bin/activate sampleminer
	/Users/.../Applications/SampleMiner/SampleMiner.py

6- Create a shortcut of the 'SampleMiner.command' bash file and place it on your desktop.

7- To run SampleMiner.py just double click the shortcut to the 'SampleMiner.command' bash file.

8- Run SampleMiner.py once and then choose '50' to quit it. This will instal the runtime directories of SampleMiner
   in the local 'Documents' directory.

9- Place the Enterobase and Patrick tsv files into the 'Documents/SampleMiner/databases tsv files' directory.

10- If you already have the up-to-date Enterobase and Patrick 'Complete genome_Metadata_list' dictionaries files imported
   from the tsv files above, just place them in the directory 'Documents/SampleMiner/databases dictionaries'.

11- If you don't have the up-to-date dictionaries, then run SampleMiner and choose option 1 so you can import the tsv files
   into dictionaries that will be automatically added to the 'Documents/SampleMiner/databases dictionaries' directory.

12- Now, the program is fully installed and ready to use.

(B) Using the program:

1- Menu option '0' serves to set up or use an existing non-default directory of samples and data. If the directory is not set,
   the default directories established during installation will be used. It is better to set a working directory than using the
   defaults.

2- Options '1' and '9' import the tsv files stored in directory 'Documents/SampleMiner/databases tsv files' into python dictionaries
   that are stored automatically in directory 'Documents/SampleMiner/databases dictionaries'. These dictionaries contain all
   metadata of the isolates that are used in the keywords search of options '2', '3', '4', '5', '10', '11', '12', '13'.

3- Options '2' to '5' serve to keyword search Patric dictionaries, while '10' to '13' do the same for Enterobase.
   '2', '3', '10' and '11' are usefull to quickly evaluate the appropriateness of the keywords chosen. '4', '5', 12 and '13' fetch
   the NCBI Biosample accession numbers and isolates metadata from Patric and Enterobase. The accession numbers will be stored in
   directory 'Documents/SampleMiner/mined samples/default[or a custom folder]/samples accession numbers', while the metadata will be
   stored as csv files in directory 'Documents/SampleMiner/mined samples/default[or a custom folder]/samples metadata'. These options
   also create Python txt files with dictionaries containing the same metadata and stored in the same directory, which may be explored
   programatically. Besides creating the '[Patric or Enterobase] isolates metadata.csv' and '[Patric or Enterobase] isolates metadata.
   txt' files, the program will also create the '[Patric or Enterobase] isolates metadata for statistics.csv' and '[Patric or Enterobase]
   isolates metadata for statistics.txt' files. These are just copies of the two files above that will not be used by SampleMiner, but 
   may explored by the user for various personal analises. Finally, these accession number fetching options also create a log of the
   searching process and store it as 'Documents/SampleMiner/mined samples/default[or a custom folder]/reports/[Patric or Enterobase]
   sampling report.txt'.

4- Options '6' and '14' can be used for determining which accession numbers should be effectivelly set to fetch chromosome, plasmid and
   assembly sequences from NCBI. Before using these options, edit the the entries in the 'Keep record?' column within the '[Patric or 
   Enterobase] isolates metadata.csv' files. Keep the 'y' option for those isolates that you want to fetch sequences from NCBI. Change it
   to 'n' for those isolates you don't want to download the sequences. These options will first back up the original accession numbers into
   the file 'Documents/SampleMiner/mined samples/default[or a custom folder]/samples metadata/[Patric or Enterobase]_accession
   numbers_BU.txt', keeping all the original accession numbers safe. Then they will create a file of removed accession numbers named
   '[Patric or Enterobase]_accession numbers_RM.txt', which is saved to the same directory above, and an up-to-date '[Patric or Enterobase]_accession numbers.txt' file containing only those isolates chosen. This file will be stored in the 'samples accession numbers' folder.

5- Options '7', '8', '15' and '16' summarize important metadata of samples in table ('7' and '15') or graph formats ('8' and '16'). Tables
   will be automatically saved as 'Documents/SampleMiner/mined samples/default[or a custom folder]/samples metadata/[Patric or Enterobase]
   isolates metadata summary.txt. Graphs may be saved by the user as they are displayed on screen. The graphs will be displayed in sucession
   with a new graphic poping up as a previous is closed by the user. To close the last graph it will be necessary to click in the close red
   buton at the left top of the window, then highlight the SampleMinder.py running terminal window and press any key.

6- Option '40' fetches the chromosome, plasmid and assembly sequences contained in file '[Patric or Enterobase]_accession numbers.txt'
   from NCBI. It stores the downloaded sequence files in directory 'Documents/SampleMiner/mined samples/default[or a custom folder]/
   downloaded sequences', plus all fasta headers and a log file in directory 'Documents/SampleMiner/mined samples/default[or a custom folder]
   /reports'.

VERSION NOTE(S)

This version of SampleMiner.py is SampleMiner V1.0.

DATABASE TEMPLATE

- Edits for the Main Menu and 'Start()' action options per added DATABASE:

(Substituting: Patric/Enterobase with DATABASE; E. coli with PATHOGEN; variables with VAR1, VAR2 ... VARn; Accession number attribute with DATABASE NCBI ACCESSION NUMBER FIELD):

		# Main Menu:

		print ("\n\nMAIN MENU\n\n(0) Set working directory\n\n(1) Import Patric tsv file\n(2) Browse Patric with keywords\n(3) Browse Patric with field specific keywords\n(4) Fetch Patric isolates’ metadata with keywords\n(5) Fetch Patric isolates’ metadata with field specific keywords\n(6) Exclude / Reinclude Patric isolates’ from sample\n(7) Describe Patrick sample with tables\n(8) Describe Patrick sample with graphics\n\n(9) Import Enterobase tsv file\n(10) Browse Enterobase with keywords\n(11) Browse Enterobase with field specific keywords\n(12) Fetch Enterobase isolates’ metadata with keywords\n(13) Fetch Enterobase isolates’ metadata with field specific keywords\n(14) Exclude / Reinclude Enterobase isolates’ from sample\n(15) Describe Enterobase sample with tables\n(16) Describe Enterobase sample with graphics\n\n(17) Import DATABASE tsv file\n(18) Browse DATABASE with keywords\n(19) Browse DATABASE with field specific keywords\n(20) Fetch DATABASE isolates’ metadata with keywords\n(21) Fetch DATABASE isolates’ metadata with field specific keywords\n(22) Exclude / Reinclude DATABASE isolates’ from sample\n(23) Describe DATABASE sample with tables\n(24) Describe DATABASE sample with graphics\n\n(40) Fetch sample isolates’ DNA sequences from NCBI\n\n(50) Quit\n")

		# Actions:

		# (17) Import DATABASE tsv file
		
		elif choice == "1":
			
			Clear_screen(OperatingSystem)
			
			print('You are using DATABASE.\n')
			
			input_file = DatabasesTsvFilesDir + "DATABASE_PATHOGEN_Complete genome_Metadata.tsv"
			
			File_checking_result = File_checking(input_file)
			
			if File_checking_result == True:
			
				result = Tsv_to_list_dicts(input_file)
				
				output_file = DatabasesDictionariesDir + "DATABASE_PATHOGEN_Complete genome_Metadata_list.txt"
				
				f = open(output_file, "w", encoding='utf-8')
				f.write(str(result))
				f.close()
			
			else:
				
				print(f'\n\n\n\nFile not found:\n\n{input_file}\n\n\n')
				option = 1
				Press_a_key(OperatingSystem, option)
			
			choice = ""
			Clear_screen(OperatingSystem)
		
		# (18) Browse DATABASE with keywords
		
		elif choice == "2":
			
			Clear_screen(OperatingSystem)
			
			print('You are using DATABASE.\n\n\n\n\n')
			
			print('Uploading DATABASE database to memory...\n\n')
			
			input_file = DatabasesDictionariesDir + "DATABASE_PATHOGEN_Complete genome_Metadata_list.txt"
			
			File_checking_result = File_checking(input_file)
			
			if File_checking_result == True:
			
				if DATABASECollection == []:
					f = open(input_file, "r", encoding='utf-8')
					contents = f.read()
					f.close()
					DATABASECollection = ast.literal_eval(contents)
				else:
					pass
				
				Collection = DATABASECollection
				
				Clear_screen(OperatingSystem)
				
				database = "DATABASE"
				
				Data_mining(database, Collection, DefaultDirectoryRoot, CustomDirectoryRoot)
			
			else:
				
				print(f'\n\n\n\nFile not found:\n\n{input_file}\n\n\n')
			
			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
			
		# (19) Browse DATABASE with field specific keywords
		
		elif choice == "3":
			
			Clear_screen(OperatingSystem)
			
			print('You are using DATABASE.\n\n\n\n\n')
			
			print('Uploading DATABASE database to memory...\n\n')
			
			input_file = DatabasesDictionariesDir + "DATABASE_PATHOGEN_Complete genome_Metadata_list.txt"
			
			File_checking_result = File_checking(input_file)
			
			if File_checking_result == True:
				
				if DATABASECollection == []:
					f = open(input_file, "r", encoding='utf-8')
					contents = f.read()
					f.close()
					DATABASECollection = ast.literal_eval(contents)
				else:
					pass
				
				Collection = DATABASECollection
				
				Clear_screen(OperatingSystem)
				
				database = "DATABASE"
				
				dict_key_options_tuple = ('VAR1', 'VAR2', 'VAR3', 'VAR4', 'VAR5', ...)
				dict_key_options_menu = ('(1) VAR1\n(2) VAR2\n(3) VAR3\n(4) VAR4\n(5) VAR5\n ...')
				options = ('1','2','3','4','5',...)
				
				Data_mining_searching_dict_keys(database, Collection, dict_key_options_tuple, dict_key_options_menu, options, DefaultDirectoryRoot, CustomDirectoryRoot)
			
			else:
				
				print(f'\n\n\n\nFile not found:\n\n{input_file}\n\n\n')
			
			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
			
		# (20) Fetch DATABASE isolates’ metadata with keywords
		
		elif choice == "4":
			
			Clear_screen(OperatingSystem)
			
			print('You are using DATABASE.\n\n\n\n\n')
			
			print('Uploading DATABASE database to memory...\n\n')
			
			input_file = DatabasesDictionariesDir + "DATABASE_PATHOGEN_Complete genome_Metadata_list.txt"
			
			File_checking_result = File_checking(input_file)
			
			if File_checking_result == True:
				
				if DATABASECollection == []:
					f = open(input_file, "r", encoding='utf-8')
					contents = f.read()
					f.close()
					DATABASECollection = ast.literal_eval(contents)
				else:
					pass
				
				Collection = DATABASECollection
				
				database = 'DATABASE'
				accession_number_field = 'DATABASE NCBI ACCESSION NUMBER FIELD'
				
				keep_entry_key = 'keep entry'
				keep_entry_val = 'y'
		
				VAR1 = 'VAR1'
				VAR2 = 'VAR2'
				VAR3 = 'VAR3'
				VAR4 = 'VAR4'
				VAR5 = 'VAR5'
				...
				
				isolates_metadata_keys = (VAR1_key, VAR2_name_key, VAR3_country_key, VAR4_key, VAR5_source_key, ...)
				
				metadata_file = SamplesMetadataDir + 'DATABASE isolates metadata.txt'
				metadata_csv_file = SamplesMetadataDir + 'DATABASE isolates metadata.csv'
				
				metadata_csv_file_headers = ('Keep entry?' + ',' + 'DATABASE NCBI ACCESSION NUMBER FIELD' + ',' + 'VAR1' + ',' + 'VAR2' + ',' + 'VAR3' + ',' + 'VAR4' + ',' + 'VAR5' + ',' + ... + '\n')
				
				statistics_file = SamplesMetadataDir + 'DATABASE isolates metadata statistics.txt'
				statistics_csv_file = SamplesMetadataDir + 'DATABASE isolates metadata statistics.csv'
				
				sampling_report_file = ReportsDir + 'DATABASE sampling report.txt'
				
				Clear_screen(OperatingSystem)
				
				Fetch_accession_numbers(Collection, database, accession_number_field, keep_entry_key, keep_entry_val, isolates_metadata_keys, metadata_file, metadata_csv_file, metadata_csv_file_headers, statistics_file, statistics_csv_file, sampling_report_file, DefaultDirectoryRoot, CustomDirectoryRoot)
				
			else:
				
				print(f'\n\n\n\nFile not found:\n\n{input_file}\n\n\n')
			
			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
			
		# (21) Fetch DATABASE isolates’ metadata with field specific keywords
		
		elif choice == "5":
			
			Clear_screen(OperatingSystem)
			
			print('You are using DATABASE.\n\n\n\n\n')
			
			print('Uploading DATABASE database to memory...\n\n')
			
			input_file = DatabasesDictionariesDir + "DATABASE_E coli_Complete genome_Metadata_list.txt"
			
			File_checking_result = File_checking(input_file)
			
			if File_checking_result == True:
				
				if DATABASECollection == []:
					f = open(input_file, "r", encoding='utf-8')
					contents = f.read()
					f.close()
					DATABASECollection = ast.literal_eval(contents)
				else:
					pass
				
				Collection = DATABASECollection
				
				database = 'DATABASE'
				accession_number_field = 'DATABASE NCBI ACCESSION NUMBER FIELD'
				
				keep_entry_key = 'keep entry'
				keep_entry_val = 'y'
				
				VAR1 = 'VAR1'
				VAR2 = 'VAR2'
				VAR3 = 'VAR3'
				VAR4 = 'VAR4'
				VAR5 = 'VAR5'
				...
				
				isolates_metadata_keys = (VAR1_key, VAR2_name_key, VAR3_country_key, VAR4_key, VAR5_source_key, ...)
				
				metadata_file = SamplesMetadataDir + 'DATABASE isolates metadata.txt'
				metadata_csv_file = SamplesMetadataDir + 'DATABASE isolates metadata.csv'
				
				metadata_csv_file_headers = ('Keep entry?' + ',' + 'DATABASE NCBI ACCESSION NUMBER FIELD' + ',' + 'VAR1' + ',' + 'VAR2' + ',' + 'VAR3' + ',' + 'VAR4' + ',' + 'VAR5' + ',' + ... + '\n')

				statistics_file = SamplesMetadataDir + 'DATABASE isolates metadata statistics.txt'
				statistics_csv_file = SamplesMetadataDir + 'DATABASE isolates metadata statistics.csv'
				
				sampling_report_file = ReportsDir + 'DATABASE sampling report.txt'
				
				dict_key_options_tuple = ('VAR1', 'VAR2', 'VAR3', 'VAR4', 'VAR5', ...)
				dict_key_options_menu = ('(1) VAR1\n(2) VAR2\n(3) VAR3\n(4) VAR4\n(5) VAR5...')
				options = ('1','2','3','4','5',...)
				
				Clear_screen(OperatingSystem)
				
				Fetch_accession_numbers_searching_dict_keys(Collection, database, accession_number_field, keep_entry_key, keep_entry_val, isolates_metadata_keys, metadata_file, metadata_csv_file, metadata_csv_file_headers, statistics_file, statistics_csv_file, sampling_report_file, dict_key_options_tuple, dict_key_options_menu, options, DefaultDirectoryRoot, CustomDirectoryRoot)
		
			else:
				
				print(f'\n\n\n\nFile not found:\n\n{input_file}\n\n\n')
		
			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
		
		# (22) Exclude / Reinclude DATABASE isolates’ from sample
		
		elif choice == "6":
			
			Clear_screen(OperatingSystem)
			
			print('You are using DATABASE.\n')
			
			accession_number_field = 'DATABASE NCBI ACCESSION NUMBER FIELD'
			
			metadata_csv_file = SamplesMetadataDir + 'DATABASE isolates metadata.csv'
			accession_numbers_file = SamplesAccessionNumbersDir + 'DATABASE_accession numbers.txt'
			accession_numbers_BU_file = SamplesAccessionNumbersDir + 'DATABASE_accession numbers_BU.txt'
			removed_accession_numbers_file = SamplesAccessionNumbersDir + 'DATABASE_accession numbers_RM.txt'
			
			File_checking_result = File_checking(metadata_csv_file)
			file1 = File_checking_result
			File_checking_result = File_checking(accession_numbers_file)
			file2 = File_checking_result
			
			if file1 == True and file2 == True:
			
				Clear_screen(OperatingSystem)
				
				Edit_accession_numbers_list(accession_number_field, metadata_csv_file, accession_numbers_file, accession_numbers_BU_file, removed_accession_numbers_file, DefaultDirectoryRoot, CustomDirectoryRoot)
			
			else:
				
				print(f'\n\n\n\nFile(s) not found:\n\n{metadata_csv_file}\n\nand / or\n\n{accession_numbers_file}\n\n\n')
				option = 1
				Press_a_key(OperatingSystem, option)
			
			choice = ""
			Clear_screen(OperatingSystem)
		
		# (23) Describe DATABASE sample with tables
		
		elif choice == "7":
			
			Clear_screen(OperatingSystem)
			
			print('You are using DATABASE.\n')
			
			database = 'DATABASE'
			graphics_option = 'n'
			
			VAR1 = 'VAR1'
			VAR2 = 'VAR2'
			VAR3 = 'VAR3'
			VAR4 = 'VAR4'
			VAR5 = 'VAR5'
			...
			
			isolates_metadata_keys = (VAR1, VAR2, VAR3, VAR4, VAR5, ...)
			
			statistics_csv_file = SamplesMetadataDir + 'DATABASE isolates metadata statistics.csv'
			sample_summary_file = SamplesMetadataDir + 'DATABASE isolates metadata summary.txt'
		
			File_checking_result = File_checking(statistics_csv_file)
			
			if File_checking_result == True:
		
				Clear_screen(OperatingSystem)
				
				Summarize(graphics_option, isolates_metadata_keys, statistics_csv_file, database, sample_summary_file, DefaultDirectoryRoot, CustomDirectoryRoot)
			
			else:
				
				print(f'\n\n\n\nFile(s) not found:\n\n{statistics_csv_file}\n\nand / or\n\n{sample_summary_file}\n\n\n')
			
			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)
		
		# (24) Describe DATABASE sample with graphics
		
		elif choice == "8":
			
			Clear_screen(OperatingSystem)
			
			print('You are using DATABASE.\n')
			
			database = 'DATABASE'
			graphics_option = 'y'
			
			VAR1 = 'VAR1'
			VAR2 = 'VAR2'
			VAR3 = 'VAR3'
			VAR4 = 'VAR4'
			VAR5 = 'VAR5'
			...
			
			isolates_metadata_keys = (VAR1, VAR2, VAR3, VAR4, VAR5, ...)
			
			statistics_csv_file = SamplesMetadataDir + 'DATABASE isolates metadata statistics.csv'
			sample_summary_file = SamplesMetadataDir + 'DATABASE isolates metadata summary.txt'
			
			File_checking_result = File_checking(statistics_csv_file)
			
			if File_checking_result == True:
			
				Clear_screen(OperatingSystem)
				
				Summarize(graphics_option, isolates_metadata_keys, statistics_csv_file, database, sample_summary_file, DefaultDirectoryRoot, CustomDirectoryRoot)
			
			else:
				
				print(f'\n\n\n\nFile(s) not found:\n\n{statistics_csv_file}\n\nand / or\n\n{sample_summary_file}\n\n\n')
		
			choice = ""
			option = 1
			Press_a_key(OperatingSystem, option)
			Clear_screen(OperatingSystem)

'''
	