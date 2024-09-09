"""
The Challenge

We have five favorite songs named A, B, C, D, and E.
We’ve created a playlist of these songs and are using an app to manage the
playlist.

The songs start off in the order A, B, C, D, E. The app has four buttons:
- Button 1: Moves the first song of the playlist to the end of the playlist.
  For example:
      - If the playlist is currently A, B, C, D, E,
        then it changes to B, C, D, E, A.
- Button 2: Moves the last song  to the beginning of the playlist.
  For example:
      - If the playlist is currently A, B, C, D, E,
        then it changes to E, A, B, C, D.
- Button 3: Swaps the first two songs of the playlist.
  For example:
  If the playlist is currently A, B, C, D, E,
  then it changes to be B, A, C, D, E.
- Button 4: Plays the playlist!

We’re provided a user’s button presses.
When the user presses button 4, output the order of songs in the playlist.

Input

The input consists of pairs of lines, where the first line of a pair gives the
number of a button (1, 2, 3, or 4), and the second gives the number of times
that the user pressed this button (between 1 and 10).
That is, the first line is the number of a button, the second line is the
number of times it is pressed, the third line is the number of a button,
the fourth line is the number of times it is pressed, and so on.
The input ends with these two lines:

4 1
indicating that the user pressed button 4 once.

Output

Output the order of songs in the playlist after all button presses.
The output must be on one line, with a space separating each pair of songs.
"""


def get_playlist(presses):
    playlist = ["A", "B", "C", "D", "E"]
    for move in presses:
        button = move[0]
        times = move[1]
        if button == 1:
            for _ in range(times):
                playlist.append(playlist.pop(0))
        elif button == 2:
            for _ in range(times):
                playlist.insert(0, playlist.pop())
        elif button == 3:
            for _ in range(times):
                playlist[0], playlist[1] = playlist[1], playlist[0]
        elif button == 4:
            return " ".join(playlist)
