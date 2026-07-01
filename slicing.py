Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#slicing
a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a="time is very precious"
a[8:12]
'very'
a[:4]
'time'
a[13:21]
'precious'
a[13:]
'precious'
>>> a="work until you succeed"
>>> a[16:]
'ucceed'
>>> a[15:]
'succeed'
>>> a[6:11]
'ntil '
>>> a[5:11]
'until '
>>> a[:5]
'work '
>>> a[12:15]
'ou '
>>> a[11:15]
'you '
>>> a="vizag is city of destiny"
>>> a[-7:-1]
'destin'
>>> a[-7:]
'destiny'
>>> a[-15:-11]
'city'
>>> a[:20]
'vizag is city of des'
>>> a[:-20]
'viza'
>>> a[:-19]
'vizag'
>>> a="hi hello how are you"
>>> a[-17:-12]
'hello'
>>> a[-11:-8]
'how'
>>> a[-7:-4]
'are'
>>> a[-3:]
'you'
>>> a[:-18]
'hi'
