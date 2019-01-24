intent = {"technology":None,"article_type":None,"sector":None}
 
def get_technology():
	if intent["technology"] not False:
		if intent["article_type"] and intent["article_type"] not False and intent["sector"] and intent["sector"] not False:
			print("Are you looking for a {} in {} on any specific technology?".format(intent["article_type"],intent["sector"]))
			response = input()

		elif intent["article_type"] and intent["article_type"] not False:
			print("Are you looking for a {} on any specific technology?".format(intent["article_type"]))
			response = input()

		elif intent["sector"] and intent["sector"] not False:
			print("Are you looking for something in {} for any specific technology?".format(intent["sector"]))
			response = input()
		else:
			print("Are you looking for something in any specific technology?")
			response = input()
		if affirmation(response):
			discover_entities(response)
		elif negative(response):
			pass
		else:
			print("Sorry I do not understand.")

	else:
		pass


def get_sector():
	if intent["sector"] not False:
		if intent["article_type"] and intent["article_type"] not False and intent["technology"] and intent["technology"] not False:
			print("Are you looking for a {} in {} on any specific sector?".format(intent["article_type"],intent["technology"]))
			response = input()

		elif intent["article_type"] and intent["article_type"] not False:
			print("Are you looking for a {} in any specific sector?".format(intent["article_type"]))
			response = input()

		else:
			print("Are you looking for some particular sector?")
			response = input()
		if affirmation(response):
			discover_entities(response)
		elif negative(response):
			pass
		else:
			print("Sorry I do not understand.")

	else:
		pass



def get_article_type():
	if intent["get_article_type"] not False:
		if intent["technology"] and intent["technology"] not False and intent["sector"] and intent["sector"] not False:
			print("Are you looking for something on {} in {}?".format(intent["technology"],intent["sector"]))
			response = input()

		elif intent["technology"] and intent["technology"] not False:
			print("Are you looking for a something on any {}?".format(intent["technology"]))
			response = input()

		elif intent["sector"] and intent["sector"] not False:
			print("Are you looking for something in {} for any specific technology?".format(intent["sector"]))
			response = input()
		if affirmation(response):
			discover_entities(response)
		elif negative(response):
			pass
		else:
			print("Sorry I do not understand.")

	else:
		pass

def get_article_type():
	if intent["article_type"] not False:
		print("Do you need any particular video or document related to {}".format(intent["technology"]))

def get_sector():
	if intent["sector"] not False:
		print("Do you need any {} related to {} for any particular Sector like finance/health care/manufacturing etc?".format(intent["article_type"],intent["technology"]))


def dialogue_manager(utterance):
	'''
	Get the utterance, 
	discover the intent
	develop the intent
	search the link
	'''
	discover_entities(utterance)
	if intent["technology"] is None:
		utterance = input()
		if affirmation(utterance):
			get_links()
		elif negative(utterance):
	elif intent["article_type"] is None:
		utterance = input()
	elif intent["Sector"] is None:
		utterance = input()