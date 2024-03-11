text = "X-DSPAM-Confidence:    0.8475"
text1=text.replace(" ","")
position=text1.find(":")
print(float(text1[position+1:]))