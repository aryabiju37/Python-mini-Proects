import pyfiglet
from termcolor import colored


def Ascii_print(text,colors):
	figtext = pyfiglet.figlet_format(text)
	colored_text = colored(figtext,color=colors)
	return colored_text

text = input("What do you want to get printed? ")
colors = input("What color do you want to print? ")
col_text = Ascii_print(text,colors)
print(col_text)


