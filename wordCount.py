import operator
import socket
import os

def getWordCount(fileName) :
    Myfile = open(fileName, "r")
    alphanumeric = ""

    for x in Myfile:
        a_string = x
        for character in a_string:
            if (character.isalnum()) or (character in [" ", "'", "-","_"]):
                alphanumeric += character
            else:
                alphanumeric += " "
        alphanumeric += " "

    text = alphanumeric

    text = text.strip()
    text = text.lower()
    words = text.split(" ")

    d = dict()
    wordCount = 0
    
    # print("text : ", text)

    for word in words:
        if word == "" :
            continue
        elif word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
        wordCount += 1

    return (d, wordCount)

def getTop3Counts(d) :
    # sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_d[:3]

def listToStr(top3Words) :
    answer = ""
    for word in top3Words :
        answer += "\t" + word[0] + " - " + str(word[1]) + "\n"
    return answer

def read_text_file(file_path):
	text_file = open(file_path, 'r')
	print(text_file.read())

def main() :
    parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    # print("parent_path : ", parent_path)
    totalWordCount = 0
    result, wordCountString, top3String = "Text files at location: /home/data are : \n", "", ""
    # print(os.listdir(parent_path + "/data"))
    for file in os.listdir(parent_path + "/data"):
        if file.endswith(".txt"):
            # read_text_file(file)
            result += "\t" + file + "\n"
            d, wordCount = getWordCount(parent_path + "/data/" + file)
            totalWordCount += wordCount
            wordCountString += "Word Count in " + file + " : " + str(wordCount) + "\n"
            if file == "IF.txt":
                top3Words = getTop3Counts(d)
                top3String = "Top 3 Words in IF.txt : \n" + listToStr(top3Words)
    result += "\n" + wordCountString
    result += "Total Word Count : " + str(totalWordCount) + "\n"
    result += "\n" + top3String

    host_name = socket.gethostname()
    IP_addres = socket.gethostbyname(host_name)
    # result += "Host Name is : " + host_name + "\n"
    result += "\nComputer IP Address is : " + IP_addres

    print(result)
    text_file = open(parent_path + '/output/result.txt', 'w')
    text_file.write(result)
    text_file.close()

main()
# fileName1 = str(input("Please enter First File Name : "))
# fileName2 = str(input("Please enter Second File Name : "))
# fileName1 = "IF.txt"
# fileName2 = "Limerick-1.txt"
# d1, wordCount_1 = getWordCount(fileName1) 
# d2, wordCount_2 = getWordCount(fileName2)

# print("Word Count in IF.txt : " + str(wordCount_1))
# print("Word Count in Limerick-1.txt : " + str(wordCount_2))
# print("Total Word Count : " + str(totalWordCount))

# top3Words = getTop3Counts(d1)
# result += "Top 3 Words : \n" + listToStr(top3Words)
# print("Top 3 Words : \n" + listToStr(top3Words))

# print("Host Name is : " + host_name)
# print("Computer IP Address is : " + IP_addres)