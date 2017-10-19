import re

def preprocess(text_input):
    text_input = re.sub(r'(#(S|s)arcasmo|#(I|i)ron(i|\W)a)','',text_input)
    text_input = re.sub(r'#SARCASMO|#IRON(I|\W)A','',text_input)
    text_input = re.sub(r'https?://t.co/.\w*','http://link', text_input)
    text_input = re.sub(r'@.\w*','@',text_input)
    text_input = re.sub(r'#','',text_input)
    return text_input
