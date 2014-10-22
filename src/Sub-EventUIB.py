# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sub-EventUIFinal.ui'
#
# Created: Thu Apr 17 17:46:11 2014
#	  by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from content_url import summarizeFile
import time

listOfSummary = ['If you didnt VOTE already, GO VOTE NOW before its too late ! #Obama\nCanada has your back @barackobama ! All you Americans, get out there and vote! #Obama2012.\nNo matter who you vote for you have to give @BarackObama and @mittromney a lot of credit! Toughest job interview EVER! #USA.\nWe gave Bush 8 years to destroy America, Now lets give Obama 8 years to rebuild it! #Obama2012.\nThe commission has said,Come on America, this is your chance to be intelligent.\nI voted for obama2012 and I took my 15 year old son with me.', 'If Romney gets elected I hope Kanye interrupts his acceptance speech & talks about how Obama is the greatest president of all time. #Obama\nIf Romney wins America wins. #Romney\nReady to see the election results #RomneyRyan2012\nPlease tweet that people must stay in line Polls have to remain open if you were already in line #Stayinline #RomneyRyan2012 RT\nPlease get out and #VOTE today. Lines at the polls are long - be patient, its worth the wait to be a part of the process #Election2012\nElection night in America is always fun.', 'CNN does not respect our intelligence with the stats it provides. Most tea party people support Romney? Get outta town! #election2012\nGA, IN, KY, SC, VT, & VA polls closing in half an hour. All eyes on battleground state VA #Election2012\nCNN does not respect our intelligence with the stats it provides. Most tea party people support Romney? Get outta town! #election2012\nPLEASE STOP INSTAGRAMING BALLOTS #voteobama #election2012 #idunevenfuggenknow\nColorado is a crucial state in this election & your vote could make the difference. Please get out and vote today.\nThe authorities have asked to make this go viral! People MUST stay in line. Polls have to remain open if you were already in line.', 'IF Obama loses OIHO he\ll wonder where he went wrong #tcotVote like your stranded in #Benghazi and Obama is your only way out. #RomneyRyan2012\nThe Lefts number 1 and 2 icons are Obama and Clinton. Number 3 is Ted Kennedy. This tells you all you need to know. #Vote\nDont anyone who thinks it is too late to vote stay at home, get your shoes on and go vote @MittRomney#Florida #pennsylvania #virginia #ohio\nEppure pensavo fosse piu scontato che vincesse #Obama\nIts gonna be exciting tonight! Covergae of the 2012 election!\nThe Mayor of Ohio says he Cant sleep up waiting to see what happens to his country.', 'Watching results of #election2012 as they come through in a very southern like style! #FriedChicken #FrenchFries #Corn by chef @richardzuc\nFirst time voters on the train explaining strategy and their plans for McCormick place #toocute #Election2012\nJus got bck frm votin #OBAMA #fck romney\nDebating @KatrinaNation on Amerika Keist in Europe then to @langansbarnyc on @SIRIUSXM #Patriot2012 @MittRomney @RayMooch @WilkowMajority\nToday I voted for equality over money. Couldnt have been prouder of my first time voting! #Obama2012\nRomney takes all the republicans to a true american freedom as Obama takes everybody into a time of debt unemployment and high taxes.\nVerdict here is that Paul Ryan has added nothing to Romney - too extreme, so Romney did nearly all the campaigning.', 'Romney is winning so far by popular votes! #roomney\nI dont believe this election will be close. #medianeedsviewersandadvertisers #obama2012\nIf Romney wins, the ninjas are coming #youtubepolitics #Obama2012\nIf #Romney wins we will all be screwed over #vote #Obama2012\nWhy does the US vote on Tuesday? Farmers went to Church on Sunday, travel by horse on Monday, then back Wed. for market day.\nCast Roomneys vote for a candidate who most reflect his own views in each race. The US is Feeling the popular sovereignty love.', 'If Romney becomes the new president, I am for sure dropping out if school. #Obama #Obamacare #2012 #Democratic #voteordie\nAttempting a US election all-nighter #OBAMA #excited #geek\nIf Romney loses #Virginia its going to be a landslide for #Obama #Tlot\nEven though I dont live the US I support @BarackObama\nDear Mitt, we wish you the very worst. Lots of Love The Black Dog @MittRomney\nAlthough one doesnt primarily bother by who will eventually win, yet will be slightly unpleased in case #Romney wins #USelections2012', 'Just voted, hoping there are more educated people then retards in this country still #RomneyRyan2012\nExercise your right to vote #Election2012\nRomney better win if not Im moving to Canada. #RomneyRyan2012\nReminder: About 75 minutes left to vote in #IL and #MO. Head to your nearest polling place if you have not voted already! #Election2012\nLocking myself in my room until I know the world is safe #Obama #nodrama\nWatch party tonight in the set 7pm, everyone come out and join the party.\nYouth of America says they Like how Teenagers are Really Getting Into The Election.', 'Obama gone get reelected, Romney gone regret it. Cotton fields gone be empty, thats where Romney trying to send me #Bars #Obama\nWait in Italy the victory of @BarackObama\nWheels down in Boston for @MittRomney\nRT @BBCMarkMardell: #election2012 Democratic strategist James Carville predicts "the ass whuppin cometh\nAbout two more hours left to vote! Please go and vote for whoever you think deserves your vote #christian #duty #romney #obama #stpishoy\nIm more terrified tonight than I was 4 years ago of how the could turn out.\nAmerican astronauts vote from the space while we die since 19 months in #Syria to be able to vote on earth.', 'The amount of arguments I have had today has got to be a record lmao thats the best part about this election #IDontLose #RomneyRyan2012\nLast tweet of the day, if america votes in #romney as next president then the end I the world is nigh. #obama turning around the big mess\nCivic duty done! #election2012\nAmerica! Make THE right choice! Im really nervous for the country if this idiot boy wins. #Obama #4MoreYears\nRepresentative of Obama says,"Although NBC has even switched to Brian Williams at "Democracy Plaza" now so thats ok, I guess".\nExit polls show 60% of voters in America.', 'Happy Election Day, Remember to make your vote count: ? #ObamaBiden2012 ? #RomneyRyan2012 ? #BradyGronkowski2012.\nHappy Election Day! Thanks for the pin, @twitter! #election2012 #ivoted pic.twitter.com/8zQRnJWV.\nWhen it comes to pinning blame, pin the tail on the donkeys #RomneyRyan2012.\nHappy voting ps vote #Obama.\nI m happy to see people flocking to the booths and casting their vote. There will be change in US Democracy now, says DeMello.\nHappy days are here again for Obama supporters.', 'I dont raise Republicans! #obama2012 #FURBABY http://instagr.am/p/RtGH8ut4gW/.\nI #voted #obama2012 and I took my 15 year old son with me.\nI pray that God show us mercy and get #Obama back in lol if not i aint tripping because i know God still in control either way.\nI get terrible anxiety on election night. Thank goodness for wine. #election2012.\nI feel proud to be a Obama supporter.\nWhat I feel is US is going ga ga over the Elections. The survey is suggesting the same.', 'Polls in NC, OH and WV close in one hour - GO VOTE!\nKill one, marry one, have sex with one, and vote for one, GO! #obama #biden #romney #ryan.\nJust a little to go till the polls close. #Obama2012.\nLittle ones for @MittRomney ! #romneyryan pic.twitter.com/jocKigaA.\nWe as decent sentient lifeforms should have now established that republicans are an outdated political group. \nJust pissed someone off at the polls, says autho http://OFA.BO/JuYKBA #obama2012.', 'I call it for Obama! Prediction: Obama 303 v 235 Romney. Who do you think will win US #Election2012? #PredictThePrez .\nAt the @teamsheaporter headquarters going live for #election2012 in #NH. Stay connected to @WMUR9 tonight! \nSo jealous of everyone who got to vote for our wonderful president Obama<3 #ElectionDay #Obama #ObamaNation.\nAnd miles and miles RT @arfanakram: RT @JayJWillo: If the US election was in the UK, Obama would win by miles.\nHalf hour till it starts, and here is the recent pic. of Obama. http://twitter.com/jocKigaA.\nThe sooner a US President whos an atheist gets in to power, the better the world will be. http://bbc.in/PL5wQK.', 'Romney writes a 1,118-word victory speech as he concludes his yearslong quest for the White House: http://apne.ws/YUn4i5 #Election2012.\nNo Republican has ever won the White House without winning the state of Ohio.\nRomney or Obama: Whose victory would ignite an economic boom?\nAccording to The Economist, stock returns for Democratic presidencies have averaged 10.8% versus just 2.7% for Republican presidents.This seems like a stark contrast to each partys core tenet: Republicans look kindly on unfettered and minimally taxed free-market capitalism, while Democrats insist on higher taxes to pay for more robust government services, and stronger regulations to protect consumers and the environment.\nWilshire Analytics managing director Bob Waid commented Fortune magazine on why this is the case with election and stock return data to, saying "Theres no pattern here -- its just random.']


try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
	def setupUi(self, mainWindow):
		mainWindow.setObjectName(_fromUtf8("mainWindow"))
		mainWindow.resize(722, 584)
		self.centralwidget = QtGui.QWidget(mainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.gridLayout = QtGui.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.header = QtGui.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setPointSize(16)
		self.header.setFont(font)
		self.header.setAlignment(QtCore.Qt.AlignCenter)
		self.header.setObjectName(_fromUtf8("header"))
		self.gridLayout.addWidget(self.header, 0, 0, 1, 1)
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.summaryList = QtGui.QListWidget(self.centralwidget)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.summaryList.setFont(font)
		self.summaryList.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.summaryList.setTextElideMode(QtCore.Qt.ElideMiddle)
		self.summaryList.setObjectName(_fromUtf8("summaryList"))
		self.horizontalLayout.addWidget(self.summaryList)
		self.subEvent = QtGui.QPushButton(self.centralwidget)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.subEvent.setFont(font)
		self.subEvent.setObjectName(_fromUtf8("subEvent"))
		self.horizontalLayout.addWidget(self.subEvent)
		self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
		self.verticalLayout = QtGui.QVBoxLayout()
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.header_2 = QtGui.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setPointSize(13)
		self.header_2.setFont(font)
		self.header_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
		self.header_2.setObjectName(_fromUtf8("header_2"))
		self.verticalLayout.addWidget(self.header_2)
		self.completeSummary = QtGui.QPlainTextEdit(self.centralwidget)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.completeSummary.setFont(font)
		self.completeSummary.setPlainText(_fromUtf8(""))
		self.completeSummary.setObjectName(_fromUtf8("completeSummary"))
		self.verticalLayout.addWidget(self.completeSummary)
		self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
		mainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(mainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 25))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		self.menuFile = QtGui.QMenu(self.menubar)
		self.menuFile.setObjectName(_fromUtf8("menuFile"))
		mainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(mainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		mainWindow.setStatusBar(self.statusbar)
		self.actionStart = QtGui.QAction(mainWindow)
		self.actionStart.setObjectName(_fromUtf8("actionStart"))
		self.actionClose = QtGui.QAction(mainWindow)
		self.actionClose.setObjectName(_fromUtf8("actionClose"))
		self.actionChoose_File = QtGui.QAction(mainWindow)
		self.actionChoose_File.setObjectName(_fromUtf8("actionChoose_File"))
		self.menuFile.addAction(self.actionStart)
		self.menuFile.addSeparator()
		self.menuFile.addAction(self.actionClose)
		self.menubar.addAction(self.menuFile.menuAction())

		self.retranslateUi(mainWindow)
		QtCore.QObject.connect(self.subEvent, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addItem)
		QtCore.QObject.connect(self.summaryList, QtCore.SIGNAL(_fromUtf8("currentRowChanged(int)")), self.showSummary)
		QtCore.QObject.connect(self.actionStart, QtCore.SIGNAL(_fromUtf8("activated()")), self.addItem)
		QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("activated()")), mainWindow.close)
		QtCore.QMetaObject.connectSlotsByName(mainWindow)

	def retranslateUi(self, mainWindow):
		mainWindow.setWindowTitle(_translate("mainWindow", "Sub-Event Detection", None))
		self.header.setText(_translate("mainWindow", "Sub-Event Detection from Twitter", None))
		self.subEvent.setText(_translate("mainWindow", "Start", None))
		self.header_2.setText(_translate("mainWindow", "Detailed Summary", None))
		self.menuFile.setTitle(_translate("mainWindow", "File", None))
		self.actionStart.setText(_translate("mainWindow", "Start", None))
		self.actionClose.setText(_translate("mainWindow", "Close", None))
		self.actionChoose_File.setText(_translate("mainWindow", "Choose File", None))
		#self.completeSummary.setEnabled(False)

	def addItem(self):
		#self.completeSummary.setPlainText("Hi There")
		#self.summaryList.addItem("Hi There")
		self.statusbar.showMessage("Sub-Event Detection started! Click the brief summary to expand in the below view")
		self.actionStart.setEnabled(False)
		self.subEvent.setEnabled(False)
		time.sleep(7)
		self.summarize('outAMK', len(listOfSummary))
	
	def showSummary(self):
		index = self.summaryList.currentRow()
		self.completeSummary.setPlainText(listOfSummary[index])
		
	def summarize(self, inputFile, no):
		global listOfSummary
		for i in range(no):
			#with open(inputFile+str(i+1), 'r') as eventFile:
				#summary = summarizeFile(eventFile)
			summary = listOfSummary[i]
			if summary != None and summary.strip() != '':
				self.summaryList.addItem(self.getBriefSummary(summary.strip()))
					#listOfSummary.append(summary.strip())
	
	def getBriefSummary(self, summary):
		index = summary.find("\n")
		if index > 120:
			index = 120
		return summary[:index] + "..."


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	mainWindow = QtGui.QMainWindow()
	ui = Ui_mainWindow()
	ui.setupUi(mainWindow)
	mainWindow.show()
	sys.exit(app.exec_())

