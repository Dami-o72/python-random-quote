<<<<<<< HEAD
import random

def main():
   #print("Keep it logically awesome.")
=======
def primary():
   print("Keep it logically awesome.")
>>>>>>> 675203637baa7cb3a22baf4c37eade92e52a52a3

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
    primary()

