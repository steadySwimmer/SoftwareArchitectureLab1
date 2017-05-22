''' Constants for keys from parser dictionary result '''
save_type_key = 'save_type'

def config_parser_result():
	result = {}
	delimiter = "="
	comment_delimiter = "#"
	with open("configuration/config", "r") as fl:
		for line in fl:
			''' Skip of line that was commented '''
			if (line[0] != comment_delimiter):
				separate_list = line.split(delimiter)
				result[separate_list[0]] = separate_list[1]

	''' If config is empty it full fils result of parser with default values '''
	if (bool(result) == False):
		result = {save_type_key: 'pickle'}

	return result
