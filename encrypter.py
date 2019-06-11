# first we gotta create a function in which we can split a bunch of characters 
text = input("Please Input Your message :) ")
divided = list(text) # THIS IS THE STATEMENT I WHICH I DIVIDE THE USER INPUT(/STR/) 
dictionary = {
    'a' : 'n',
    'b' : 'o',
    'c' : 'p',
    'd' : 'q',
    'e' : 'r',
    'f' : 's',
    'g' : 't',
    'h' : 'u',
    'i' : 'v',
    'j' : 'w',
    'k' : 'x',
    'l' : 'y',
    'm' : 'z',
    'z' : 'm',
    'y' : 'l',
    'x' : 'k',
    'w' : 'j',
    'v' : 'i',
    'u' : 'h',
    't' : 'g',
    's' : 'f',
    'r' : 'e',
    'q' : 'd',
    'p' : 'c',
    'o' : 'b',
    'n' : 'a',
    ' ' : ' ',
    'A' : 'N',
    'B' : 'O',
    'C' : 'P',
    'D' : 'Q',
    'E' : 'R',
    'F' : 'S',
    'G' : 'T',
    'H' : 'U',
    'I' : 'V',
    'J' : 'W',
    'K' : 'X',
    'L' : 'Y',
    'M' : 'Z',
    'Z' : 'M',
    'Y' : 'L',
    'x' : 'K',
    'W' : 'J',
    'V' : 'I',
    'U' : 'H',
    'T' : 'G',
    'S' : 'F',
    'R' : 'E',
    'Q' : 'D',
    'P' : 'C',
    'O' : 'B',
    'N' : 'A',
}




panchat = ['result',' ','>' , ' ',' ',' ',' ',' ' ,' ' ,' ' ,' ' ] 


mac = list


for i in divided:
    mac = dictionary[i]  
    m = panchat.append(mac)

main_result =  ''.join(panchat)
print(main_result)
