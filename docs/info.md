<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

A Moore Sequence Detector is a Finite State Machine (FSM) that checks if a specific bit pattern (sequence) appears in a serial input stream. In a Moore machine, the output depends only on the current state, not on the input directly.
1. Components

States → Each state represents how much of the target sequence has been matched so far.

Transitions → Based on the current input bit (0 or 1), the FSM moves to the next state.

Output → In a Moore machine, the output is associated with states (not transitions).

Output = 1 only in the final state (when full sequence is detected).

Output = 0 in all other states.

## How to test

State Transitions
Current State	Input = 0 → Next State	Input = 1 → Next State
S0	S0	S1
S1	S2	S1
S2	S0	S3
S3	S2	S4
S4	S2	S1
## External hardware
Start in S0 (reset state).

Input bits come one by one:

If input = 1, go to S1 (matched first bit).

Next bit 0 → go to S2 (matched 10).

Next bit 1 → go to S3 (matched 101).

Next bit 1 → go to S4 (full match 1011).

In S4, output = 1 for one cycle (Moore output).

Then FSM moves based on next input (for overlap).
List external hardware used in your project (e.g. PMOD, LED display, etc), if any
