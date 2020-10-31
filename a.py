from collections import Counter

# def calculate_frequencies(file_contents):
#     # Here is a list of punctuations and uninteresting words you can use to process your text
#     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#     uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
#     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
#     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
#     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
#     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
#     # LEARNER CODE START HERE
#     frequencies={}
#     file=""
#     exp=file_contents.lower().split(" ")
#     for word in exp:
#         if word not in uninteresting_words :
#             file+=word+" "
#     f=file.split(" ")
#     text={val for val in f if val.isalpha()}
#     for letter in text:
#         if letter in frequencies.keys():
#             frequencies[letter]+=1
#         else :
#             frequencies[letter]=1
#     #print(frequencies)
#     return frequencies
file_contents="same same fuck u same"
#print(calculate_frequencies(file_contents))


#y = calculate_frequencies(file_contents)
y =Counter(file_contents.split())
print(y)

    