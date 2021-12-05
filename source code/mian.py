from pynput.keyboard import Key, Listener, Controller
import pyautogui as pya
import pyperclip

English = [
	'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]

Hewbrew = [
	'א',
	'ב',
	'ג',
	'ד',
	'ה',
	'ו',
	'ז',
	'ח',
	'ט',
	'י',
	'כ',
	'ל',
	'מ',
	'נ',
	'ס',
	'ע',
	'פ',
	'צ',
	'ק',
	'ר',
	'ש',
	'ת',
]

keyboard = Controller()

def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    return pyperclip.paste()

def changeLanguge(text):
	finelText = ""
	EL = {
		't': 'א',
		'c': 'ב',
		'd': 'ג',
		's': 'ד',
		'v': 'ה',
		'u': 'ו',
		'z': 'ז',
		'j': 'ח',
		'y': 'ט',
		'h': 'י',
		'f': 'כ',
		'k': 'ל',
		'n': 'מ',
		'b': 'נ',
		'x': 'ס',
		'g': 'ע',
		'p': 'פ',
		'e': 'ק',
		'm': 'צ',
		'r': 'ר',
		'a': 'ש',
		',': 'ת',
		'w': "'",
		'q': '/',
		'i': 'ן',
		'o': 'ם',
		';': 'ף',
		'l': 'ך',
		'.': 'ץ',
		'/': '.',
        'T': 'א',
		'C': 'ב',
		'D': 'ג',
		'S': 'ד',
		'V': 'ה',
		'U': 'ו',
		'Z': 'ז',
		'J': 'ח',
		'Y': 'ט',
		'H': 'י',
		'F': 'כ',
		'K': 'ל',
		'N': 'מ',
		'B': 'נ',
		'X': 'ס',
		'G': 'ע',
		'P': 'פ',
		'E': 'ק',
		'M': 'צ',
		'R': 'ר',
		'A': 'ש',
		'W': "'",
		'Q': '/',
		'I': 'ן',
		'O': 'ם',
		'L': 'ך',
	}
	HL = {
		'ש': 'a',
		'נ': 'b',
		'ב': 'c',
		'ג': 'd',
		'ק': 'e',
		'כ': 'f',
		'ע': 'g',
		'י': 'h',
		'ן': 'i',
		'ח': 'j',
		'ל': 'k',
		'ך': 'l',
		'צ': 'm',
		'מ': 'n',
		'ם': 'o',
		'פ': 'p',
		'/': 'q',
		'ר': 'r',
		'ד': 's',
		'א': 't',
		'ו': 'u',
		'ה': 'v',
		"'": 'w',
		'ס': 'x',
		'ט': 'y',
		'ז': 'z',
	}
	
	if text[0] in English or text[1] in English:
		for char in text:
			if char in EL:
				finelText += EL[char]
			else:
				finelText += char
				
	elif text[0] in Hewbrew or text[1] in Hewbrew:
		for char in text:
			if char in HL:
				finelText += HL[char]
			else:
				finelText += char
				
	return finelText


def on_press(key):
    if str(key) == 'Key.f9':
        var = copy_clipboard()
        changeLanguge(var)
        keyboard.type(changeLanguge(var))

with Listener(on_press=on_press) as listener:
    listener.join()
