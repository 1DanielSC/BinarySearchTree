# Binary Search Tree Project

![GitHub last commit](https://img.shields.io/github/last-commit/1danielsc/BinarySearchTree)  ![GitHub issues](https://img.shields.io/github/issues-raw/1danielsc/BinarySearchTree)  [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)



> Status: Developing ⚠️


## Table of Contents

  - [Description](#1-description)
  - [Installation](#2-installation)
  - [Code details](#3-code-details)
  - [How to run it](#4-how-to-run-it)
  - [Roadmap](#5-roadmap)
  - [License](#6-license)


## 1. Description

This project is an implementation of Binary Search Tree data structure along with some of its algorithms in Python. 


This application is set to receive an input file consisting of sequential instructions to be executed. The instructions supported can be found at [Files](#33-files).


## 2. Installation
You should have [Python 3.10.0](https://www.python.org/downloads/release/python-3100/) version installed on your computer.


## 3. Code details

All details about the code and its implementation:

  - [Classes](#31-classes)
  - [Methods](#32-methods)
  - [Files](#33-files)

### 3.1 Classes

#### 3.1.1 Node

The element to be stored in a tree.

#### 3.1.1.1 Attributes

- self.key - Integer number
- self.left - Reference to the left subtree
- self.right - Reference to the right subtree


#### 3.1.1 Binary Tree

The Binary Tree class is the one which most of elementary methods of a Binary Tree is implemented, such as traversals, isBinarySearchTree(), getSize() and findKthElement().

#### 3.1.1.1 Attributes


- self.root - Reference to the node element that is the root of the tree


#### 3.1.2 Binary Search Tree

### 3.2 Methods



### 3.3 Files

#### 3.3.1 Input file

All operations have to be written sequentially on the file ***instructions.txt***.

The program will read each instruction at a time and execute it.

Operations suported:



<ul>

  <li>Insert [element]</li>
  <li>Remove [element]</li>
  <li>Search [element]</li>
  <li>Print</li>
  <li>FindKthElement [element]</li>
  <li>Size</li>

  <li>Traversals
    <ul>
      <li>Pre-order</li>
      <li>In-order</li>
      <li>Post-order</li>
      <li>Level-order</li>
    </ul>
  </li>

</ul>



Proper way to write on file: 
>OPERATION + WHITE_SPACE + ELEMENT 
>
>Instruction in CAPS followed by a white space and a number right after it if necessary.

Examples:

PRINT

INSERT 20



## 4. How to run it

This section will contain all the necessary information to run this application.

## 5. Roadmap

Features to be added to this project in the future:

- AVL Tree class.
- Support to read an input file consisting of ordered operations that the program must follow.
- More methods. For instance: median() and mean().
- Dedicated class to run the program.

## 6. License

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

[MIT licensed.]("https://github.com/1DanielSC/BinarySearchTree/blob/main/LICENSE")