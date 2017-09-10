text="""wo
shi
shui"""
text1='''wo
shi
shui'''

with open('requirement.txt') as f:
    text2=reduce(lambda x,y:x+y, f.readlines())


z=['1\n','2\n','3\n','4\n','5\n','6\n']
text3=reduce(lambda x,y:x+y, z)
print(text3)