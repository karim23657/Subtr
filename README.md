# Subtr
Effortless Subtitle Translation is a user-friendly tool that seamlessly translates SRT and DFXP subtitles.

It's the ideal choice for handling subtitle sentence breaks across tracks, ensuring smooth and accurate translations.

for exp. :
```
8
00:01:10,374 --> 00:01:12,576
Adam is paying

9
00:01:12,776 --> 00:01:15,655
attention to the teacher.
```

We translate  ✅:
```
8
00:01:10,374 --> 00:01:12,576
آدم حواسش به

9
00:01:12,776 --> 00:01:15,655
معلم است.
```


But others ❌:
```
8
00:01:10,374 --> 00:01:12,576
آدام پرداخت می کند

9
00:01:12,776 --> 00:01:15,655
توجه به معلم
```

# How to use

put `subtr.py` next to your code , then :
```python
from subtr import SubTr

translator = SubTr()
translator.srt('Avengers Infinity War 2018.srt')
translator.translate(dest_lang="fa" , src_lang="en",save_path='Avengers Infinity War 2018-fa.srt')
```

or dfpx :
```python
from subtr import SubTr

translator = SubTr()
translator.dfpx('67_000_Dreams_.html')
translator.translate(dest_lang="fa" , src_lang="en",save_path='67_000_Dreams_fa.srt')
```
