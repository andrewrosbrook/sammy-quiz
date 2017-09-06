import md5
import pickle
from random import randint

def load_pkl(fn):
	inp = open(fn, "rb")
	x = pickle.load(inp)
	inp.close()
	return x

def check_answer(num, ans):
        expected = answers[num]
        actual = md5.new(ans).hexdigest()
	if actual == expected:
		print "Correct! " + titbits[num]
		print
		return True
	else:
		return False	

def ask_until_correct(num, text):
	while(not check_answer(num, raw_input(text + " "))):
		print "\tIncorrect!"
		demotivate()
		print ""

def demotivate():
	idx = randint(0, len(demotivate_messages)-1)
	print "\t" + demotivate_messages[idx]

demotivate_messages = [ "Oh Sammy Sammy Sammy", "I'm sure Ahmmad could answer this one...", "Should we ask Sourav?",
"The first stop towards failure is trying", 
"If at first you don't succeed, give up and try something else",
"Optimism, the prelude to disappointment" ]

questions = load_pkl("questions.pkl")
answers = load_pkl("answers.pkl")
titbits = load_pkl("titbits.pkl")

banner = """ \

db   d8b   db d88888b db       .o88b.  .d88b.  .88b  d88. d88888b      .d8888.  .d8b.  .88b  d88. .88b  d88. db    db db 
88   I8I   88 88'     88      d8P  Y8 .8P  Y8. 88'YbdP`88 88'          88'  YP d8' `8b 88'YbdP`88 88'YbdP`88 `8b  d8' 88 
88   I8I   88 88ooooo 88      8P      88    88 88  88  88 88ooooo      `8bo.   88ooo88 88  88  88 88  88  88  `8bd8'  YP 
Y8   I8I   88 88~~~~~ 88      8b      88    88 88  88  88 88~~~~~        `Y8b. 88~~~88 88  88  88 88  88  88    88       
`8b d8'8b d8' 88.     88booo. Y8b  d8 `8b  d8' 88  88  88 88.          db   8D 88   88 88  88  88 88  88  88    88    db 
 `8b8' `8d8'  Y88888P Y88888P  `Y88P'  `Y88P'  YP  YP  YP Y88888P      `8888Y' YP   YP YP  YP  YP YP  YP  YP    YP    YP 
                                                                                                                         
                                                                                                                         

Hello Sammy!

Many congratulations on the Wedding! Giving you a card with a voucher would be a little too easy...you have to do a bit of work first!

You are required to answer a series of questions, for the chance to win an Amazon Gift Card :-)!

There is only one IMPORTANT rule to remember:
	All answers must be lower case

Good Luck!

Andy

                                                                                                                                                                          
"""

print banner

ask_until_correct(1, questions[1])
ask_until_correct(2, questions[2])
ask_until_correct(3, questions[3])

print
print "Congratulations!!"
print 
print "Obviously I cannot expose the Amazon voucher code on GitHub, so please let me know you successfully passed the quiz :-)!"
print
print "Good luck at the wedding!"
print 
print "--------------------------------------------------------"
print 

