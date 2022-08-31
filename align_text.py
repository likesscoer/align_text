from urllib.request import urlopen
import re, textwrap, random

line_limit = 40
random_paragraphs = False


def remove_html(source):
	match_html = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
	clean_tags = re.sub(match_html, '', source)
	return clean_tags


def clean_text(text):
	f = open('nuevo text.txt', 'w')
	f.write(text)
	f.close()
	f = open('nuevo text.txt', 'r')
	read = f.read()

	clean_nr = re.sub(r'\\r\\n|\\', ' ',read)
	replace_long_space = re.sub("    |b'", '\n\n', clean_nr)
	strip = replace_long_space.strip()
	return strip


def align_text(text, line_limit, is_random):
	paragraphs = text.split('\n\n')
	paragraphs.remove(" '")

	if is_random:
		random.shuffle(paragraphs)

	wrapper = textwrap.TextWrapper(width=line_limit,break_long_words=False,replace_whitespace=True)
	wrapped = [wrapper.fill(paragraph.strip()) for paragraph in paragraphs]
	result = '\n\n'.join(wrapped)
	return result



html = urlopen("https://likesscoer.github.io").read()
text = remove_html(str(html))
text_cleaned = clean_text(text)
text_aligned = align_text(text_cleaned, line_limit, random_paragraphs)



if not random_paragraphs:
	f = open('align{}.txt'.format(line_limit), 'w')
	f.write(text_aligned)
	f.close()

if random_paragraphs:
	f = open('randomshuffle.txt', 'w')
	f.write(text_aligned)
	f.close()
