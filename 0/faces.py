def convert(text:str):
    if '(:' in text:
        text2=text.replace('(:','🙂')
    if '):' in text:
        text2=text2.replace('):','🙁')    
    return text2



def main():
     text=input()
     print(convert(text))


main()