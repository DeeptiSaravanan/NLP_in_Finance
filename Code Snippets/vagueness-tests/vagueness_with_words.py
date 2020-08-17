import PyPDF2

# creating an object 
file = open('../Papers&Docs/Regulations/Insider Trading.pdf', 'rb')
terms = open('vague_terms', 'r')
words = open('vague_WORDS.txt','r')

v_terms = terms.readlines()

vague_terms = []
for k in v_terms:
	vague_terms.append(k.strip())

# print(vague_terms)

# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file, strict = False)

pages = fileReader.numPages

for i in range(8,pages-1):
		# Creating a page object
		pageObj = fileReader.getPage(i)
		# Printing Page Number
		print("Page No: ",i)
		# Extracting text from page
		# And splitting it into chunks of lines
		text = pageObj.extractText().split('\n')
		# Finally the lines are stored into list
		# For iterating over list a loop is used
		for i in range(len(text)):
			for k in vague_terms:
				if k in text[i].split(): 
					print(text[i])
					print(k)
					print('-----------------------------------------------------------------------------------------------------------------')
		print('**********************************************************')			
		# For Seprating the Pages
		# print()
# closing the pdf file object
# pdfFileObj.close()