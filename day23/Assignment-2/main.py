path="story.txt"

def count_hate_t(path_file):
    with open(path_file, "r") as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            if line[0] != "T":
                count += 1
        print(count)

count_hate_t(path)

#-----------------------------------------------------------------------------------------------------------------------
path="just_text.txt"

def count_love_e(path_file):
    with open(path_file, "r") as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            words = line.split()
            for word in words:
                if word.strip(",.?!")[-1] == "e":
                    count += 1

        return count

print(count_love_e(path))

#-----------------------------------------------------------------------------------------------------------------------
path="WORDS.TXT"

def JTOI(path_file):
    with open(path_file, "r") as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            words = line.split()
            for word in words:
                if "J" in word:
                    word = word.replace("J", "I")
                print(word, end=" ")

JTOI(path)












