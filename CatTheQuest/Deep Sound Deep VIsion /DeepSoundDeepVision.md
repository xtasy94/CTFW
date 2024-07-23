# CatTheQuest: Deep Sound Deep Vision
**Title:** Deep Sound Deep Vision

**Description:** Sounds can be seen and colors can be heard, as an old proverb goes. Deep sound, deep vision, it's 2.0, not just any vision. You hear a strange, somewhat goofy noise, reminiscent of a monster. This monster seems to swallow words, hiding precious secrets. An attentive ear and the right tools could reveal... the monsters. Can you hear the hidden truth? Can you see what lies behind the sound?

**Challenge Help:**
Use this information to achieve the resolution of the challenge,
Google Drive file here: [_YOU.wav](https://drive.google.com/file/d/1Uv_BtOptZIH_hQKTaKXFyLFkKrFa1Cm9/view?usp=sharing)

**Hint:** No hint.

## Solution:
Upon listening to the audio, it seems there is nothing hidden within it. Therefore, there might be something hidden behind it. Let's begin by examining its spectrogram in [Audacity](https://www.audacityteam.org/download/): 

![Audacity](https://github.com/xtasy94/CTFW/blob/main/CatTheQuest/Deep%20Sound%20Deep%20VIsion%20/Files/Audacity.png)

The spectrogram reveals the message: 'CODE: THE_MONSTER_IS'. It appears incomplete. Considering the audio file's name, '_YOU', it seems to complement the partial code from the spectrogram. Therefore, the full code is likely 'THE_MONSTER_IS_YOU'. The next step is to determine what this code might be used for.
Considering the challenge title, 'Deep Sound Deep Vision,' it suggests a possible involvement of the software ['Deepsound 2.0.'](https://deepsound.en.uptodown.com/windows) A tool used for steganography and audio conversion, allowing users to hide secret data within audio files and also extract hidden files from audio files or CD tracks.

Upon opening the file in DeepSound 2.0, we are prompted to enter a password. After entering the correct password, we can access a hidden file named ['MONSTERS.txt'](https://github.com/xtasy94/CTFW/blob/main/CatTheQuest/Deep%20Sound%20Deep%20VIsion%20/Files/MONSTERS.txt), we extract the file and save it.

We look at the MONSTERS.txt and we can see that there is something that can be helpful to us, now we write a script that can extract and print all sequences of two or more consecutive digits from the `MONSTERS.txt` file, [extract.py](https://github.com/xtasy94/CTFW/blob/main/CatTheQuest/Deep%20Sound%20Deep%20VIsion%20/Files/extract.py): 

![Image](https://github.com/xtasy94/CTFW/blob/main/CatTheQuest/Deep%20Sound%20Deep%20VIsion%20/Files/carbon.png)

Next, we take the output and input it into [CyberChef](https://cyberchef.org/). In the Recipe tab, drag the "From Decimal" operation into the workspace and set the delimiter to "Line Feed", which gives us our flag in the output: `CAT{Look_Behind_You_HaHaHa}`
