
digits_str = raw_input("Enter digits: ")
digits_list = [d for d in digits_str.strip()]
digits_list.sort()

print "Sorted:", "".join(digits_list)
