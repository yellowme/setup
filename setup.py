#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os
import json
import urllib2
import subprocess

name = ''
email = ''
options = { 'ssh': '', }

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


# Install Brew & Brew Cask
print "Installing Brew & Brew Cask"
os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
os.system('brew tap homebrew/bundle')
os.system('brew tap caskroom/cask')
os.system('brew update && brew upgrade && brew cleanup && brew cask cleanup')


# Install Languages
print "Installing Git"
os.system('brew install git')

os.system('git config --global user.name "%s"' % name)
os.system('git config --global user.email "%s"' % email)
os.system('git config --global color.ui auto')

print "Installing Essential Apps"
os.system('brew cask install slack notion')

# Clean Up
os.system('brew cleanup && brew cask cleanup')

# Ask for ssh
while options['ssh'] not in ['y', 'n']:
    options['ssh'] = raw_input(
        "Do you want to generate your ssh keys? (%s)  " % '|'.join(['y', 'n']))

if options['ssh'] == 'y':
    if not os.path.isfile(os.path.expanduser("~") + '/.ssh/id_rsa.pub') :
        print "Creating your Private Key"
        os.system('ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N "" -C "%s"' % email)
    print "Your SSH Public Key Is:"
    with open(os.path.expanduser("~") + '/.ssh/id_rsa.pub', 'r') as f:
        print f.read()
    print ""

print "*************************************"
print "Remember to restart your Mac"
print "All done! Enjoy your new macOS!"
print "*************************************"
