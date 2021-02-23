# PICO_MORSE_ENCODER


The code is designed to run in a raspberry pi Pico controller.
You can just copy and paste the code in an ide like THONNY and loaded it into your pico. 

Following standards was followed for the timing. Unit time can be changed in the code defined by the unit_time variable.

The timing in Morse code is based around the length of one "dit" (or "dot" if you like). From the dit length we can derive the length of a "dah" (or "dash") and the various pauses:

Dit: 1 unit

Dah: 3 units

Intra-character space (the gap between dits and dahs within a character): 1 unit

Inter-character space (the gap between the characters of a word): 3 units

Word space (the gap between two words): 7 units
