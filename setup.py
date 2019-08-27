#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os
import json
import urllib2
import subprocess

name = ''
email = ''
options = {
    'ssh': '',
    'ios': '',
    'android': '',
    'web': '',
    'dev': '',
    'extras': '',
}


# Check if Xcode Command Line Tools are installed
if os.system('xcode-select -p') != 0:
    print "Installing XCode Tools"
    os.system('xcode-select --install')
    print "**************************************************************"
    print "Install the XCode Command Line Tools and run this script again"
    print "**************************************************************"
    exit()


# Hello message
print "\n\nAnd we lived beneath the waves In our yellow submarine.\n"


# Basic Info
while name == '':
    name = raw_input("What's your name?\n").strip()

while email == '' or '@' not in email:
    email = raw_input("What's your email?\n").strip()

print "Hi %s!" % name
print "You'll be asked for your password at a few points in the process"
print "Setting up your Mac..."


# Setup Options
while options['dev'] not in ['y', 'n']:
    options['dev'] = raw_input(
        "Do you want to install general Dev Tools? (%s)  " % '|'.join(['y', 'n']))

while options['ssh'] not in ['y', 'n']:
    options['ssh'] = raw_input(
        "Do you want to generate your ssh keys? (%s)  " % '|'.join(['y', 'n']))

while options['web'] not in ['y', 'n']:
    options['web'] = raw_input(
        "Do you want to install Web Developer Tools? (%s)  " % '|'.join(['y', 'n']))

while options['android'] not in ['y', 'n']:
    options['android'] = raw_input(
        "Do you want to install Android Tools? (%s)  " % '|'.join(['y', 'n']))

while options['ios'] not in ['y', 'n']:
    options['ios'] = raw_input(
        "Do you want to install iOS Tools? (%s)  " % '|'.join(['y', 'n']))

while options['extras'] not in ['y', 'n']:
    options['extras'] = raw_input(
        "Do you want to install Extras? (%s)  " % '|'.join(['y', 'n']))


# Install Brew & Brew Cask
print "Installing Brew & Brew Cask"
os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
os.system('brew tap homebrew/bundle')
os.system('brew tap caskroom/cask')
os.system('brew update && brew upgrade && brew cleanup && brew cask cleanup')


# Install Git
print "Installing Git"
os.system('brew install git')

os.system('git config --global user.name "%s"' % name)
os.system('git config --global user.email "%s"' % email)
os.system('git config --global color.ui auto')


##
# Here you can add additional install statements for each category
# NOTE: Don't forget that if you want to modify the categories you
# have to update the `raw_input` statements above
##

# Install Dev
if options['dev'] == 'y':
    print "Installing Dev Tools"
    os.system('brew install tree')
    os.system('brew cask install postman')


# Install Web
if options['web'] == 'y':
    print "Installing Web Tools"
    os.system('brew install nvm')
    os.system('brew cask install docker')


# Install Android
if options['android'] == 'y':
    print "Installing Android Tools"
    os.system('brew cask install java')
    os.system('brew cask install android-studio')


# Install iOS
if options['ios'] == 'y':
    print "Installing iOS Tools"
    print "We need your password"
    os.system('sudo gem install cocoapods')


# Install Extras
if options['extras'] == 'y':
    print "Installing Extras"
    os.system('brew cask install vlc')
    os.system('brew cask install spotify')
    os.system('brew cask install spectacle')
    os.system('brew cask install slack')
    os.system('brew cask install notion')


# Install ssh
if options['ssh'] == 'y':
    if not os.path.isfile(os.path.expanduser("~") + '/.ssh/id_rsa.pub'):
        print "Creating your Private Key"
        os.system(
            'ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N "" -C "%s"' % email)
    print "Your SSH Public Key Is:"
    with open(os.path.expanduser("~") + '/.ssh/id_rsa.pub', 'r') as f:
        print f.read()
    print ""


# Clean Up
os.system('brew cleanup && brew cask cleanup')


print "*************************************"
print "Remember to restart your Mac"
print "All done! Enjoy your new macOS!"
print "*************************************"
