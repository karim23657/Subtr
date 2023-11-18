def grouping_json_subtitle(_captions: list) -> list:
    stop_list = (".", "!", "?")
    result = []
    templist = []
    for caption in _captions:
        caption['text'] = str(caption['text']).replace("\n", " ")
        if str(caption['text']).strip().endswith(stop_list):
          templist.append(caption)
          result.append(templist)
          templist = []
        else:
            templist.append(caption)
    return result


def group_strings (g_c_j,limit=5000):
  # initialize an empty list to store the groups
  groups = []
  # initialize an empty list to store the current group
  current_group = []
  # loop through the strings in the list
  for s in g_c_j:
    # if the current group is empty or adding the string does not exceed the limit
    if not current_group or sum (len (x['text']) for x in current_group) + sum (len (y['text']) for y in s) <= limit:
      # append the string to the current group as a list element
      current_group.extend (s)
    else:
      # otherwise, append the current group to the groups list and reset it
      groups.append (current_group)
      current_group = []
      # append the string to the new current group as a list element
      current_group.extend (s)
  # append the last current group to the groups list if it is not empty
  if current_group:
    groups.append (current_group)
  # return the groups list
  return groups

import requests ,json
def translate_text001(
    target: str, text_list: list[str], source: str = "en", separator: str = "u~~~u"
) -> list[str]:
    url = "https://translate.googleapis.com/translate_a/single"
    result = ()
    sl = source
    text = f" ".join(text_list)
    params = {"client": "gtx", "sl": sl, "tl": target, "dt": "t", "q": text}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0"
        "Safari/537.36 Edg/114.0.1823.79"
    }
    r = requests.get(url, params=params, headers=headers)
    # print(r.text)
    try:
        json_result = r.json()
        # print(json.dumps(json_result))
        return json_result
    except Exception:
        ...




import string
def cl_punc(list_2):
  list_1 = list_2[:]
  for i in range(len(list_1)):
    # Remove any punctuation characters from the word using a translation table
    list_1[i] = list_1[i].translate(str.maketrans('', '', string.punctuation)).strip()
  return list_1


def split_list_by_ratio(strings, numbers):
  # calculate the total sum of the numbers
  total = sum(numbers)
  # initialize an empty list to store the sublists
  result = []
  # initialize a variable to keep track of the current index in the strings list
  index = 0     # loop through the numbers list
  for number in numbers:
    # calculate how many strings should be in the current sublist
    count = int(round(len(strings) * number / total))
    # slice the strings list from the current index to the count
    sublist = strings[index:index + count]
    # append the sublist to the result list
    result.append(sublist)
    # update the index by adding the count
    index += count     # return the result list

  if len(strings) != index:
    try :
      result[-1].extend(strings[index:len(strings)])
    except:
      print(result)
      print(index)
  return result


# safe append
def s_a(line_no,list_i,dict_obj):
  if not line_no in dict_obj:
    dict_obj[line_no]=[]
  dict_obj[line_no].extend(list_i)


import collections

def translate_each_group(captions_json,dest_lang='fa', src_lang="en"):
  q = (c['text'] for c in captions_json)
  tr_json = translate_text001(dest_lang,q,src_lang)
  w = [c['text'] for c in captions_json]
  ccaps = w[:]
  en_texts_v1 = []
  for id,i in enumerate(ccaps):
    e = cl_punc(i.split())
    for j in e:
      if j:
        en_texts_v1.append([j,id])

  all_da1={}
  w1_1 = en_texts_v1.copy()
  tr_en_texts = []
  h_history = ''
  for id,i in enumerate(tr_json[0]):
    e = cl_punc(i[1].split())
    f = []
    for j in e:
      if j:
        if j == w1_1[0][0]:
          x = w1_1.pop(0)
          f.append(x[1])
        else:
          if h_history :
            if h_history+j == w1_1[0][0]:
              x = w1_1.pop(0)
              f.append(x[1])
          h_history = j
          print('|> no match:',j , w1_1[0][0],id)
          print('|> next:', w1_1[1][0], w1_1[2][0],id)
          print('|> next:',e,id)
          r=0
      else:
        print('|> nothing:',j , w1_1[0][0],id)
        r=0
    tr_en_texts.append( collections.Counter(f))

  transl_align_1 ={}
  for id,i in enumerate(tr_en_texts):
    numbers = [i[v] for v in i.keys()]
    sent =tr_json[0][id][0]
    spl_snt =cl_punc(sent.split())
    strings = [x for x in spl_snt if x]
    groupped = split_list_by_ratio(strings,numbers)
    for iid,j in enumerate(i.keys()):
      s_a(j,groupped[iid],transl_align_1)

  g = captions_json[:]
  for id,i in enumerate(g):
    i['text']=' '.join(transl_align_1[id])

  return g



import pysrt

def srt_to_caption_list(srt_file_path):
    captions = pysrt.open(srt_file_path, encoding='utf-8')

    caption_list = []
    for caption in captions:
        caption_info = {
            'start': str(caption.start),
            'end': str(caption.end),
            'text': caption.text,
        }
        caption_list.append(caption_info)

    return caption_list




def captions_json_translator(_captions_json,dest_lang="fa", src_lang="en"):
  ee_j = _captions_json[:]
  c_j = grouping_json_subtitle(ee_j)
  gc_j = group_strings(c_j,10000)
  outp=[]
  for id,cc in enumerate(gc_j):
    print('|> :',id)
    cc1 = cc[:]
    outp.extend(translate_each_group(cc1,dest_lang, src_lang))
  return outp



class SubTr:
    def __init__(self):
        self.cpj = []

    def srt(self,srt_path):
        self.cpj = srt_to_caption_list(srt_path)
        
    def dfpx(self,dfpx_path):
        from dfpx_parser import parse_xml_to_srt2
        with open(dfpx_path,'r', encoding='utf-8') as f:
            xml_text = f.read()
        captions_141 = parse_xml_to_srt2(xml_text)
        self.cpj = captions_141[:]
    def translate(self,dest_lang="fa" , src_lang="en",save_path=None):
        result = captions_json_translator(self.cpj,dest_lang, src_lang)
        self.cpj = []
        if save_path:
            file = pysrt.SubRipFile()
            for id,sub_t in enumerate(result):
                sub = pysrt.SubRipItem(id+1, start=sub_t['start'], end=sub_t['end'], text=sub_t['text'])
                file.append(sub)
            file.save(save_path, encoding='utf-8')
        else:
            return result
        


