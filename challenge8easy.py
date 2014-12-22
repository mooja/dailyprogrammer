

chorus = ["{0} bottles of beer on the wall,",
          "{0} bottles of beer...\n",
          "Take on down, and pass it around, "
          "{1} bottles of bear on the wall"]

def humanized_song_verse(n):
    if n == 1:
        chorus[2:3] = ["1 bottle of beer on the wall 1 bottle of beer",
                       "Take it down and pass it around, no more bottles of beer on the wall"]
    return "\n".join([verse.format(str(n), str(n-1)) for verse in chorus])


for i in range(99, 0, -1):
    print humanized_song_verse(i)
    print 
