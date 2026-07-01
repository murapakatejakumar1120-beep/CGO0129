Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="vijayawada"
a[1]
'i'
a[4]
'y'
a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]
'ijayawada'
a=" i am in class"
a[2]+a[3]
' a'
a[3]+a[4]
'am'
a[9]
'c'
>>> a[9]+a[10]+a[11]+a[12]+a[13]
'class'
>>> a="simple is better than complex"
>>> a[10]
'b'
>>> a[10]+a[11]+a[12]+a[13]+a[14]+a[15]
'better'
>>> a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]
'complex'
>>> a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'simple'
>>> a="codegnan it solutions"
>>> a[12]+a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'solution'
>>> a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]
'codegnan'
>>> a[9]+a[10]
'it'
>>> a="i am learning python"
>>> a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
>>> a[-15]+a[-14]+a[-13]+a[-12]+a[-11]+a[-10]+a[-9]+a[-8]
'learning'
>>> a[-15]+a[-14]+a[-13]+a[-12]+a[-11]
'learn'
>>> a[-17]+a[-18]
'ma'
>>> a[-18]+a[-17]
'am'
>>> a[-19]+a[-18]+a[-17]
' am'
>>> a="python fullstack"
>>> a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'stack'
>>> a[-9]+a[-8]+a[-7]+a[-6]
'full'
>>> a[-16]+a[-15]+a[-14]+a[-13]+a[-12]+a[-11]
'python'
