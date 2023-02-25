# Rhasspy_Google_STT
<b>[CAT]<br></b>
Imatge Docker actualitzada per poder emprar Google Speech To Text.

Aquesta imatge és una actualització de la feina feta en [NullEnt1ty/GCloudSpeech](https://github.com/NullEnt1ty/GCloudSpeech) que es basa en la imatge base [LuisMalhadas/rhasspy](https://github.com/LuisMalhadas/rhasspy).

Reviseu que li heu configurat un fitxer d'autentificació que permeti fer ús de el Google Cloud API. En cas de dubte podeu revisar [la informació oficial de Google](https://cloud.google.com/docs/authentication/getting-started)

Després de la instal·lació s'ha de modificar el fitxer GCloudSpeech\google-stt.py amb el camí al vostre fitxer de credencials (per exemple "credentials.json")

Inclou els fitxers necessaris per possibilitar emprar nombres en català en Rhasspy.

Espero que us sigui d'utilitat ;-)
<br><br>
<b>[ENG]<br></b>
Rhasspy with a addon for use Google Speech to Text

This is a update from [NullEnt1ty/GCloudSpeech](https://github.com/NullEnt1ty/GCloudSpeech) work and from docker image from [LuisMalhadas/rhasspy](https://github.com/LuisMalhadas/rhasspy)

Make sure that you’re providing valid authentication credentials in order to use the Google Cloud API. Head over to https://cloud.google.com/docs/authentication/getting-started for more information.

<b>After installation yous must update GCloudSpeech\google-stt.py with the path to your credentials.json.</b>

Include the necesary files to have the possibility to use numbers in catalan correctly.

I hope that help you ;-)
