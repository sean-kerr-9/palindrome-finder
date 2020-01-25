
def findPalindrome(word):
  for idx, val in enumerate(word):
    if(word[idx] == word[len(word)-(1+idx)]):
      continue
    else:
      return print(word+ " is not a palindrome")
  return print(word + " is a palindrome")


if __name__ == "__main__":
    words = ["couch", "dad", "lily", "iowa", "lamp", "hannah", "racecar"]
    for word in words:
      findPalindrome(word)