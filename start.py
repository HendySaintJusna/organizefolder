from django.shortcuts import render
from array import array
import shutil
import time
import os



audios = [
	".aif",
	".cda",
	".mid",
	"midi",
	".mp3",
	".mpa",
	".ogg",
	".wav",
	".wma",
	".wpl",
	"Audio"
]

compressedfiles = [
	".7z",
	".arj",
	".deb",
	".pkg",
	".rar",
	".rpm",
	".tart.gz",
	".z",
	".zip",
	"Compressed Files"
]

disc = [
	".bin",
	".dmg",
	".iso",
	".toast",
	".vcd",
	"Disc"
]

datas = [
	".cvs",
	".dat",
	".db",
	".dbf",
	".log",
	".mbd",
	".sav",
	".sql",
	".tar",
	"xml",
	"Data"
]

emails = [
	"email",
	".eml",
	".emlx",
	".msg",
	".oft",
	".ost",
	".pst",
	".vcf",
	"E-mail"
]

executables = [
	".apk", 
	".bat",
	".bin",
	".cgi",
	".pl",
	".com", 
	".exe", 
	".gadget", 
	".jar", 
	".msi", 
	".py", 
	".wsf", 
	"Executables"
]

images = [
	".ai",
	".bmp",
	".gif",
	".ico",
	".jpg",
	".jpeg",
	".tiff",
	".png",
	".ps",
	".psd",
	".svg",
	".tif",
	".webp",
	"Images"
]

programming_and_script = [
	".asp",
	".cer",
	".cfm",
	".html",
	".cgi",
	".css",
	".htm",
	".js",
	".jsp",
	".part",
	".php",
	".py",
	".rss",
	".xhtml",
	".aspx",
	".pl",
	".c",
	".cgi",
	".class",
	".cpp",
	".cs",
	".h",
	".java",
	".php",
	".py",
	".sh",
	".swift",
	".vb",
	".pl",
	"Programming & Script"
]

presentation = [
	".key",
	".odp",
	".pps",
	".ppt",
	".pptx",
	".ppsx",
	"Font Files"
]

speadsheets = [
	"ods",
	".xls",
	".xlsm",
	".xlsx",
	"Speadsheet"
]

system = [
	".bak",
	".cab",
	".cfg",
	".cpl",
	".cur",
	".dll",
	".dmp",
	".drv",
	".icns",
	".ico",
	".ini",
	".lnk",
	".msi",
	".sys",
	".tmp",
	"System"
]

video = [
	".3g2",
	".3gp",
	".avi",
	".flv",
	".h264",
	".m4v",
	".mkv",
	".mov",
	".mp4",
	".mpg",
	".rm",
	".swf",
	".vob",
	".webm",
	".wmv",
	".mpeg",
	".aep",
	".prproj",
	"Video"
]

word = [
	".doc",
	".odt",
	".pdf",
	".rtf",
	".tex",
	".txt",
	".wpd",
	".docx",
	"Docs"
]

all_type = [audios,compressedfiles,disc,datas,emails,executables,images,programming_and_script,presentation,speadsheets,system,video,word]
duplicate = []
quit = 0



while quit == 0:
	try:
		your_path = input("Copy the path of the folder you want to organise or write 'quit' to exit: ")
		all_folder_file = os.listdir(your_path)
		if your_path == 'quit':
			quit = 1
	except:
		print("[HELP] : WRITE A VALID FOLDER PATH")

	if quit == 1:
		print("EXIT")
	else:

		try:

			for file in all_folder_file:
				filepath = your_path + '/' + file
				filename, file_extension = os.path.splitext(filepath)
				if file_extension == "":
					pass
				else:
					for x in all_type:
						for z in x:
							if z == file_extension:
								created_folder = your_path + '/' + x[-1]
								print(created_folder)
								if not os.path.exists(created_folder):
									os.makedirs(created_folder)
								print("PLACING : " + file + " ...")
								if file in duplicate:
									pass
								else:
									shutil.move(filepath, created_folder)
									duplicate.append(file)
					
					if os.path.exists(filepath):
						created_folder = your_path + '/' + "Unclassified Files"
						if not os.path.exists(created_folder):
							os.makedirs(created_folder)	
						shutil.move(filepath, created_folder)

					duplicate = []

			print("TASK FINISHED!")

		except:
			print("OOPS! Something went wrong...")