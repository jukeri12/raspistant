** What is this **

* Raspistant * is a sweet and simple text-to-speech driven assistant created with Raspberry Pi in mind.
It can be run on any Python-enabled system though for now, but future updates may break this.
Basically it is like a robotic assistant that can notify you of things that you set it to notify about
using the pyttsx text-to-speech module.

** Requirements **
pyttsx => 1.1

Pyttsx also requires a text-to-speech engine to run on.
    ** Unix ** : espeak
    ** Windows ** : SAPI5
    ** Mac ** : NSSpeechSynthesizer
    see pyttsx documentation for more info.

** Features **

-Notify user of daily things using a simple ini-file


** Quick start **

You can set pyttsx related settings in pyttsx-settings.ini (see .example file for examples of settings and refer
to pyttsx documentation for more detailed info.) You can assign notifications in notifications.ini (see notifications.ini.example
for examples of notifications) by writing a time in HH:MM format and a text for the speech engine to speak.


** Future features **
-Interface with motion, heat etc sensors installed on the Raspi
-REST integration for getting data from various REST services
-A more personal and smart assistant possibly