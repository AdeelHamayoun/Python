str = 'X-DSPAM-Confidence: 0.8475 '

fpost = str.find(':')
lpost = len(str)
sub_string = str[fpost+1:lpost]
fval = float(sub_string.strip())
print(fval)
