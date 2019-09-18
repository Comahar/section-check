import os.path
def main():
	if(not os.path.exists('config.txt')):
		print("config.txt file does not exists. Generating.\nClose and change values to your needs.")
		f = open("config.txt")
	f = open("config.txt")

	semesterInput = f.readline()
	semesterSwitch = {
		"fall" : 1,
		"spring": 2,
		"summer": 3
	}
	if(semesterInput.lower()[:-1] in semesterSwitch.keys()):
		semester = semesterSwitch[semesterInput.lower()[:-1]]
	else:
		print("Wrong semester input. Exiting.")
		return

	depts = []
	courseCodes = []
	sections = []
	lines = f.readlines()
	for i in range(len(lines)):
		line = lines[i]
		try:
			line = line.rstrip('\n')
			depts.append(line.split("-")[0])
			courseCodes.append(line.split("-")[1])
			if(line.count("-")==2):
				sections.append(line.split("-")[2].split(","))
			else:
				sections.append([])
		except Exception:
			print("Format Error in line", i, " ", line)
			return

	import sectioncheck
	handler = sectioncheck.courseCrawlerHandler(depts, courseCodes, sections, semester)

	while True:
		try:
			inText = input("Write exit to exit.\nWrite course to check current courses.\n")
			if(inText == "exit"):
				handler.exit()
				return
			elif(inText == "course"):
				# for i in range(len(depts)):
				# 	print(depts[i], courseCodes[i], sections[i])
				handler.print()
		except Exception as e:
			print(e)
			return

main()
input("Press enter to exit")
