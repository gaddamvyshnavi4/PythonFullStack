Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
##indexing
a='vijayawada'
a[0]
'v'
a[-1]
'a'
a[0]+a[1]+a[2]+a[3]+a[4]
'vijay'
a[-10]
'v'
a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'vijay'
#slicing
a='bejayawada is a royal city'
a[22:26]
'city'
a[0:10]
'bejayawada'
a[16:21]
'royal'
a[11:13]
'is'
a='machine learnign'
a[3:]
'hine learnign'
a[-3:]
'ign'
a[:-7]
'machine l'
#important





#striding
a='data science'
a[::]
'data science'
a[::1]
'data science'
a[::-1]
'ecneics atad'
a='cloud computing'
a[::6]
'cci'
a[::3]
'cucpi'
a[5::9]
' g'
a[::6]
'cci'
a[:6]
'cloud '
a[2:8]
'oud co'
a'hello python'
SyntaxError: invalid syntax
a='hello python'
a[-1:-6:-2]
'nhy'
a[-2:-9:-4]
'op'
a[-3:-9:-2]
'hy '
a[-4:-12:-5]
'tl'
##string methods
='vyshnavi"
SyntaxError: unterminated string literal (detected at line 1)
a="vyshnavi"
len(a)
8
len("    ")
4
len("")
0
#count
a='twinke twinkle little star'
a.count("twinkle')
        
SyntaxError: unterminated string literal (detected at line 1)
a.count("twinkle")
        
1
a.count('t')
        
5
a.count('')
        
27
# above code returns len+1
        
a.count('T')
        
0
#find a string
        
a="code"
        
a,find('e')
        
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a,find('e')
NameError: name 'find' is not defined
a.find('e')
        
3
a='codee'
        
a.find('e')
        
3
#only returns first ocuurance
        
a.find("T")
        
-1
#here it returns -1
        
#escape seuence
        
''' \n new line
    \b back space
    \t tab space
    '''
        
' \n new line\n    \x08 back space\n    \t tab space\n    '
a='vyshnavii \n \t how are you'
        
a
        
'vyshnavii \n \t how are you'
print(a)
        
vyshnavii 
 	 how are you
#############
        
a.replace('v','y')
        
'yyshnayii \n \t how are you'
#upper
        
a="sigma"
        
a.upper()
        
'SIGMA'
a.lower()
        
'sigma'
a='sigma upper lower'
        
a.capitalize()
        
'Sigma upper lower'
a.title()
        
'Sigma Upper Lower'
a.islower()
        
True
a.isupper()
        
False
a.isalpha()
        
False
#here space is not alphabet
        
a.isdigit()
        
False
a.startswith('y')
        
False
a.endswith('r')
        
True
a.split()
        
['sigma', 'upper', 'lower']
#default space
        
a.split('a')
        
['sigm', ' upper lower']
#join()
        
a.join()
        
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a.join()
TypeError: str.join() takes exactly one argument (0 given)
a.join(" ")
        
' '
    a
        
SyntaxError: unexpected indent
a
        
'sigma upper lower'
" ".join(a)
        
's i g m a   u p p e r   l o w e r'
a=1,2,3
        
a
        
(1, 2, 3)
' '.joina()
        
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    ' '.joina()
AttributeError: 'str' object has no attribute 'joina'. Did you mean: 'join'?
' '.join(a)
        
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    ' '.join(a)
TypeError: sequence item 0: expected str instance, int found
#join is only for str
        
a='1','2','3'
        
' '.join(a)
        
'1 2 3'
'_'.join(a)
        
'1_2_3'
'b'.join('ok)
         
SyntaxError: unterminated string literal (detected at line 1)
'b'.join('ok')
         
'obk'
#strip
         
a="     jbjkhbkj      "
         
a.strip()
         
'jbjkhbkj'
a.lstrp()
         
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    a.lstrp()
AttributeError: 'str' object has no attribute 'lstrp'. Did you mean: 'lstrip'?
a.lstrip()
         
'jbjkhbkj      '
a.rstrip()
         
'     jbjkhbkj'
a="     jbjkhbkj      $#^"
         
a.strip()
         
'jbjkhbkj      $#^'
a="     jbjkhbk ---"
         
a.strip()
         
'jbjkhbk ---'
#formatting
         
a=9;b=7
         
a=9;b=7;
         
print("hi {}  {}",format(a,b))
         
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    print("hi {}  {}",format(a,b))
TypeError: format() argument 2 must be str, not int
>>> print("hi {}  {}".format(a,b))
...          
hi 9  7
>>> print("hi {}  {}".format(10,90))
...          
hi 10  90
>>> a='k'
...          
>>> b='kjh'
...          
>>> print("njkjk",a+b)
...          
njkjk kkjh
>>> print(a,b)
...          
k kjh
>>> #concatination
...          
>>> a+b
...          
'kkjh'
>>> print(f"jashbm {a}  {b}")
...          
jashbm k  kjh
>>> a=f"jashbm {a}  {b}"
...          
>>> print(f"a)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print(f"a")
...       
a
>>> print(a)
...       
jashbm k  kjh
