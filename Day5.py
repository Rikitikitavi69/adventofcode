"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?

--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?
"""

import re
lst = []
with open("5.txt", "r", 1) as f:
    for line in f:
        lst.append(line[:-1]) if line[-1] == "\n" else lst.append(line)

regex1 = re.compile(r"[aeiou]")
regex2 = re.compile(r"(.)\1")
regex3 = re.compile(r"(ab|cd|pq|xy)")

niceStrings = []

for line in lst:

	forbid = re.search(regex3, line)
	if forbid != None:
		continue

	vowels = re.findall(regex1, line)
	if vowels != None:
		if len(vowels) < 3:
			continue

	double = re.search(regex2, line)
	if double == None:
		continue

	niceStrings.append(line)

print("Part 1 answer: ", len(niceStrings))

########## PART 2 ##########
regex1_2 = re.compile(r"([a-z]{2,}).*\1")
regex2_2 = re.compile(r"(\w).\1")

niceStrings2 = []

for line in lst:
    twoletters = re.search(regex1_2, line)
    if twoletters == None:
        continue

    repeatletter = re.search(regex2_2, line)
    if repeatletter == None:
        continue

    niceStrings2.append(line)

print("Part 2 answer:", len(niceStrings2))
