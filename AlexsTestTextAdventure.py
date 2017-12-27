import time
import random

def game():

	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("Welcome to Atta, the Lost City of Mice")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	
	name = input("What is your name? ")
	
	if name in ["Alex","alex","Aiden","aiden","Alexei","alexei"]:
		print("Oh, that is a legendary name!")
		
	furColour = input("What colour is your fur, little one? ")
	
	age = int(input("How old are you? "))
	
	gender = input("Are you male or female? (M/F) ")
	
	trait = input("Would you describe yourself as faster, stronger, or wiser? (f/s/w) ")
	
	print("Here in Atta, there are 3 major clans: the Skaw Clan, the Gibbers Clan, and the Birdleaf Clan.")
	
	clanCount = 0
	
	while (clanCount == 0):
	
		clan = input("To which clan do you belong? (Skaw, Gibbers, or Birdleaf) ")
	
		if clan in ["Skaw","skaw"]:
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			print("Skaw Clan is led by the wise old Diego,")
			print("a snowy white mouse trained in the way")
			print("of the sword and dagger.")
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			clanLeader = "Diego"
			clanWeapon = "dagger"
			clanSymbol = "badger"
			clanCount = 1
		elif clan in ["Gibbers","gibbers"]:
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			print("Gibbers Clan is led by the mysterious")
			print("Madra, a dark brown mouse trained in")
			print("the way of hand-to-hand combat.")
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			clanLeader = "Madra"
			clanWeapon = "staff"
			clanSymbol = "fox"
			clanCount = 1
		elif clan in ["Birdleaf","birdleaf"]:
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			print("Birdleaf Clan is led by the young and") 
			print("spirited Filo, a grey and white mouse") 
			print("trained in the way of the archer.")
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			clanLeader = "Filo"
			clanWeapon = "bow and arrow"
			clanSymbol = "falcon"
			clanCount = 1
		else:
			print("Sorry, what was that? ")
	
	if age < 19:
		print("Your mother, father, and younger brother Talo are also from " + clan + " Clan.")
	else:
		print("Your partner and son Talo are also from " + clan + " Clan.")
		
	print("Today, Talo is receiving his first weapon from " + clanLeader + ".")
	print("Your family has gathered at the Atta Star, a tall spire in the centre of the City.")
	print("Talo smooths his " + furColour + " fur, the same shade as your own, and looks up at you.")
	
	if age < 19:
		print("Talo: '" + name + ", I'm nervous.'")
	else:
		if gender in ["F","f"]:
			print("Talo: 'Mama, I'm nervous.'")
		elif gender in ["M","m"]:
			print("Talo: 'Papa, I'm nervous.'")
		else:
			print("Talo: 'I'm nervous.'")	
	
	choice0 = str(input("(a) You tell Talo to be strong, (b) You tell Talo that you were nervous once, too. "))
	
	if choice0 in ["a","(a)","A","(a)"]:
		print("Talo puffs out his chest, but you can see him tremble.")
	elif choice0 in ["b","(b)","B","(B)"]:
		print("Talo: 'Really?'")
		print("You: 'Really.'")
		print("You squeeze his little hand and he relaxes.")
	else:
		print("Talo stares and you and tears form in his eyes.")
		
	print(clanLeader + " appears at the top of the steps leading up to the Star.")
	print(clanLeader + ": 'Greetings, brave mice of " + clan + "!'")
	print("Your family stands at respectful attention.  Talo puts on a brave face.")
	print(clanLeader + " smiles. 'Today is the day, is it, young Talo?'")
	print("Talo musters his courage and approaches the leader.")
	print("Kneeling before " + clanLeader + ", Talo speaks the words that you have taught him.")
	
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("Atta guide me through darkest night")
	print(clan + " Clan stay by my side") 
	print("I, young Talo, shall defend us all") 
	print("Lest malicious bidding be our fall.")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")	
	
	print("Pleased, " + clanLeader + " nods, first to him and then to you.")
	print("'I see you have been taught well, Talo.'")
	print(clanLeader + " raises a " + clanWeapon + " to present to Talo, the weapon of " + clan + " Clan.")
	
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("Suddenly, a large spider with fierce,") 
	print("dripping fangs emerges from the other")
	print("side of the spire.")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	
	print(clanLeader + ": *gasping* 'No, it can't be!'")
	choice1 = input("(a) You fling yourself in front of Talo. (b) You grab the " + clanWeapon + " from " + clanLeader + ". ")
	
	print("You: 'Stay back, vermin!'")
	print("The spider laughs in a hissing, sickly manner.")
	print("'Bold little rodent, aren't you? You must not know me.'")
			
	if choice1 in ["a","(a)","A","(A)"]:
		print("")
	elif choice1 in ["b","(b)","B","(B)"]:
		choice1b = input("Do you attack or speak to the spider? (a/s) ")
		if choice1b in ["a","(a)","A","(A)"]:
			print(clanLeader + " cries: 'No, " + name + ", don't!'")
			if clan in ["Skaw","skaw"]:
				print("You slice with the dagger, aiming for one of the spider's eyes.")
				attack0 = str(int(random.randint(3, 10)))
				attack1 = str(int(random.randint(1, 5)))
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				print ("You attack with " + attack0 + " damage")
				print ("The spider attacks with " + attack1 + " damage")
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				
				attack0 = int(attack0)
				attack1 = int(attack1)

				if attack0 < attack1:
					print("The spider shrugs off your blow and sinks its fangs into you.")
					complete = 0
					return complete
			else:
				print("You strike the spider in an eye and it shrieks, recoiling.")
				print("You grab Talo and wave to the others to follow.")
				complete = 1
				return complete
		else:
			choice1bspeak = input("You: (a) 'I know who you are.' (b) 'I do not.'")
			if choice1bspeak in ["a","(a)","A","(A)"]:
				print("Spider: 'Then you know what I'll do!'")
				print("The spider lunges forth.")
				choice1bspeaka = input("You: (a) Brandish the '" + clanWeapon + " and take aim! (b) Dive to the side, taking Talo with you.")
				if choice1bspeaka in ["a","(a)","A","(A)"]:
					attack2 = str(int(random.randint(3, 10)))
					attack3 = str(int(random.randint(1, 5)))
					print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
					print ("You attack with " + attack2 + " damage")
					print ("The spider attacks with " + attack3 + " damage")
					print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				else:
					
			else: 
				print("Spider: *chuckling, gestures to " + clanLeader + "* 'Your great leader does.'")
				print(clanLeader + ": 'Karkrawl.'")
  	
	#else:
		#print("The spider lunges forward and sinks its fangs into you.")
    	#complete = 0
    	#return complete    	
       
complete = game()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Atta will carry on without you, friend")
print("(Thanks to Aiden for debugging help :))")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
