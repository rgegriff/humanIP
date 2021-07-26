# humanIP
---------
Generate memorable, speakable strings from IPv4 addresses

## What is this?
This is a project centered around creating a universal system for translating IPv4 addresses into human-memorable, human-speakable strings. This is acomplished by maintaining a series of *humanIP wordlists* for many different languages (eventually)

## What does a humanIP address look like?
A humanIP address takes the form of `v<version_number>/<languagecode>:<word>-<word>-<word>-<word>`. Where each of the words corresponds to a byte from an IPv4 address. As an example, the ip address `127.0.0.1` corresponds to the humanIP address of `v1/en:muscle-abandon-abandon-access`. The words map directly from the decimal value of the byte onto a position specific version of a language's wordlist. The languagecode is based on the ISO 639-1 list of language codes for any languages where it makes sense for the sake of brevity, but may also use ISO 639-3 for languages where ISO 639-1 is not sufficiantly distinct.

## Human-memorable translations of IP addresses!? Isn't that just DNS?
This is *NOT* DNS. DNS is made up of a whole interconnected network of resolvers, nameservers, registrars, authorities. humanIP doesn't try to do any of that. humanIP is simply a way of representing numerical ip addresses in a more friendly format.

## How can I contribute?
The goal of this project is to be as useful as possible for as many people; To that end, contributions of libraries for encoding/decoding in differet languages would be appreciated; as well as contributions of wordlists, especially for non-english languages.

## What are the criteria for a wordlist?
There are a few attributes I have identified for what makes a good word list:

### inoffensive
It should go without saying, but I am going to say it anyway, absolutely none of the words in the wordlist should be slurs, profane, or even carry particularly negative connotations.

### simple
The words on a word list should be relatively simple. The first version of the English-language word list, for example, is pulled from a list of the 3000 most commonly used English words. The length of the words should tend toward shorter in length, but some can be up to 12 letters in length.

### distinct
Some work should be put into the word list to avoid words that lookalike, soundalike, rhyme, or can sound similar if spoken in different accents. Obviously, this is a non-trivial task. This attribute in particular is the reason for having support for different versions of wordlists. If there is a common pair of words that we discover are confusing, we can always address that in a later version of the wordlist.

### lexographically sorted
one interesting aspect of the wordlists is that they are sorted lexographically (where languages allow for such a thing) to give an indirect impression of the magnitude of the bytes represented. Is this particularly useful? No. But it *is* neat!

## Can I incorporate this concept into my project?
Yes! Absolutely! All code in this repository is licensed under the MIT license; so go for it! If you do incorporate it into any user-facing aspects of your project there are some I wish for you to follow:

- Only use the name humanIP to describe the string if you are using the *official* address structure, generated using an *official* version of an *official* wordlist. I can't stop you from using a different wordlist, or a different address structure; but please avoid confusing everyone by calling it humanIP if you do! :)
- A link back to the project would be much appreciated! Help spread the idea!

## @todo(anyone)

- [x] Create initial english language wordlist
- [x] Create prototype Python library
- [ ] Create github pages site to provide an easy way to encode/decode humanIPs as well as provide informantion on the project
- [ ] Colaborate with speakers of other languages to create wordlists in other languages

