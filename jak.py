prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == prefixes[5] or prefixes[7]:
       print letter + 'u' + suffix
    else:
       print letter + suffix

