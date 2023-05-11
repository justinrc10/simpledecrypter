# simpledecrypter
A decrypter for simple encryptions

An encryption is an invertible function used to obfuscate information. 
A simple encryption is an encryption defined by replacing the representation of a symbol. 

For example, an alphabetical message can be encrypted by replacing every letter with its numerical position in the alphabet. 
That is, a = 1, b = 2, c = 3, and so on. 
With this simple encryption, the message "helloworld" would be encrypted as "6 5 12 12 15 23 15 18 12 4".

Thus, for a message encrypted using a simple encryption, one can only decipher the "structure" or "shape" of the decrypted message. 
That is, one can only say whether letters are used multiple times and in what positions. 
In the encrypted message:

"6 5 12 12 15 23 15 18 12 4"

We can see that whatever letter that represents 12 is used in the 3rd, 4th, and 9th position of the message, and whatever letter that represents 15 is used in the 5th and 7th position of the message. 
From here, we can compare the shape of this word to existing words and select the most reasonable match from addtional context.

This program takes in the shape of an encrypted message, which symbols are already correct, and outputs matches from a large lexicon. 
For example, upon running the program,


  Enter encrypted message:
  
  12llo 3o4l5
  
  Which of these characters are correct?
  
  lo


The output will be


  cello boils

  cello bowls

  cello doily

  cello foals

  cello foils

  ...

  hello toils

  hello world

  hello would

  ...

  hullo toils

  hullo voile

  hullo world


From context, the decrypted message is most likely "hello world".
