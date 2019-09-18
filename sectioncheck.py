import pyglet
import datetime
import urllib.request
import threading
import time


class CourseCrawler(threading.Thread):
    def __init__(self, thread_id, dept, sections, semester, sleep_time=5):
        threading.Thread.__init__(self)
        self.year = datetime.datetime.now().date().year
        self.semester = ""
        self.url = "https://stars.bilkent.edu.tr/homepage/ajax/plainOfferings.php?COURSE_CODE=" + str(dept) + "&SEMESTER=" + str(self.year) + str(semester)
        self.thread_id = thread_id
        self.dept = dept
        self.sections = []
        self.stop = False
        self.current_area = ""
        self.sleep_time = sleep_time
        self.start_time = datetime.datetime.now()
        for section in sections:
            self.sections.append(dept + ' ' + section)

    def run(self):
        while not self.stop:
            with urllib.request.urlopen(self.url) as f:
                area = False
                for line in f:
                    line = line.decode('utf-8')

                    for section in self.sections:
                        if section in line:
                            self.current_area = section
                            area = True

                    if area is True:
                        if self.is_avalible(line):
                            self.found()

                    if 'images/icon_desc.gif' in line:
                        area = False
            time.sleep(self.sleep_time)

    def stop_t(self):
        self.stop = True

    def __str__(self):
        return "\nThread " + str(self.thread_id) + " is searching for " + str(self.sections) + " since " + str(self.start_time) + "\n"

    @staticmethod
    def is_avalible(line):
        return ("Must or Elect" in line) and (int(line.split("<td align='center'>")[7].split("</td>")[0]) != 0)

    def found(self):
        print("Found: {0}, {1}.".format(self.dept, self.current_area))
        song = pyglet.media.load('siren.wav')
        song.play()
        pyglet.app.run()


class courseCrawlerHandler():
    def __init__(self, depts, courseCodes, sections, semester):
        try:
            f = open("siren.wav")
            f.close()
        except Exception:
            print("siren.wav not found. This will error")
        self.depts = depts
        self.courseCodes = courseCodes
        self.sections = sections
        self.semester = semester
        self.threads = []
        print("Searching for:")
        for i in range(len(depts)):
            formattedSections = []
            if(sections[i] == []):
                formattedSections.append(courseCodes[i])
            else:
                for section in sections[i]:
                    formattedSections.append(courseCodes[i] + "-" + section)
            crawler = CourseCrawler(i, depts[i], formattedSections, semester)
            self.threads.append(crawler)
            crawler.start()
    def exit(self):
        for thread in self.threads:
            thread.stop_t()
            thread.join()
        pyglet.app.exit()
    def print(self):
        for thread in self.threads:
            print(str(thread))
