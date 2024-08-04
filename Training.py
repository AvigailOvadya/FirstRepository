line = raw_input()
while line.startswith('a'):
    print "I don't like a'", line
    line = raw_input()

while True:
    line = raw_input()
    if not line.startswith('a'): break

    print "I don't like a'", line





word_count = 0
line = raw_input()

while len(line) > 0:
    word_count += len(line.split())
    line = raw_input()

print "You typed a total of %d words" % word_count