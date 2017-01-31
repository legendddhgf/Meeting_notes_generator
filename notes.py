#!/usr/bin/python3

import sys
from time import gmtime, strftime

speakers = []

def wrap_statements(speakerstr1, speakerstr2, buf): # assumes correctly format
  returnstr = ""
  bufptr = 0
  curline = 1
  returnstr += '-' * 100 + '\n'
  while(False and bufptr < len(buf)):


    ## TODO:CONTINUE
    count = 0
    while (True): # get the size of the line into count variable
      if (buf[bufptr + count] == '\n'):
        break
    # loop for putting the characters, shouldn't leave till it just jumped over
    # a newline
    if (buf[bufptr] == '\n'): # warning, assumes unix style endings
      returnstr += " |"
  return returnstr

def print_speakers():
    print('List of speakers:')
    for i in range(0, len(speakers)):
        print(str(i + 1) + ": " + speakers[i])
    print('\n')

if (len(sys.argv) < 2 or len(sys.argv) > 3):
    raise SystemExit("Usage: ./notes.py [config file] <Output File>")

config = None

if (len(sys.argv) == 2):
    try:
        config = open('notes.cfg', 'r')
    except FileNotFoundError:
        raise SystemExit("notes.cfg: File doesn't exist")

elif (len(sys.argv) == 3):
    try:
        config = open(sys.argv[1], 'r')
    except FileNotFoundError:
        raise SystemExit("notes.cfg: File doesn't exist")

for line in config:
    for token in line.split():
        speakers.append(token)

config.close()

print("Config loaded the following people:")
print_speakers()

out = None
try:
    check = open(sys.argv[len(sys.argv) - 1], 'r')
except FileNotFoundError:
    print("Successfully opened new file for writing: " +
            sys.argv[len(sys.argv) - 1])
else:
    over_write = input("Append to file " +
            sys.argv[len(sys.argv) - 1] + "? [!y]: ")
    if (over_write != 'y' and over_write != 'Y'):
        raise SystemExit("Exiting program")

out = open(sys.argv[len(sys.argv) - 1], 'a')

out.write("\n")

while(True):
    cmd = input("Enter a command ('h' for help): ")
    if (cmd == 'h'):
        print('h: list commands and their functions')
        print('n: new note')
        print('e: exit and write to output file')
    elif (cmd == 'n'):
        print_speakers()
        speaker = None
        try:
            speaker = int(input("Enter a speaker: "))
        except ValueError:
            print(str(speaker) + ": not a valid speaker index")
            continue
        if (speaker < 1 or speaker > len(speakers)):
            print(str(speaker) + ": not a valid speaker index")
            continue

        print("Successfully chosen speaker: " + speakers[speaker - 1])

        print("Note will be saved upon entering of blank line")

        buf = ""; # buffer for the group of notes
        while(True):
            
            line = input(sys.argv[len(sys.argv) - 1] + " > ")
            
            if (len(line) < 1):
              speakerstr1 = "| " + speakers[speaker - 1]
              speakerstr2 = "| " + strftime(" %Y-%m-%d :: %H:%M:%S")
              while (len(speakerstr1) > len(speakerstr2)):
                speakerstr2 += ' ' # make str2 atleast size of str1
              while (len(speakerstr1) < len(speakerstr2)):
                speakerstr1 += ' ' # make str1 atleast size of str2
              speakerstr1 += " | "
              speakerstr2 += " | "
              out.write(wrap_statements(speakerstr1, speakerstr2, buf))
              buf = "" # clear buffer
              break

            buf += line + '\n' # if the line exists
    elif (cmd == 'e'):
        out.close()
        raise SystemExit(sys.argv[len(sys.argv) - 1] + ": written")
    else:
        print(cmd + ": invalid command")
