#!/usr/bin/ruby

# Daily Programmer Challenge 164 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/26ijiu/5262014_challenge_164_easy_assemble_this_scheme/


puts 'hello world'

count = (1..100).each do |x|
    if (x % 3 == 0) and (x % 5 == 0)
        print x, ' '
    end
end

print "\n"

def is_anagram(word1, word2)
    return (word1.chars.sort.join == word2.chars.sort.join)
end

if is_anagram('abc', 'cab')
    puts 'is anagram!'
end
