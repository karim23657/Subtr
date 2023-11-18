from bs4 import BeautifulSoup
import html
import re
def convert_timestamp(timestamp):
    # split the timestamp by the dot
    parts = timestamp.split(".")
    # check if the second part has two digits
    if len(parts[1]) == 2:
        # add a zero at the end
        parts[1] += "0"
    # join the parts back with the dot
    return ",".join(parts)

def parse_xml_to_srt2(xml_text):
    root = BeautifulSoup(xml_text, 'html.parser')
    subtitles = []

    for p in root.find_all("p"):
        begin = convert_timestamp(p.get('begin'))
        end = convert_timestamp(p.get('end'))
        text =  re.sub(r'\s+', ' ', p.text.replace('\n', ' ')).strip()

        # Omit empty tracks
        if text:
            # Convert HTML entities to characters
            text = html.unescape(text)
            subtitles.append({"start": begin, "end": end, "text": text})

    return subtitles
