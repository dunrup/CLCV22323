# Definitions
- **JavaScript** - a programming language. 

- **Node.js** - Javascript's runtime environment.
    - **runtime environment** - a place where stuff coded in a language runs.

- **NPM** (Node Package Manager) - the default package manager for Node.js, JavaScripts runtime.
    - **package manager** automates the process of installing, upgrading, configuring, and removing programs.
    - **NPM** comprises a CLI (command line interface) and an online repository that hosts JavaScript packages.

- **NVM** (Node Version Manager) - a version manager that allows you to install and use different versions of node via the command line.
    - [**nvm-Windows**](https://github.com/coreybutler/nvm-windows), which will soon be replaced by [Runtime](https://github.com/coreybutler/nvm-windows/wiki/Runtime) (a program, not to be confused with little r runtime)

- [**nw.js**](https://nwjs.io/), (previously known as node-webkit) lets you call all Node.js modules directly from DOM.
    - **DOM** (Document Object Model) is the data representation of the objects that comprise the structure and content of a document on the web. It is a programming interface for web documents.
    - I still don't really know what either of these things mean.

-[**nw-builder module**](https://github.com/nwutils/nw-builder)  Lets you build your NW.js apps for mac, win and linux via cli. It will download the prebuilt binaries for a newest version, unpacks it, creates a release folder, create the app.nw file for a specified directory and copies the app.nw file where it belongs."


note: I can't believe I'm doing all this just to change a fucking font size

# The Journey
I wanted to mess with the app [Myosotis](https://github.com/gebrkn/Myosotis). To do this, I learned that I could download the code and edit it in VSCode here, but I didn't know how to then package and run the code I was using. 

Georgios pointed me [here](https://stackoverflow.com/questions/37648756/how-to-package-a-nw-js-application-on-windows/37649349#37649349). These are instructions on how to package a NW.js app on Windows. So I need to package this app, which was coded with NW.js. To do so, I needed to install Node.js and NPM, which I did by first installing nvm-Windows. Then I installed the nw-builder module

try following these instrutions
https://github.com/nwjs/nw.js

    
    


        
        


