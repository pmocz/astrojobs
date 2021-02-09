"""
astrojobs: Get latest astronomy job and rumor news in your command line

Project website: https://github.com/pmocz/astrojobs

The MIT License (MIT)
Copyright (c) 2021 Philip Mocz (pmocz)
http://opensource.org/licenses/MIT
"""
from __future__ import absolute_import, print_function

import difflib
import os
from shutil import copyfile
import sys
from argparse import ArgumentParser
from distutils.version import StrictVersion

import bs4 as bs
import requests
import urllib.request
from wasabi import color


__version__ = "0.0.2"
dir_path = os.path.dirname(os.path.realpath(__file__))



def printDiff(file1, file2):
	text1 = open(file1).readlines()
	text2 = open(file2).readlines()
	diff = difflib.ndiff(text1, text2)
	for l in diff:
		if (l[0] == "+"):
			print(color(l[2:], fg="green"))
		elif (l[0] == "-"):
			print(color(l[2:], fg="red"))
		




def check_aas_updates(jobType):
	### List New Job Openings from AAS Job Register
	if(jobType == 'faculty'):
		jobTypeId = 'FacPosTen'
	elif(jobType == 'postdoc'):
		jobTypeId = 'PostDocFellow'
	
	source = urllib.request.urlopen('https://jobregister.aas.org/').read()
	
	soup = bs.BeautifulSoup(source,'html.parser')
	
	jobs = soup.find(id=jobTypeId).nextSibling.find_all('td')
	
	N = int(len(jobs)/6)
	
	jobfile = dir_path + '/sav_' + jobType + '.txt'
	jobfile_old = dir_path + '/sav_' + jobType + '_old.txt'
	
	if not os.path.exists(jobfile_old):
		open(jobfile_old,"w+").close()
	
	### save new jobs ###
	f = open(jobfile,"w+")
	cc = 0
	sep = "   ||  "
	for i in range(0,N):
		line = "https://jobregister.aas.org" + str(jobs[cc]);
		line = line.replace('<td class="ad_status_new"><a href="','');
		line = line.replace('<td class=""><a href="','');
		line = line.replace('">',' ');
		line = line.replace('</a></td>','');
	
		cc +=1
		line = line + sep + str(jobs[cc]);
		cc +=1
		#line = line + sep + str(jobs[cc]);
		line = line.replace('<td>','');
		line = line.replace('</td>','');
		line = line + '\n';
		cc +=4
	
		f.write(line)
	
	f.close()
	
	print('=======================================================')
	print('NEW ' + jobType + ' jobs on https://jobregister.aas.org')
	print('=======================================================')
	
	# Print differences
	#os.system('colordiff ' + jobfile_old + ' ' + jobfile)
	printDiff(jobfile_old,jobfile)
	
	# save jobs as oldjobs
	copyfile(jobfile, jobfile_old)
	
	print(jobType + ' job check complete!\n')





def check_rumormill_updates(jobType):
	### List New Rumors from the Rumor Mill
	if(jobType == 'faculty'):
		jobTypeId = 'Rumor+Mill+Faculty-Staff'
	elif(jobType == 'postdoc'):
		jobTypeId = 'Rumor+Mill'
	
	source = urllib.request.urlopen('https://www.astrobetter.com/wiki/'+jobTypeId).read()
	
	soup = bs.BeautifulSoup(source,'html.parser')
	
	jobs = soup.find_all('td')
	
	jobfile = dir_path + '/sav_' + jobType + '_rumor.txt'
	jobfile_old = dir_path + '/sav_' + jobType + '_rumor_old.txt'
	
	if not os.path.exists(jobfile_old):
		open(jobfile_old,"w+").close()
	
	### save new rumors ###
	f = open(jobfile,"w+")
	cc = 0
	for line in jobs:
		newline = "   ||  "
		if ((cc % 2) == 1):
			newline = "\n"
		line = str(line)
		line = line.replace('<td>','')
		line = line.replace('</td>','')
		line = line.replace('<a href=','')
		line = line.replace('</a>','')
		line = line.replace('>ad','')
		line = line.replace('<a class=','')
		line = line.replace('<p>','')
		line = line.replace('</p>','')
		line = line.replace('<br/>','')
		line = line.replace('<td width="300">','')
		line = line.replace('<td width="434">','')
		line = line.replace('<td width=','')
		line = line.replace('\n','   ')
		#line = line.replace('<','')
		#line = line.replace('>','')
		line = line + newline
		f.write(line)
		cc += 1
	
	f.close()
	
	print('=======================================================')
	print('NEW ' + jobType + ' rumors')
	print('=======================================================')
	
	# Print differences
	#os.system('colordiff ' + jobfile_old + ' ' + jobfile)
	printDiff(jobfile_old,jobfile)
	
	# save jobs as oldjobs
	copyfile(jobfile, jobfile_old)
	
	print(jobType + ' rumor mill check complete!\n')




### Main
def main():
	
	parser = ArgumentParser()
	parser.add_argument(
		"-f",
		"--faculty",
		action="store_true",
		help="show updates for faculty jobs/rumors",
	)
	parser.add_argument(
		"-p",
		"--postdoc",
		action="store_true",
		help="show updates for postdoc jobs/rumors",
	)
	parser.add_argument(
		"--version",
		action="version",
		version="%(prog)s {version}".format(version=__version__),
	)
	args = parser.parse_args()
	
	if len(sys.argv)==1:
		print('=======================================================')
		print('astrojobs: get astro job/rumor updates in terminal since last check')
		print('=======================================================\n')
		parser.print_help()
	
	
	# show postdoc updates
	if args.postdoc:
		check_aas_updates("postdoc")
		check_rumormill_updates("postdoc")
		
		
	# show faculty updates
	if args.faculty:
		check_aas_updates("faculty")
		check_rumormill_updates("faculty")
	

	# check version
	try:
		latest_version = StrictVersion(
			requests.get(
				"https://pypi.python.org/pypi/astrojobs/json", timeout=0.1,
			).json()["info"]["version"]
		)
	except (requests.RequestException, KeyError, ValueError):
		pass
	else:
		if latest_version > StrictVersion(__version__):
			msg = "A newer version of astrojobs (v{}) is now available!\n".format(
				latest_version
			)
			msg += "Please consider updating it by running:\n\n"
			msg += "pip install astrojobs=={}".format(latest_version)
			print(_headerize(msg))



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(_headerize("Abort! astrojobs interupted by a keyboard signal!"))
