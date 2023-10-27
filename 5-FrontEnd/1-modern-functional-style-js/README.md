# Modern functional-style Javascript

## Instructor Notes & Prerequesites

Some previous JS programming experience is required; students should already be able to write and run JS programs locally and be comfortable writing programs in JS somewhat beyond the beginner level.

**The instructor should demo the beginning parts of the assignment (video store logic) as a tutorial during class time.**

## Lectures & Assignments

### Lectures

1. [Intro to the node ecosystem - npm, yarn, node projects, CommonJS Modules vs ESModules](./intro-to-node-ecosystem-modules.md)
2. [Modern functional-style Javascript](./modern-js.md)

### Assignments

- [Create the logic for a video store using the tools we have learned](https://github.com/Code-Platoon-Assignments/video-store-0-functional-js-and-state)

## What are we trying to accomplish?

In preparation for working with React.js (a frontend JS UI framework) we will review JS, look at some more advanced coding styles which are the modern way of writing Javascript, and become more familiar with the tooling needed to manage different versions of node.js, install node packages, import/export Javascript from one file to another, and get a preview of the build tools (such as vite or create-react-app) needed to do modern frontend development.

## TLO's (Testable Learning Objectives)

### Basic proficiency with functional-style javascript

- Comfortable with arrow functions, object destructuring, array destructuring
- Able to use `.foreach()`, `.map()`, `.filter()`, `.reduce()`
  - Over arrays with strings, numbers, and booleans
  - Over arrays containing objects or nested arrays - more complex data shapes
  - Able to do method chaining w/the above
  - Able to use all of the above to write nontrivial programs

### Node projects

- Able to create a new node project with npm and explain the basic project structure to someone else.
  - Able to add an npm script to `package.json`
- Familiar with the node package ecosystem (npm, yarn) and able to use npm and install node modules.
- Able to create a basic `.gitignore` file for a node project 

### Importing / Exporting modules

- Understands that ESModules are best practice
- Able to set up a node project to use  ESModules
- Able to import/export with both CommonJS and ESModules


### Node / JS modules

- Familiar with  and able to use `require`
- Familiar with and able to use `import` and `export`

### Frontend build tooling

- Able to create a "hello world" frontend project with vite and has introductory familiarity with the tooling & project structure.

## ELO's (Elective Learning Objectives)

- Somewhat familiar with the node package ecosystem
  - npm vs yarn
  - insecurity - [the leftpad fiasco](https://www.theverge.com/2016/3/24/11300840/how-an-irate-developer-briefly-broke-javascript)
  - CommonJS modules vs ESModules
- Beginnging to learn that build tooling is a big deal, especially in JS-land
- Beginning to learn that project structure is a big deal
