import glob

# find txt files
parse_files = glob.glob("*.txt")
with open("testglob.txt", "w") as outfile: # create output file named result.txt
    for x in parse_files:
        with open(x, "rb") as infile:
#            outfile.write(x + '\n' + infile.read().decode("utf-8"))
            outfile.write(infile.read().decode("utf-8"))
