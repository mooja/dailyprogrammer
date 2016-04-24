
# Daily Programmer Challenge 186 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2kh2tz/10272014_challenge_186_easy_admin_schmadmin/
#
# 24.April.2016


# * Get the 20 last used documents from the system and sort by the date they
#   were modified.
## $ ls -t | head -n 10

# * Output the above command to a .txt file.
## $ $(ls -t | head -n 10) > recentfiles.txt

# * Retrieve the last 10 commands used on the console.
## $ history | tail -n 11 | head -n 10

# *  Get the 10 most CPU-heavy processes in descending order.
## $ ps -e -o %cpu,%mem,comm --sort=-%cpu | head -n 10

# * Retrieve the last 20 error logs/messages and output these as a formatted HTML table
## $ echo "<table>"
## $ for line in $(dmesg | tail -n 20);
## $ do
## $     echo "<tr><td> $line </td></tr>"
## $ done
## $ echo "</table>"


# * Retrieve all txt/pdf/exe files on the machine (You do not need to do the
#   whole machine, just 1 drive is enough, or less if your machine is
#   struggling).
## $ find . -name '*.txt -o -name '*.pdf' -o -name '*.exe'
