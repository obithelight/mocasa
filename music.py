import time
import random

myChoice = ["unique taste", "lofty sense", "fly posture", "robust appreciation", "good exposure"]
randomChoice = random.choice(myChoice)

def musicApp():
  print("Experience Mocasa. Experience Premium Music.\n")
  time.sleep(1)

  while True:
    username = input("What should we call you? ").title()

    # remove extra/unwanted spaces if mistakenly entered by user
    username = ' '.join(username.split())

    if username:
      break
    else:
      print("\nEmpty input. Please enter your name.\n")
      time.sleep(1)

  print(f"\nHello, {username}. Tell us a bit about yourself.\n")
  time.sleep(1)

  while True:
    genre = input("1.  What's your favorite music genre? ").title()

    # remove extra/unwanted spaces if mistakenly entered by user
    genre = ' '.join(genre.split())

    if genre:
      break
    else:
      print("\nEmpty input. Please tell us your preferred genre.\n")
      time.sleep(1)

  print(f"\nSeems you've got your grooves on, {username}. More than {random.randint(10, 50)} million of our subscribers vibe to {genre}.\n")
  time.sleep(2)

  while True:
    artiste = input(f"2.  Who's your favorite {genre} musical artist? ").title()

    # remove extra/unwanted spaces if mistakenly entered by user
    artiste = ' '.join(artiste.split())

    if artiste:
      break
    else:
      print("\nEmpty input. Please enter the stage name of your favorite artiste.\n")
      time.sleep(1)

  print(f"\nAwesome! {artiste} is a well celebrated icon in {genre}.\n")
  time.sleep(1)

  print(f"Now let's see how well you know {artiste}.\n")
  time.sleep(1)

  print(f"This will be fun, {username}. There are no wrong answers.\n")
  time.sleep(1)

  while True:
    fullname = input(f"3.  What's {artiste}'s full name? ").title()

    # remove extra/unwanted spaces if mistakenly entered by user
    fullname = ' '.join(fullname.split())

    if fullname:
      break
    else:
      print("\nEmpty input. Please enter the full name of artiste.\n")
      time.sleep(1)

  print(f"\nHehehe, you're slowly but surely proving to be a great fan of {artiste}.\n")
  time.sleep(1)

  while True:
    nickname = input(f"4.  What's {artiste}'s nick name? ").title()

    # remove extra/unwanted spaces if mistakenly entered by user
    nickname = ' '.join(nickname.split())

    if nickname:
      break
    else:
      print("\nEmpty input. Please enter the nickname of artiste.\n")
      time.sleep(1)

  print(f"\nNo jokes, you're doing well. I'm sure {artiste} would be proud.\n")
  time.sleep(1)

  while True:
    country = input(f"5.  What nationality is {artiste}? ").title()

    # remove extra/unwanted spaces if mistakenly entered by user
    country = ' '.join(country.split())

    if country:
      break
    else:
      print("\nEmpty input. Please enter the nationality of artiste.\n")
      time.sleep(1)

  print(f"\nInteresting. It's already telling how much you admire {artiste}.\n")
  time.sleep(1)

  while True:
    try:
      age = int(input(f"6.  How old do you think {artiste} is? ").strip())
      break

    except ValueError:
      print("\nPlease enter a valid number for age.\n")
      time.sleep(1)

  print(f"\nAwesome. Now let's build you a playlist, {username}.\n")
  time.sleep(1)

  # playlist function call
  playList(username, genre, artiste, fullname, nickname, country, age)

def playList(username, genre, artiste, fullname, nickname, country, age):
  while True:
    try:
      myplaylist = int(input("7.  How many albums/tracks do you want to be in your playlist? "))

      tracklist = []
      break

    except ValueError:
      print("\nPlease enter a valid number for playlist size.\n")

  # add user favorite tracks into tracklist
  for song in range(myplaylist):
    while True:
      track = input("\nEnter album/track name: ").title()

      # remove extra/unwanted spaces if mistakenly entered by user
      track = ' '.join(track.split())

      if track:
        tracklist.append(track)
        break
      else:
        print("Please enter a valid non-empty track name.")

  print(f"\nWow, your {randomChoice} of music is amazing. You've been ranked in the top {random.randint(3, 10)} of our dopest subscribers.\n")
  time.sleep(1)

  print(f"You rock, {username}. Your playlist is ready!\n")
  time.sleep(4)

  # displaylist function call
  displayList(username, genre, artiste, fullname, nickname, country, age, tracklist)

def displayList(username, genre, artiste, fullname, nickname, country, age, tracklist):

  capitalizeUser = username.upper()
  capitalizeArtiste = artiste.upper()

  print(f"\t\tWELCOME TO {capitalizeUser}'S MUSIC LIBRARY.\n")
  time.sleep(1)

  # display user information
  userInfo = {
    "A.  Your favorite genre": genre,
    "B.  Your favorite artiste": artiste,
    "C.  Favorite artiste's full name": fullname,
    "D.  Favorite artiste's nick name": nickname,
    f"E.  How old is {artiste}?": age,
    f"F.  What nationality is {artiste}?": country
  }

  for infoTitle, infoValue in userInfo.items():
    print(f"{infoTitle}: {infoValue}\n")
    time.sleep(2)

  print(f"\t\tYOUR FAVORITE ALBUMS/TRACKS FROM {capitalizeArtiste} ARE: \n")
  time.sleep(1)

  for index, track in enumerate(tracklist, start=1):
    print(f"{index}. {track}\n")
    time.sleep(1)

musicApp()
