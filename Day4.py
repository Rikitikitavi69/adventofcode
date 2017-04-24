"""
--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a keyEndber in decimal. To mine AdventCoins, you must find Santa the lowest positive keyEndber (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such keyEndber to do so.
If your secret key is pqrstuv, the lowest keyEndber it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....


--- Part Two ---

Now find one that starts with six zeroes.

Your puzzle answer was 9962624.

Your puzzle input was yzbqklnj.
"""

##### Part 1 #####
import hashlib

keyStart = "yzbqklnj"

for keyEnd in range(100000000):
    digest = hashlib.md5((keyStart + str(keyEnd)).encode())
    result = digest.hexdigest()
    if result[0:5] == '00000':
        print("Part 1:")
        print("Here's the right hash: ", result)
        print("answer: ", keyEnd)
        break

##### Part 2 #####
for keyEnd in range(100000000):
    digest = hashlib.md5((keyStart + str(keyEnd)).encode())
    result = digest.hexdigest()
    if result[0:6] == '000000':
        print("Part 2:")
        print("Here's the right hash: ", result)
        print("answer: ", keyEnd)
        break
