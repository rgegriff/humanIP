'''
A prototype library for encoding/decoding humanIP addresses
'''
import os

class InvalidHumanIP(Exception):
    pass

class WordlistDoesNotExist(Exception):
    pass

def load_wordlist(version, language):
    """
    takes the version and langage and returns an ordered list of words
    """
    curdir = os.path.dirname(__file__)
    wordlist_filename = "v{}{}.txt".format(version, language)
    wordlist_path = os.path.join(curdir, "wordlists_official", wordlist_filename)
    with open(wordlist_path, "r") as wordfile:
        wordlist = wordfile.read().split("\n")
    wordlist.remove('') # remove a blank entry caused by a trailing newline
    return wordlist

def parse_humanip(humanip_str):
    """
    takes a humanip like string and return a dictionary containing wordparts
    example:
      humanip_str == "v1/en:muscle-abandon-abandon-access"
      will return
      {
        'version': 1, 
        'language': "en",
        'words': ["muscle", "abandon", "abandon", "access"]
      }
    """
    parsed = {'version': None, 'language': None, 'words': []}
    version_language, words = humanip_str.split(":")
    version, language = version_language.split("/")
    word_list = words.split("-")
    parsed['version'] = int(version.strip("v"))
    parsed['language'] = language
    parsed['words'] = word_list
    return parsed

def encode_humanip(version, language, ip_addr):
    """
    takes a wordlist version, language, and IPv4 address and returns a humanIP
    (1, "en", "127.0.0.1") -> "v1/en:muscle-abandon-abandon-access"
    """
    wordlist = load_wordlist(version, language)
    words = (wordlist[int(b)] for b in ip_addr.split("."))
    humanip_str = "v{}/{}:{}-{}-{}-{}".format(version, language, *words)
    return humanip_str
    

def decode_humanip(humanip_str):
    """
    takes a humanip string and returns the corresponding decimal IPv4 address
    ("v1/en:muscle-abandon-abandon-access") -> "127.0.0.1"
    """
    parsed = parse_humanip(humanip_str)
    wordlist = load_wordlist(parsed['version'], parsed['language'])
    ip_addr = ".".join( (str(wordlist.index(word)) for word in parsed['words']) )
    return ip_addr

