@template: post.html
@title: Music composing assistant
@date: 28-04-2020
@tags: big-data spark scala

# Music composing assistant

- use Ludwig from Uber for seq2seq
- get notes/chords from midi files using music21 python library and create sequences
- train with seq2seq:
	- chords -> notes
	- notes  -> chords
	- base   -> drum
	- etc...

